"""v2版本打包

"""

import json
import logging
import os
import re
import sys
import time
from typing import Dict

logging.basicConfig(
    handlers=[
        logging.FileHandler(
            f"{time.strftime('%Y-%m-%d', time.localtime()) }.log", encoding="utf-8"
        ),
        logging.StreamHandler(sys.stderr),
    ],
    level=logging.DEBUG,
    format="%(asctime)s %(filename)s %(levelname)s %(message)s",
    datefmt="%a %d %b %Y %H:%M:%S",
)

INDEX_SET = set()


def init_index_file(index_file: str):
    """Load user-defined dictionary index to prevent it from being empty after the jump
        加载用户自定义的词典索引，防止出现跳转后为空的情况

    Args:
        index_file (str): user-defined dictionary index file path
    """
    with open(index_file, "r", encoding="utf-8") as f:
        for line in f:
            # Skip entries similar to たべる【食べる】,
            # which are usually used in Japanese electronic dictionaries to save meanings
            # 跳过类似たべる【食べる】的词条，日语电子词典通常使用这种词条保存释义
            if "【" not in line:
                INDEX_SET.add(line.replace("\n", ""))


def convert_hira_to_kata(input_text: str) -> str:
    """Convert hiragana to katakana in the given text.
    将平假名转为片假名

    Args:
        input_text (str): A String containing the hiragana.

    Returns:
        str: The text with hiragana converted to katakana.
    """
    output_text = ""
    for gana in input_text:
        # 关于取值范围，请阅读下面的链接
        # Read url for why the condition is 12352 and 12438
        # https://www.unicode.org/charts/PDF/U3040.pdf
        gana_code = int(ord(gana))
        if 12352 < gana_code < 12438:
            hira = chr(gana_code + 96)
            output_text = output_text + hira
        else:
            output_text = output_text + gana
    return output_text


CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
os.chdir(CURRENT_PATH)


rule_path = os.path.join(CURRENT_PATH, r"rule")
INDEX_PATH = os.path.join(CURRENT_PATH, r"index")
PROCESS_PATH = os.path.join(CURRENT_PATH, r"process")


def do_inflect(rules_dict: Dict[str, list[str]], index_file: str, process_file: str):
    """根据规则穷举所有非辞書形

    Args:
        rules_dict (Dict[str, list[str]]): 穷举非辞書形时参考的规则
        index_file (str): 依据词性分类的文件
        process_file (str):穷举出的非辞書形保存的地址
    """
    with open(index_file, "r", encoding="utf-8") as input_file, open(
        process_file, "w", encoding="utf-8"
    ) as output_file:
        for line in input_file:
            line = line.replace("\n", "")
            if line != "":
                variant = line.split("\t")[0]
                jishokei = line.split("\t")[1]
                if jishokei not in INDEX_SET:
                    # 用户辞典未收录该词
                    logging.critical(
                        "%s is not included in index.txt, you should add this word to index.txt",
                        jishokei,
                    )
                # 忽略用户辞典中已收录的非辞書形，
                if variant not in INDEX_SET:
                    output_file.write(variant + "\t" + jishokei + "\n")
                # 通过词尾假名加载相应的规则
                variant_last_letter = variant[-1]
                rules: list[str] = rules_dict.get(variant_last_letter, [])
                # 没有词尾假名对应的规则，需要检查对应的rule.json文件
                if len(rules) == 0:
                    logging.error(
                        "variant last letter is %s, not in rule.json file!",
                        variant_last_letter,
                    )
                variant_stem = variant[0:-1]
                for rule in rules:
                    output_file.write(variant_stem + rule + "\t" + jishokei + "\n")


def do_v1_inflect(index_file: str, process_file: str):
    """穷举一段动词的连用形一（比如：食べにいく），这种活用是直接去掉了词尾处的假名，所以需要单独处理"""
    with open(index_file, "r", encoding="utf-8") as input_file, open(
        process_file, "a", encoding="utf-8"
    ) as output_file:
        for line in input_file:
            line = line.replace("\n", "")
            if line != "":
                variant = line.split("\t")[0]
                jishokei = line.split("\t")[1]
                if jishokei not in INDEX_SET:
                    logging.critical(
                        "%s is not included in index.txt, you should add this word to index.txt",
                        jishokei,
                    )

                variant_stem = variant[0:-1]
                output_file.write(variant_stem + "\t" + jishokei + "\n")


def do_sahenn_inflect(
    rules_dict: Dict[str, list[str]], index_file_path: str, process_file_path: str
):
    """根据规则穷举サ変动词的所有非辞書形

    Args:
        rules_dict (Dict[str, list[str]]): 穷举非辞書形时参考的规则
        index_file (str): 依据词性分类的文件
        process_file (str):穷举出的非辞書形保存的地址
    """
    with open(index_file_path, "r", encoding="utf-8") as input_file, open(
        process_file_path, "w", encoding="utf-8"
    ) as output_file:
        for line in input_file:
            line = line.replace("\n", "")
            if line != "":
                variant = line.split("\t")[0]
                jishokei = line.split("\t")[1]
                if jishokei not in INDEX_SET:
                    # 用户辞典未收录该词
                    logging.critical(
                        "%s is not included in index.txt, you should add this word to index.txt",
                        jishokei,
                    )
                # 忽略用户辞典中已收录的非辞書形，
                if variant not in INDEX_SET:
                    output_file.write(variant + "\t" + jishokei + "\n")
                # 定义穷举规则
                rules: list[str]
                if variant[-1] != "る":
                    # 形如【卒す】这样活用词尾是1个假名的单词
                    variant_last_letter = variant[-1]
                    rules = rules_dict.get(variant_last_letter, [])
                    variant_stem = variant[0:-1]
                else:
                    # 形如【卒する】这样活用词尾是2个假名的单词
                    variant_last_letter = variant[-2:]
                    rules = rules_dict.get(variant_last_letter, [])
                    variant_stem = variant[0:-2]

                if len(rules) == 0:
                    # 如果没有词尾假名对应的规则，提醒用户检查对应的 rule.json 文件
                    logging.error(
                        "variant last letter is %s, not in rule.json file!",
                        variant_last_letter,
                    )

                for rule in rules:
                    output_file.write(variant_stem + rule + "\t" + jishokei + "\n")


def do_hira_inflect():
    """根据规则穷举平假名的所有非辞書形"""
    with open(r"index/hiragrana.txt", "r", encoding="utf-8") as input_file, open(
        r"process/hiragrana.txt", "w", encoding="utf-8"
    ) as output_file:
        for line in input_file:
            line = line.replace("\n", "")
            if line != "":
                output_file.write(convert_hira_to_kata(line) + "\t" + line + "\n")
            if re.search(r"^(.*?)っと$", line):
                # 形如 【ぐっと】的单词 添加【グッと】这样部分转为片假名的非辞書形
                output_file.write(
                    convert_hira_to_kata(line[0:-2]) + "ッと" + "\t" + line + "\n"
                )


def inflect_adj():
    """穷举形容词的所有非辞書形"""
    adj_rule = init_rule(os.path.join(rule_path, r"adj.json"))
    adj_index = os.path.join(INDEX_PATH, r"adj.txt")
    adj_process = os.path.join(PROCESS_PATH, r"adj.txt")
    do_inflect(adj_rule, adj_index, adj_process)


def inflect_v1():
    """穷举一段动词的所有非辞書形"""
    v1_rule = init_rule(os.path.join(rule_path, r"v1.json"))
    v1_index_file = os.path.join(INDEX_PATH, r"v1.txt")
    v1_process_file = os.path.join(PROCESS_PATH, r"v1.txt")
    do_inflect(v1_rule, v1_index_file, v1_process_file)
    do_v1_inflect(v1_index_file, v1_process_file)


def inflect_v5():
    """穷举五段动词的所有非辞書形"""
    v5_rule = init_rule(os.path.join(rule_path, r"v5.json"))
    v5_index_file = os.path.join(INDEX_PATH, r"v5.txt")
    v5_process_file = os.path.join(PROCESS_PATH, r"v5.txt")
    do_inflect(v5_rule, v5_index_file, v5_process_file)


def inflect_sahenn():
    """穷举サ变动词的所有非辞書形"""
    sahenn_rule = init_rule(os.path.join(rule_path, r"sahenn.json"))
    sahenn_index_file = os.path.join(INDEX_PATH, r"sahenn.txt")
    sahenn_process_file = os.path.join(PROCESS_PATH, r"sahenn.txt")
    do_sahenn_inflect(sahenn_rule, sahenn_index_file, sahenn_process_file)


def inflect_hiragana():
    """穷举片假名的所有片假名非辞書形"""
    do_hira_inflect()


def inflect_noun():
    """穷举名词的非辞書形"""
    with open(r"index/noun.txt", "r", encoding="utf-8") as input_file, open(
        r"process/noun.txt", "w", encoding="utf-8"
    ) as output_file:
        for line in input_file:
            line = line.replace("\n", "")
            if line != "":
                variant = line.split("\t")[0]
                jishokei = line.split("\t")[1]
                if jishokei in INDEX_SET:
                    if variant not in INDEX_SET:
                        # 忽略词典中已收录的非辞書形
                        output_file.write(variant + "\t" + jishokei + "\n")
                else:
                    logging.critical(
                        "%s is not included in index.txt, you should add this word to index.txt",
                        jishokei,
                    )


def init_rule(file: str) -> Dict[str, list[str]]:
    """初始化规则

    Args:
        file (str): 规则文件路径

    Returns:
        dict: 以【"い": ["う", "か", "く", "け", "さ", "す", "み", "そ"]】的格式返回词尾假名的所有可能出现的情况
    """
    with open(file, "r", encoding="utf-8") as f:
        return json.loads(f.read())


def inflect_nonjishokei():
    """穷举非辞書形"""
    inflect_adj()
    inflect_v5()
    inflect_v1()
    inflect_sahenn()
    inflect_hiragana()
    inflect_noun()


init_index_file(os.path.join(CURRENT_PATH, r"index/index.txt"))

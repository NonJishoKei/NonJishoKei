"""convert a nonjishokei to a jishokei"""

import json
import os
from typing import Dict, List

from preprocess import preprocess


def read_rule_file(rule_file: str) -> Dict[str, list[str]]:
    """read json file
        加载规则文件

    Args:
        input_file (str): input file path

    Returns:
        dict: json file content
    """
    with open(rule_file, "r", encoding="utf-8") as f:
        return json.loads(f.read())


CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))

orthography_rule_path: str = os.path.join(CURRENT_PATH, "index_v3.json")
orthography_rule_dict: Dict[str, list[str]] = read_rule_file(orthography_rule_path)
conjugate_rule_path: str = os.path.join(CURRENT_PATH, "conjugate_rule.json")
conjugate_rule_dict: Dict[str, list[str]] = read_rule_file(conjugate_rule_path)
special_rule_path: str = os.path.join(CURRENT_PATH, "special_rule.json")
special_rule_dict: Dict[str, list[str]] = read_rule_file(special_rule_path)


def convert_orthography(input_text: str) -> list | None:
    """convert input text to the form of a word that appears as an entry in a dictionary,
        for example, convert【気づく】to【気付く】
        通过查询确认推导结果是否正确，同时消除假名书写造成的非辞書型，比如【気づく】和【気付く】

    Args:
        input_text (str): a form of a word that will not appear as an entry in a dictionary

    Returns:
        str: the form of a word that appears as an entry in a dictionary
    """
    if input_text in orthography_rule_dict:
        return orthography_rule_dict[input_text]
    else:
        return None


def convert_conjugate(input_text: str) -> list:
    """convert a verb conjugation to basic form.
        还原动词的活用变形

    Args:
        input_text (str): A String containing the conjugation.

    Returns:
        list: The list with conjugation converted to the basic form.
    """
    input_stem = input_text[0:-1]
    input_last_letter = input_text[-1]
    process_output_list: list[str] = []
    # 本程序的 input_stem 概念对应的不是一段动词语法意义上的词干
    # 今日は、寿司を**食べ**に銀座に行いきます。
    process_text = input_text + "る"
    process_output_list.append(process_text)

    jishokei_last_letter_list = conjugate_rule_dict.get(input_last_letter)
    if jishokei_last_letter_list is not None:
        for jishokei_last_letter in jishokei_last_letter_list:
            process_output_list.append(input_stem + jishokei_last_letter)

    # 将输入的字符串作为最后一个结果返回
    # 因为输入的字符串可能就是正确的辞書型
    if input_text not in process_output_list:
        process_output_list.append(input_text)

    # 删除其中的重复值，只保留第一次的结果
    output_list: List[str] = []
    for i in process_output_list:
        if i not in output_list:
            output_list.append(i)

    return output_list


def convert_nonjishokei(input_text: str) -> list:
    """Convert nonjishokei to jishokei.
        将非辞书形还原为辞书形

    Args:
        input_text (str): A String containing the nonjishokei.

    Returns:
        list:The list with nonjishokei converted to the jishokei.
    """
    # 还原动词的活用变形
    converted_conjugate_list = convert_conjugate(input_text)
    # 检查还原结果
    orthography_list: list[str] = []
    for i in converted_conjugate_list:
        orthography_text = convert_orthography(i)
        if orthography_text is not None:
            orthography_list.extend(set(orthography_text))
    output_list = []
    for i in orthography_list:
        output_list.append(i)
    return output_list


def scan_input_string(input_text: str) -> list:
    """Scans the input string by Maximum Matching and returns a list of possible jishokei.
        采用最长一致法扫描字符串，推导并返回所有可能的辞书形

    Args:
        input_text (str): The string to scan.
        output_max_length (int, optional): The maximum length of the returned results.

    Returns:
        list: A list of converted jishokei.
    """

    # 预处理
    input_text = preprocess(input_text)

    # 记录扫描的临时字符串
    scanned_input_list = []
    # 记录扫描过程中的推导结果
    scan_process_list = []
    for input_index in range(len(input_text) + 1):
        scanned_input_text = input_text[0 : input_index + 1]
        scanned_input_list.append(scanned_input_text)

        # 特殊规则
        special_output_text = special_rule_dict.get(scanned_input_text)
        if special_output_text is not None:
            for i in special_output_text:
                scan_process_list.append(i)

        # TODO 用户自定义的转换规则

        scan_output_text = convert_nonjishokei(scanned_input_text)
        for i in scan_output_text:
            scan_process_list.append(i)

    # 返回给用户的扫描结果
    scan_output_list: List[str] = []
    # 优先展示更长字符串的扫描结果，提高复合动词的使用体验
    for i in reversed(scan_process_list):
        # 只添加第一次的推导结果
        if i not in scan_output_list:
            # 不添加扫描过程中的临时字符串
            if i not in scanned_input_list:
                scan_output_list.append(i)

    # 将输入的字符串作为最后一个结果返回
    # 方便用户在程序无法推导出正确结果时快速编辑
    if input_text not in scan_output_list:
        scan_output_list.append(input_text)

    return scan_output_list

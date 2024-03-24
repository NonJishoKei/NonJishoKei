"""基于 v2 版本的索引创建 v3 版本的索引"""

import json
import os
import unicodedata
from typing import Dict

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


def convert_kata_to_hira(input_text: str) -> str:
    """Convert katakana to hiragana in the given text.
    将片假名转为平假名

    Args:
        input_text (str): A String containing the katakana.

    Returns:
        str: The text with katakana converted to hiragana.
    """
    output_text = ""
    for gana in input_text:
        # 关于取值范围，请阅读下面的链接
        # Read url for why the condition is 12448 and 13543
        # https://www.unicode.org/charts/PDF/U30A0.pdf
        gana_code = int(ord(gana))
        if 12448 < gana_code < 12543:
            hira = chr(gana_code - 96)
            output_text = output_text + hira
        else:
            output_text = output_text + gana
    return output_text


def convert_half_full_width(input_text: str) -> str:
    """Converts half-width characters to full-width characters.
        将半角字符转换为全角字符

    Args:
        input_text (str): A string containing half-width characters.

    Returns:
        str: A string containing full-width characters.
    """
    output_text = ""
    output_text = unicodedata.normalize("NFKC", input_text)
    return output_text


def scan_v2_index_files(input_file: str, index_dict: dict) -> dict:
    """convert v2 index file to v3 index rule.
        将v2 版本的索引文件转为 v3 版本

    Args:
        input_file (str): the file path of v2 index file.
        index_dict (dict): v3 index rule.

    Returns:
        index_dict (dict): v3 index rule.
    """
    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            nonjishokei = line.partition("\t")[0]
            # v3 版本会将《サボる》类似的非辞书形转为《さぼる》再进行进一步的处理
            nonjishokei = convert_kata_to_hira(nonjishokei)
            nonjishokei = convert_half_full_width(nonjishokei)
            jishokei = line.partition("\t")[2]
            index_dict.setdefault(nonjishokei, []).append(jishokei)
        return index_dict


def write_v3_index_file(output_file: str, index_dict: dict):
    """_summary_
        将 v3 版本的索引写入到 json 文件中

    Args:
        output_file (str):
        index_dict (dict): _description_
    """
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(index_dict, f, indent=None, ensure_ascii=False)


index_v2_file_list = ["adj.txt", "godann.txt", "itidann.txt", "sahenn.txt"]
INDEX_DICT: Dict[str, list[str]] = {}
for i in index_v2_file_list:
    scan_v2_index_files(os.path.join(CURRENT_PATH, i), INDEX_DICT)

write_v3_index_file(os.path.join(CURRENT_PATH, "index_v3.json"), INDEX_DICT)

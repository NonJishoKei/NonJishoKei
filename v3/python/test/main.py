"""convert a nonjishokei to a jishokei"""

import os
import json
from typing import Dict, List
from textwrap import dedent


def convert_v5(input_text: str, input_stem: str, input_last_letter: str) -> str:
    """convert a v5 verb conjugation to basic form.
        还原五段动词的活用变形，请注意，该函数只处理词尾假名来自五段动词活用的假名。

    Args:
        input_text (str): A String containing the conjugation.

    Returns:
        str: The text with conjugation converted to the basic form.
    """
    if input_text != input_stem + input_last_letter:
        raise ValueError(
            dedent(
                f"""input_text is {input_text},
            but input_stem is {input_stem}, input_last_letter is {input_last_letter},
            you may edited source in a wrong way,
            or you can report on you can report on github: 
            https://github.com/NoHeartPen/NonJishoKei"""
            )
        )

    v5_nonjishokei_last_letter = set(
        "えおかがきぎけげこごさしせそたちてとなにねのばびべぼまみめもらりれろわ"
    )
    if input_last_letter not in v5_nonjishokei_last_letter:
        if input_last_letter in "い":
            raise ValueError(
                dedent(
                    f"""{input_text} is v5, but you shouldn't use this function,
                        you can report on github: 
                        https://github.com/NoHeartPen/NonJishoKei"""
                )
            )
        else:
            raise ValueError(
                dedent(
                    f"""{input_text} is not v5,
                        you can report on github: 
                        https://github.com/NoHeartPen/NonJishoKei"""
                )
            )
    if input_last_letter in "がぎげご":
        jishokei = input_stem + "ぐ"
    elif input_last_letter == "と":
        jishokei = input_stem + "つ"
    elif input_last_letter == "ば":
        jishokei = input_stem + "ぶ"
    elif input_last_letter == "わ":
        jishokei = input_stem + "う"
    else:
        jishokei_dic = {}
        v5_jishokei_last_letter = set("うくすつぬぶむる")
        # TODO fix
        for i in v5_jishokei_last_letter:
            # 计算输入的假名与词尾原型假名之间的距离
            jishokei_dic[abs(ord(i) - ord(input_last_letter))] = i
        jishokei = input_text[0:-1] + jishokei_dic.get(
            min(jishokei_dic.keys()), "无法判断该五段假名的原型"
        )
    return jishokei


orthography_dict: Dict[str, list[str]] = dict()
CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(CURRENT_PATH, "index_v3.json"), "r", encoding="utf-8") as f:
    orthography_dict = json.loads(f.read())


def convert_orthography(input_text: str) -> list:
    """convert input text to the form of a word that appears as an entry in a dictionary,
        for example, convert【気づく】to【気付く】
        通过查询确认推导结果是否正确，同时消除假名书写造成的非辞書型，比如【気づく】和【気付く】

    Args:
        input_text (str): a form of a word that will not appear as an entry in a dictionary

    Returns:
        str: the form of a word that appears as an entry in a dictionary
    """
    if input_text in orthography_dict:
        return orthography_dict[input_text]
    else:
        return [input_text]


def convert_v5_need_once(input_stem: str, input_last_letter: str) -> str:
    """convert input text that can only come from a v5 verb
        还原只可能来自一个五段动词的动词活用的词尾假名

    Args:
        input_stem (str): A String containing the conjugation.
        input_last_letter (str): A String containing the conjugation.

    Raises:
        ValueError: the input text cannot be converted by this function,
        you can only use this function under the condition of v5_last_letter.

    Returns:
        str: The text with conjugation converted to the basic form.
    """
    if input_last_letter in "わえお":
        process_result = input_stem + "う"
    elif input_last_letter in "かきけこ":
        process_result = input_stem + "く"
    elif input_last_letter in "がぎげご":
        process_result = input_stem + "ぐ"
    elif input_last_letter in "しせ":
        process_result = input_stem + "す"
    elif input_last_letter in "にねの":
        process_result = input_stem + "ぬ"
    elif input_last_letter in "ばびべぼ":
        process_result = input_stem + "ぶ"
    elif input_last_letter in "めも":
        process_result = input_stem + "む"
    elif input_last_letter in "り":
        process_result = input_stem + "る"
    else:
        process_result = input_stem + input_last_letter
        raise ValueError(
            f"""{process_result} shouldn't converted by this function,
            you can report on github: https://github.com/NoHeartPen/NonJishoKei"""
        )
    return process_result


ProcessPath = os.getcwd()


def convert_conjugate(input_text: str) -> list:
    """convert a verb conjugation to basic form.
        还原动词的活用变形

    Args:
        input_text (str): A String containing the conjugation.

    Returns:
        list: The list with conjugation converted to the basic form.
    """
    # 请注意以下4条规则指的是不含动词未活用时原型词尾假名规律
    v1_last_letter = set("、よぬ")
    v5_last_letter = set("わえおがきぎげこごにねのばびべぼめもり")
    # 这些词尾假名只可能来自サ変动词活用
    sahen_last_letter = set("じぜ")
    adj_last_letter = set("くうす")
    v1_sahen_last_letter = set("ず")
    v5_sahen_last_letter = set("し")
    # 这些词尾假名只可能来自一段、五段的动词活用
    v1_v5_last_letter = set("たちてとなまられろ")
    # 这些词尾假名只可能来自一段、五段、サ変的动词活用
    v1_v5_sahen_last_letter = set("せ")
    # 这些词尾假名只可能来自形容词、五段的动词活用
    adj_v5_last_letter = set("かけみ")

    input_stem = input_text[0:-1]
    input_last_letter = input_text[-1]

    process_output_list = []

    # 本程序的 input_stem 概念对应的不是一段动词语法意义上的词干
    # 今日は、寿司を**食べ**に銀座に行いきます。
    process_text = input_text + "る"
    process_output_list.append(process_text)
    if input_last_letter in v1_last_letter:
        print("词尾假名是：" + input_last_letter + "有可能是一段动词")
        process_text = input_stem + "る"
        process_output_list.append(process_text)
    elif input_last_letter in v5_last_letter:
        print("词尾假名是：" + input_last_letter + "有可能是五段动词")
        process_text = convert_v5_need_once(input_stem, input_last_letter)
        process_output_list.append(process_text)
    elif input_last_letter in adj_last_letter:
        print("词尾假名是：" + input_last_letter + "有可能是形容词")
        process_text = input_stem + "い"
        process_output_list.append(process_text)
    elif input_last_letter in sahen_last_letter:
        print("词尾假名是：" + input_last_letter + "有可能是サ変")
        process_text = input_stem + "ずる"
        process_output_list.append(process_text)
        process_text = input_stem + "す"
        process_output_list.append(process_text)
        process_text = input_stem + "ず"
        process_output_list.append(process_text)
    elif input_last_letter in adj_v5_last_letter:
        print("词尾假名是：" + input_last_letter + "有可能是形容词，也有可能是五段动词")
        process_text = input_stem + "い"
        process_output_list.append(process_text)
        process_text = convert_v5(input_text, input_stem, input_last_letter)
        process_output_list.append(process_text)
    elif input_last_letter in v1_v5_last_letter:
        print(
            "词尾假名是：" + input_last_letter + "有可能是一段动词，也有可能是五段动词"
        )
        process_text = input_stem + "る"
        process_output_list.append(process_text)
        process_text = convert_v5(input_text, input_stem, input_last_letter)
        process_output_list.append(process_text)
    elif input_last_letter in v1_sahen_last_letter:
        print("词尾假名是：" + input_last_letter + "有可能是一段动词，也有可能是サ変")
        process_text = input_stem + "る"
        process_output_list.append(process_text)
        process_text = input_stem + "ずる"
        process_output_list.append(process_text)
    elif input_last_letter in v5_sahen_last_letter:
        print("词尾假名是：" + input_last_letter + "有可能是五段动词，也有可能是サ変")
        process_text = convert_v5_need_once(input_stem, input_last_letter)
        process_output_list.append(process_text)
        process_text = input_stem + "する"
        process_output_list.append(process_text)
    elif input_last_letter in v1_v5_sahen_last_letter:
        print(
            "词尾假名是："
            + input_last_letter
            + "有可能是一段动词，也有可能是五段动词，也有可能是サ変"
        )
        process_text = input_stem + "る"
        process_output_list.append(process_text)
        process_text = convert_v5(input_text, input_stem, input_last_letter)
        process_output_list.append(process_text)
        process_text = input_stem + "する"
        process_output_list.append(process_text)
    elif input_last_letter == "そ":
        print("词尾假名是：" + input_last_letter + "有可能是五段动词")
        process_text = input_stem + "い"
        process_output_list.append(process_text)
        process_text = input_stem + "す"
        process_output_list.append(process_text)
        process_text = input_stem + "する"
        process_output_list.append(process_text)
    elif input_last_letter == "っ":
        print("词尾假名是：" + input_last_letter + "有可能是五段动词")
        process_text = input_stem + "る"
        process_output_list.append(process_text)
        process_text = input_stem + "つ"
        process_output_list.append(process_text)
        process_text = input_stem + "う"
        process_output_list.append(process_text)
        if input_text == "行っ":
            process_output_list.append("行く")
            process_output_list.append(process_text)
    elif input_last_letter == "さ":
        print(
            "词尾假名是："
            + input_last_letter
            + "有可能是形容词，也有可能是五段动词，也有可能是一段动词"
        )
        process_text = input_stem + "い"
        process_output_list.append(process_text)
        process_text = input_stem + "す"
        process_output_list.append(process_text)
        process_text = input_stem + input_text[-1].replace(input_last_letter, "る")
        process_output_list.append(process_text)
        process_text = input_stem + "する"
        process_output_list.append(process_text)
    elif input_last_letter == "ん":
        print(
            "词尾假名是：" + input_last_letter + "有可能是一段动词，也有可能是五段动词"
        )
        process_text = input_stem + "む"
        process_output_list.append(process_text)
        process_text = input_stem + "ぶ"
        process_output_list.append(process_text)
        process_text = input_stem + "ぬ"
        process_output_list.append(process_text)
        process_text = input_stem + "る"
        process_output_list.append(process_text)
    elif input_last_letter == "い":
        print(
            "词尾假名是："
            + input_last_letter
            + "有可能是五段动词活用，也有可能是辞書形"
        )
        process_text = input_stem + "う"
        process_output_list.append(process_text)
        process_text = input_stem + "く"
        process_output_list.append(process_text)
        process_text = input_stem + "ぐ"
        process_output_list.append(process_text)
    elif input_last_letter == "ゃ":
        print("词尾假名是：" + input_last_letter + "有可能是一段动词")
        process_text = input_text[0:-2] + "る"
        process_output_list.append(process_text)
    else:
        # 不是动词活用出现的非辞書型
        print("词尾假名出现例外情况！" + input_text)
        process_output_list.append(input_text)

    # 将输入的字符串作为最后一个结果返回
    # 因为输入的字符串可能就是正确的辞書型
    if input_text not in process_output_list:
        process_output_list.append(input_text)

    # 删除其中的重复值，只保留第一次的结果
    output_list: List[str] = []
    for i in process_output_list:
        if i not in output_list:
            orthography_text = convert_orthography(i)
            if orthography_text is not None:
                output_list.extend(set(orthography_text))

    # 将输入的字符串作为最后一个结果返回
    # 方便用户在程序无法推导出正确结果时手动编辑
    if input_text not in output_list:
        output_list.append(input_text)

    return output_list

"""convert a nonjishokei to a jishokei"""

import os
import re
import time

START_TIME = time.perf_counter()


def convert_v5(input_text: str) -> str:
    """convert a v5 verb conjugation to basic form.
        还原五段动词的活用变形

    Args:
        input_text (str): A String containing the conjugation.

    Returns:
        str: The text with conjugation converted to the basic form.
    """
    v5_nonjishokei_last_letter = set(
        "えおかがきぎけげこごさしせそたちてとなにねのばびべぼまみめもらりれろわ"
    )
    if INPUT_LAST_LETTER not in v5_nonjishokei_last_letter:
        raise ValueError(
            f"""{input_text} is not v5,
            you can report on github: https://github.com/NoHeartPen/NonJishoKei"""
        )
    if INPUT_LAST_LETTER in "がぎげご":
        jishokei = input_text[0:-1] + "ぐ"
    elif INPUT_LAST_LETTER == "と":
        jishokei = input_text[0:-1] + "つ"
    elif INPUT_LAST_LETTER == "ば":
        jishokei = input_text[0:-1] + "ぶ"
    elif INPUT_LAST_LETTER == "わ":
        jishokei = input_text[0:-1] + "う"
    else:
        jishokei_dic = {}
        v5_jishokei_last_letter = set("うくすつぬぶむる")
        # TODO fix
        for i in v5_jishokei_last_letter:
            # 计算输入的假名与词尾原型假名之间的距离
            jishokei_dic[abs(ord(i) - ord(INPUT_LAST_LETTER))] = i
        jishokei = input_text[0:-1] + jishokei_dic.get(
            min(jishokei_dic.keys()), "无法判断该五段假名的原型"
        )
    return jishokei


index_set = set()
orthography_set = set()
orthography_dict = dict()
CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(CURRENT_PATH, "v3_index.txt"), "r", encoding="utf-8") as f:
    for item in f.readlines():
        item = item.replace("\n", "")
        if "\t" in item:
            orthography = item.split("\t")[0]
            orthography_set.add(orthography)
            index_set.add(orthography)
            orthography_dict[orthography] = item.split("\t")[1]
        else:
            index_set.add(item)


def convert_orthography(input_text: str) -> str:
    """convert input text to the form of a word that appears as an entry in a dictionary,
        for example, convert【気づく】to【気付く】
        通过查询消除假名书写造成的非辞書型，比如【気づく】和【気付く】

    Args:
        input_text (str): a form of a word that will not appear as an entry in a dictionary

    Returns:
        str: the form of a word that appears as an entry in a dictionary
    """
    if input_text in orthography_set:
        search_result = orthography_dict.get(input_text)
        return search_result
    else:
        return input_text


def search_index(input_text: str) -> str:
    """confirm whether the derivation results are correct by querying.
        通过查询确认推导结果是否正确

    Args:
        input_text (str): the results deduced by the program are not necessarily real words.

    Returns:
        str: a word that appears as an entry in a dictionary
    """
    # TODO 与 convert_orthography 函数合并
    if input_text in index_set:
        # TODO not use global
        global SearchResult
        SearchResult = input_text
        process_output_list.append(SearchResult)
        return SearchResult
    else:
        # TODO this looks like a bug
        SearchResult = INPUT_TEXT + "无该索引"
        return False


def convert_v5_need_once(input_text: str) -> str:
    """convert input text that can only come from a v5 verb
        还原只可能来自一个五段动词的动词活用的词尾假名

    Args:
        input_text (str): A String containing the conjugation.

    Raises:
        ValueError: the input text cannot be converted by this function,
        you can only use this function under the condition of v5_last_letter.

    Returns:
        str: The text with conjugation converted to the basic form.
    """
    if INPUT_LAST_LETTER in "わえお":
        process_result = input_text[0:-1] + "う"
    elif INPUT_LAST_LETTER in "かきけこ":
        process_result = input_text[0:-1] + "く"
    elif INPUT_LAST_LETTER in "がぎげご":
        process_result = input_text[0:-1] + "ぐ"
    elif INPUT_LAST_LETTER in "しせ":
        process_result = input_text[0:-1] + "す"
    elif INPUT_LAST_LETTER in "にねの":
        process_result = input_text[0:-1] + "ぬ"
    elif INPUT_LAST_LETTER in "ばびべぼ":
        process_result = input_text[0:-1] + "ぶ"
    elif INPUT_LAST_LETTER in "めも":
        process_result = input_text[0:-1] + "む"
    elif INPUT_LAST_LETTER in "り":
        process_result = input_text[0:-1] + "る"
    else:
        process_result = input_text
        raise ValueError(
            f"""{input_text} shouldn't converted by this function,
            you can report on github: https://github.com/NoHeartPen/NonJishoKei"""
        )
    return process_result


ProcessPath = os.getcwd()


def convert_conjugate(input_text: str) -> str:
    """convert a verb conjugation to basic form.
        还原动词的活用变形

    Args:
        input_text (str): A String containing the conjugation.

    Returns:
        str: The text with conjugation converted to the basic form.
    """
    # 请注意以下4条规则指的是不含动词未活用时原型词尾假名规律
    v1_last_letter = set("、ずよぬ")
    v5_last_letter = set("わえおがきぎげこごしにねのばびべぼめもり")
    adj_last_letter = set("くうす")
    # 这些词尾假名只可能来自一段、五段的动词活用
    v1_v5_last_letter = set("せたちてとなまられろ")
    # 这些词尾假名只可能来自形容词、五段的动词活用
    adj_v5_last_letter = set("かけみそ")

    # FIXME  不使用 global
    global process_output_list, INPUT_LAST_LETTER
    process_output_list = []  # 保留查询的结果
    search_index(input_text)  # 查看是否收录在词典中
    INPUT_LAST_LETTER = input_text.replace("\n", "")[-1]
    process_text = input_text + "る"  # 一段动词的连用形1
    search_index(process_text)
    if INPUT_LAST_LETTER in v1_last_letter:
        print("词尾假名是：" + INPUT_LAST_LETTER + "有可能是一段动词")
        process_text = input_text[0:-1] + "る"
        search_index(process_text)
    elif INPUT_LAST_LETTER in v5_last_letter:
        print("词尾假名是：" + INPUT_LAST_LETTER + "有可能是五段动词")
        process_text = convert_v5_need_once(input_text)
        search_index(process_text)
    elif INPUT_LAST_LETTER in adj_last_letter:
        print("词尾假名是：" + INPUT_LAST_LETTER + "有可能是形容词")
        process_text = input_text[0:-1] + "い"
        search_index(process_text)
    elif INPUT_LAST_LETTER in adj_v5_last_letter:
        print("词尾假名是：" + INPUT_LAST_LETTER + "有可能是形容词，也有可能是五段动词")
        process_text = input_text[0:-1] + "い"
        search_index(process_text)
        process_text = convert_v5(input_text)
        search_index(process_text)
    elif INPUT_LAST_LETTER in v1_v5_last_letter:
        print(
            "词尾假名是：" + INPUT_LAST_LETTER + "有可能是一段动词，也有可能是五段动词"
        )
        process_text = input_text[0:-1] + "る"
        search_index(process_text)
        process_text = convert_v5(input_text)
        search_index(process_text)
    elif INPUT_LAST_LETTER == "っ":
        print("词尾假名是：" + INPUT_LAST_LETTER + "有可能是五段动词")
        process_text = input_text[0:-1] + "る"
        search_index(process_text)
        process_text = input_text[0:-1] + "つ"
        search_index(process_text)
        process_text = input_text[0:-1] + "う"
        search_index(process_text)
        if input_text == "行っ":
            process_output_list.append("行く")
            search_index(process_text)
            process_output_list.append(input_text)
    elif INPUT_LAST_LETTER == "さ":
        print(
            "词尾假名是："
            + INPUT_LAST_LETTER
            + "有可能是形容词，也有可能是五段动词，也有可能是一段动词"
        )
        process_text = input_text[0:-1] + "い"
        search_index(process_text)
        process_text = input_text[0:-1] + "す"
        search_index(process_text)
        process_text = input_text[0:-1] + input_text[-1].replace(
            INPUT_LAST_LETTER, "る"
        )
        search_index(process_text)
    elif INPUT_LAST_LETTER == "ん":
        print(
            "词尾假名是：" + INPUT_LAST_LETTER + "有可能是一段动词，也有可能是五段动词"
        )
        process_text = input_text[0:-1] + "む"
        search_index(process_text)
        process_text = input_text[0:-1] + "ぶ"
        search_index(process_text)
        process_text = input_text[0:-1] + "ぬ"
        search_index(process_text)
        process_text = input_text[0:-1] + "る"
        search_index(process_text)
    elif INPUT_LAST_LETTER == "い":
        print(
            "词尾假名是："
            + INPUT_LAST_LETTER
            + "有可能是五段动词活用，也有可能是辞書形"
        )
        process_text = input_text[0:-1] + "う"
        search_index(process_text)
        process_text = input_text[0:-1] + "く"
        search_index(process_text)
        process_text = input_text[0:-1] + "ぐ"
        search_index(process_text)
    elif INPUT_LAST_LETTER == "ゃ":
        print("词尾假名是：" + INPUT_LAST_LETTER + "有可能是一段动词")
        process_text = input_text[0:-2] + "る"
        search_index(process_text)
    else:
        print("词尾假名出现例外情况！" + input_text)
        process_output_list.append(input_text)
    process_output_list.append(input_text)  # 任何情况下都返回复制的值，便于手动修改

    # 删除其中的重复值，只保留第一次的结果
    output_list = []
    for i in process_output_list:
        if i not in output_list:
            i = convert_orthography(i)
            output_list.append(i)

    # 注意，直接使用join遇到数字时会报错，但通过剪贴板获取的数字会被转为字符串
    output_text = "\n".join(output_list)
    return output_text


def del_word_ruby(input_text: str) -> str:
    """Removes ruby character from the input text.
        移除假名注音

    Args:
        input (str) : A string contains ruby.

    Returns:
        str: The text with converted ruby character.
    """
    # 通过检查注音符号前的字符串是否是汉字，判断是否是在为汉字注音
    # 汉字的 Unicode 编码范围请参考下面的链接
    # https://www.unicode.org/charts/
    reg = re.compile(
        r"""(?P<cjk_unified_ideographs>[\u4E00-\u9FFF])|
            (?P<extension_a>[\u3400-\u4DBF])|
            (?P<extension_b>[\u20000-\u2A6DF])|
            (?P<extension_c>[\u2A700-\u2B738])|
            (?P<extension_d>[\u2B740-\u2B81D])|
            (?P<extension_e>[\u2B820-\u2CEA1])|
            (?P<extension_f>[\u2CEB0-\u2EBE0])|
            (?P<extension_g>[\u30000-\u23134A])|
            (?P<extension_h>[\u31350-\u323AF])|
            (?P<extension_i>[\u2EBF0-\u2EE5F])(\(|（|《)(.*?)
        """
    )
    if reg.search(input_text) is None:
        return input_text

    reg = re.compile(r"(\(|（|《)[\u3040-\u309f]*?(\)|）|》)")
    replacement = r""
    output_text = re.sub(reg, replacement, input_text)
    return output_text


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


def convert_repe_single_sign(input_text: str) -> str:
    """Converts a repeated single sign (々 or 〻 or ゝ or ヽ) in the given text.
        移除单字符重复符号々、〻、ゝ、ヽ

    Args:
        input (str): A string containing the repeated single sign.

    Returns:
        str: The text with converted repeated single sign.
    """
    reg = r"^(.*?)(々|〻|ゝ|ヽ)(.*?)$"
    match = re.match(reg, input_text)
    if not match:
        return input_text

    i = 0
    output_text = ""
    while i < len(input_text):
        if i != 0:
            if input_text[i] in "々〻ゝヽ":
                output_text += input_text[i - 1]
            else:
                output_text += input_text[i]
        else:
            # 当"々"等符号位于第一个位置时，不做任何处理，例：々段
            output_text += input_text[i]
        i += 1
    return output_text


def convert_repe_single_daku_sign(input_text: str) -> str:
    """Converts a repeated single daku sign (ヾ or ゞ) in the given text.
        移除单字符浊音符号ヾ、ゞ

    Args:
        input_text (str): A string containing the repeated single daku sign.

    Returns:
        str: The text with converted repeated single daku sign.
    """
    reg = r"^(.*?)(\w{1})(ヾ|ゞ)(.*?)$"
    match = re.match(reg, input_text)
    if not match:
        return input_text

    # 匹配单字符浊音符前的字符串（不包括单字符浊音符前的第一个字符串）
    pre_text = match.group(1)
    # 计算单字符浊音符前的第一个字符串
    char = match.group(2)
    new_char = chr(ord(char) + 1)
    # 匹配单字符浊音后的所有字符串
    post_text = match.group(4)

    output_text = pre_text + char + new_char + post_text
    return output_text


def convert_repe_double_sign(input_text: str) -> str:
    """Converts repeated double sign in the given text.
        移除多字符重复符号〳〵、／＼、〱

    Args:
        input_text (str): The text containing the repeated double sign.

    Returns:
        str: The text with converted repeated double sign.
    """
    match = re.match(r"^(.*?)(〳〵|／＼|〱)$", input_text)

    if not match:
        return input_text

    # 匹配多字符重复符号前的字符串
    pre_input_text = match.group(1)

    output_text = pre_input_text + pre_input_text
    return output_text


def convert_repe_double_daku_sign(input_text: str) -> str:
    """Convert a repeated double daku sign ( 〴〵, ／″＼) in the given text.
        移除多字符浊音符号 〴〵、／″＼

    Args:
        input (str): A String containing the repeated double daku sign.

    Returns:
        str: The text with converted repeated double daku sign.
    """
    match = re.match(r"^(.*?)(〴〵|／″＼)(.*?)$", input_text)

    if not match:
        return input_text

    # 匹配多字符浊音符号前的字符串
    pre_input_text = match.group(1)
    # 匹配多字符浊音符号后的字符串
    post_input_text = match.group(3)

    if re.search(r"[^\u3040-\u30ff]", pre_input_text) is not None:
        # 如果多字符浊音符号前的字符串中不止汉字
        # 比如像「代わる〴〵」这样，同时含有汉字和假名
        # 那么拼接多字符浊音符号前的部分然后输出拼接后的字符串，例：「代わる代わる」
        output_text = pre_input_text + pre_input_text + post_input_text
    elif re.search(r"([\u3040-\u30ff]{1})(.*?)", pre_input_text) is not None:
        # 提取多字符浊音符号前的字符串的第一个假名并计算出对应的浊音假名
        # 拼接后输出拼接后的字符串
        daku_character = chr(int(ord(pre_input_text[0])) + 1)
        new_pre_input_text = daku_character + pre_input_text[1:]
        output_text = pre_input_text + new_pre_input_text + post_input_text
    else:
        print(f"input_text is: {input_text}")
        return input_text
    return output_text


def del_ocr_error(input_text: str) -> str:
    """Removes OCR errors from the input text.
        移除 OCR 易识别错误的字符

    Args:
        input (str): a string containing OCR-detected text with spaces and newlines.

    Returns:
        str: a processed string with spaces and newlines removed.
    """
    input_text = input_text.replace(" ", "")
    output_text = input_text.replace("\n", "")
    output_text = input_text.replace("\r\n", "")
    return output_text


def preprocess(input_text: str) -> str:
    """Preprocess the input text.
        预处理输入文本

    Args:
        input_text (str): The input text.

    Returns:
        str: The processed text.
    """
    input_text = del_ocr_error(input_text)
    if "(" in input_text:
        input_text = del_word_ruby(input_text)
    # 转换片假名书写的单词
    if re.search(r"^[\u30a0-\u30ff]*?$", INPUT_TEXT) is not None:
        input_text = convert_kata_to_hira(input_text)
    if re.search(r"(\w{1})(々|〻|ゝ|ヽ)", input_text) is not None:
        input_text = convert_repe_single_sign(input_text)
    if re.search(r"^(.*?)(\w{1})(ヾ|ゞ)(.*?)$", input_text) is not None:
        input_text = convert_repe_single_daku_sign(input_text)
    if re.search(r"^(\w{2})(〳〵|／＼)(.*?)$", input_text) is not None:
        input_text = convert_repe_double_sign(input_text)
    if re.search(r"^(.*?)(〴〵|／″＼)(.*?)$", input_text) is not None:
        input_text = convert_repe_double_daku_sign(input_text)
    return input_text


INPUT_TEXT = "歩く"


OUTPUT_TEXT = convert_conjugate(INPUT_TEXT)
print(OUTPUT_TEXT)
END_TIME = time.perf_counter()
print(f"耗时:{round((END_TIME - START_TIME) * 1000, 3)}毫秒")

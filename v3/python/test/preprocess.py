"""Preprocess the input text."""

import re


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

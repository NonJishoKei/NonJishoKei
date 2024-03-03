import os
import re
import time

"""
返回所有查询结果
"""
START_TIME = time.perf_counter()


def GetGodannJiSho(InputText):  # 下表还可以再修改
    GodanLastLetter = set(
        "えおかがきぎけげこごさしせそたちてとなにねのばびべぼまみめもらりれろわ"
    )
    if INPUT_LAST_LETTER not in GodanLastLetter:
        print("非五段动词变形！")
    if INPUT_LAST_LETTER in "がぎげご":
        GodannJiSho = InputText[0:-1] + "ぐ"
    elif INPUT_LAST_LETTER == "と":
        GodannJiSho = InputText[0:-1] + "つ"
    elif INPUT_LAST_LETTER == "ば":
        GodannJiSho = InputText[0:-1] + "ぶ"
    elif INPUT_LAST_LETTER == "わ":
        GodannJiSho = InputText[0:-1] + "う"
    else:
        Jisho_Dic = {}
        GodanJishoLastLetter = set("うくすつぬぶむる")
        for i in GodanJishoLastLetter:
            Jisho_Dic[abs(ord(i) - ord(INPUT_LAST_LETTER))] = (
                i  # 计算输入的假名与词尾原型假名之间的距离
            )
        GodannJiSho = InputText[0:-1] + Jisho_Dic.get(
            min(Jisho_Dic.keys()), "无法判断该五段假名的原型"
        )
    return GodannJiSho


IndexTextSet = set()
OrthographySet = set()
OrthographyDict = dict()
CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(CURRENT_PATH, "v3_index.txt"), "r", encoding="utf-8") as f:
    for item in f.readlines():
        item = item.replace("\n", "")
        if "\t" in item:
            Orthography = item.split("\t")[0]
            OrthographySet.add(Orthography)
            IndexTextSet.add(Orthography)
            OrthographyDict[Orthography] = item.split("\t")[1]
        else:
            IndexTextSet.add(item)


def DisambiguateCompound(SearchText):
    if SearchText in OrthographySet:
        SearchResult = OrthographyDict.get(SearchText)
        print(SearchResult)
        return SearchResult
    else:
        return SearchText


def SearchInIndex(SearchText):
    print("尝试在索引中查找" + SearchText)
    if SearchText in IndexTextSet:
        global SearchResult
        SearchResult = SearchText
        process_output_list.append(SearchResult)
        return SearchResult
    else:
        SearchResult = INPUT_TEXT + "无该索引"
        return False


def ProcessNeedOnceProcess_Godan(
    InputText,
):  # 请确保是五段动词活用可能出现的词尾再调用该函数
    if INPUT_LAST_LETTER in "わえお":
        ProcessResult = InputText[0:-1] + "う"
    elif INPUT_LAST_LETTER in "かきけこ":
        ProcessResult = InputText[0:-1] + "く"
    elif INPUT_LAST_LETTER in "がぎげご":
        ProcessResult = InputText[0:-1] + "ぐ"
    elif INPUT_LAST_LETTER in "しせ":
        ProcessResult = InputText[0:-1] + "す"
    elif INPUT_LAST_LETTER in "にねの":
        ProcessResult = InputText[0:-1] + "ぬ"
    elif INPUT_LAST_LETTER in "ばびべぼ":
        ProcessResult = InputText[0:-1] + "ぶ"
    elif INPUT_LAST_LETTER in "めも":
        ProcessResult = InputText[0:-1] + "む"
    elif INPUT_LAST_LETTER in "り":
        ProcessResult = InputText[0:-1] + "る"
    else:
        # 抛出异常，不应该调用这个方法
        ProcessResult = InputText
        print(ProcessResult + "ProcessNeedOnceProcess_Godan异常")
    return ProcessResult


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
    SearchInIndex(input_text)  # 查看是否收录在词典中
    INPUT_LAST_LETTER = input_text.replace("\n", "")[-1]
    process_text = input_text + "る"  # 一段动词的连用形1
    SearchInIndex(process_text)
    if INPUT_LAST_LETTER in v1_last_letter:
        print("词尾假名是：" + INPUT_LAST_LETTER + "有可能是一段动词")
        process_text = input_text[0:-1] + "る"
        SearchInIndex(process_text)
    elif INPUT_LAST_LETTER in v5_last_letter:
        print("词尾假名是：" + INPUT_LAST_LETTER + "有可能是五段动词")
        process_text = ProcessNeedOnceProcess_Godan(input_text)
        SearchInIndex(process_text)
    elif INPUT_LAST_LETTER in adj_last_letter:
        print("词尾假名是：" + INPUT_LAST_LETTER + "有可能是形容词")
        process_text = input_text[0:-1] + "い"
        SearchInIndex(process_text)
    elif INPUT_LAST_LETTER in adj_v5_last_letter:
        print("词尾假名是：" + INPUT_LAST_LETTER + "有可能是形容词，也有可能是五段动词")
        process_text = input_text[0:-1] + "い"
        SearchInIndex(process_text)
        process_text = GetGodannJiSho(input_text)
        SearchInIndex(process_text)
    elif INPUT_LAST_LETTER in v1_v5_last_letter:
        print(
            "词尾假名是：" + INPUT_LAST_LETTER + "有可能是一段动词，也有可能是五段动词"
        )
        process_text = input_text[0:-1] + "る"
        SearchInIndex(process_text)
        process_text = GetGodannJiSho(input_text)
        SearchInIndex(process_text)
    elif INPUT_LAST_LETTER == "っ":
        print("词尾假名是：" + INPUT_LAST_LETTER + "有可能是五段动词")
        process_text = input_text[0:-1] + "る"
        SearchInIndex(process_text)
        process_text = input_text[0:-1] + "つ"
        SearchInIndex(process_text)
        process_text = input_text[0:-1] + "う"
        SearchInIndex(process_text)
        if input_text == "行っ":
            process_output_list.append("行く")
            SearchInIndex(process_text)
            process_output_list.append(input_text)
    elif INPUT_LAST_LETTER == "さ":
        print(
            "词尾假名是："
            + INPUT_LAST_LETTER
            + "有可能是形容词，也有可能是五段动词，也有可能是一段动词"
        )
        process_text = input_text[0:-1] + "い"
        SearchInIndex(process_text)
        process_text = input_text[0:-1] + "す"
        SearchInIndex(process_text)
        process_text = input_text[0:-1] + input_text[-1].replace(
            INPUT_LAST_LETTER, "る"
        )
        SearchInIndex(process_text)
    elif INPUT_LAST_LETTER == "ん":
        print(
            "词尾假名是：" + INPUT_LAST_LETTER + "有可能是一段动词，也有可能是五段动词"
        )
        process_text = input_text[0:-1] + "む"
        SearchInIndex(process_text)
        process_text = input_text[0:-1] + "ぶ"
        SearchInIndex(process_text)
        process_text = input_text[0:-1] + "ぬ"
        SearchInIndex(process_text)
        process_text = input_text[0:-1] + "る"
        SearchInIndex(process_text)
    elif INPUT_LAST_LETTER == "い":
        print(
            "词尾假名是："
            + INPUT_LAST_LETTER
            + "有可能是五段动词活用，也有可能是辞書形"
        )
        process_text = input_text[0:-1] + "う"
        SearchInIndex(process_text)
        process_text = input_text[0:-1] + "く"
        SearchInIndex(process_text)
        process_text = input_text[0:-1] + "ぐ"
        SearchInIndex(process_text)
    elif INPUT_LAST_LETTER == "ゃ":
        print("词尾假名是：" + INPUT_LAST_LETTER + "有可能是一段动词")
        process_text = input_text[0:-2] + "る"
        SearchInIndex(process_text)
    else:
        print("词尾假名出现例外情况！" + input_text)
        process_output_list.append(input_text)
    process_output_list.append(input_text)  # 任何情况下都返回复制的值，便于手动修改

    # 删除其中的重复值，只保留第一次的结果
    output_list = []
    for i in process_output_list:
        if i not in output_list:
            i = DisambiguateCompound(i)
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


INPUT_TEXT = "歩く"

# 预处理
INPUT_TEXT = del_ocr_error(INPUT_TEXT)
if "(" in INPUT_TEXT:  # 删除Word等使用的注音假名，注意是半角()
    INPUT_TEXT = del_word_ruby(INPUT_TEXT)
if re.search(r"^[\u30a0-\u30ff]*?$", INPUT_TEXT) is not None:  # 转换片假名书写的单词
    INPUT_TEXT = convert_kata_to_hira(INPUT_TEXT)
if re.search(r"(\w{1})(々|〻|ゝ|ヽ)", INPUT_TEXT) is not None:
    INPUT_TEXT = convert_repe_single_sign(INPUT_TEXT)
if re.search(r"^(.*?)(\w{1})(ヾ|ゞ)(.*?)$", INPUT_TEXT) is not None:
    INPUT_TEXT = convert_repe_single_daku_sign(INPUT_TEXT)
if re.search(r"^(\w{2})(〳〵|／＼)(.*?)$", INPUT_TEXT) is not None:
    INPUT_TEXT = convert_repe_double_sign(INPUT_TEXT)
if re.search(r"^(.*?)(〴〵|／″＼)(.*?)$", INPUT_TEXT) is not None:
    INPUT_TEXT = convert_repe_double_daku_sign(INPUT_TEXT)


OUTPUT_TEXT = convert_conjugate(INPUT_TEXT)
print(OUTPUT_TEXT)
END_TIME = time.perf_counter()
print(f"耗时:{round((END_TIME - START_TIME) * 1000, 3)}毫秒")

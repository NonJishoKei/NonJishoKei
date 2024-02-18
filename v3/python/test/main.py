import os
import re
import time

"""
返回所有查询结果
"""
StartTime = time.perf_counter()


def GetGodannJiSho(InputText):  # 下表还可以再修改
    GodanLastLetter = set(
        "えおかがきぎけげこごさしせそたちてとなにねのばびべぼまみめもらりれろわ"
    )
    if LastLetter not in GodanLastLetter:
        print("非五段动词变形！")
    if LastLetter in "がぎげご":
        GodannJiSho = InputText[0:-1] + "ぐ"
    elif LastLetter == "と":
        GodannJiSho = InputText[0:-1] + "つ"
    elif LastLetter == "ば":
        GodannJiSho = InputText[0:-1] + "ぶ"
    elif LastLetter == "わ":
        GodannJiSho = InputText[0:-1] + "う"
    else:
        Jisho_Dic = {}
        GodanJishoLastLetter = set("うくすつぬぶむる")
        for i in GodanJishoLastLetter:
            Jisho_Dic[abs(ord(i) - ord(LastLetter))] = (
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
        Output.append(SearchResult)
        return SearchResult
    else:
        SearchResult = InputText + "无该索引"
        return False


def ProcessNeedOnceProcess_Godan(
    InputText,
):  # 请确保是五段动词活用可能出现的词尾再调用该函数
    if LastLetter in "わえお":
        ProcessResult = InputText[0:-1] + "う"
    elif LastLetter in "かきけこ":
        ProcessResult = InputText[0:-1] + "く"
    elif LastLetter in "がぎげご":
        ProcessResult = InputText[0:-1] + "ぐ"
    elif LastLetter in "しせ":
        ProcessResult = InputText[0:-1] + "す"
    elif LastLetter in "にねの":
        ProcessResult = InputText[0:-1] + "ぬ"
    elif LastLetter in "ばびべぼ":
        ProcessResult = InputText[0:-1] + "ぶ"
    elif LastLetter in "めも":
        ProcessResult = InputText[0:-1] + "む"
    elif LastLetter in "り":
        ProcessResult = InputText[0:-1] + "る"
    else:
        ProcessResult = InputText
        print(ProcessResult + "ProcessNeedOnceProcess_Godan异常")
    return ProcessResult


NeedOnceProcess_itidann = set("、ずよぬ")
NeedOnceProcess_godann = set("わえおがきぎげこごしにねのばびべぼめもり")
NeedOnceProcess_adj = set("くうす")


NeedTwiceProcess_adj_godann = set("かけみそ")  # 这几个词尾来源：形容词/五段
NeedTwiceProcess_itidann_godann = set("せたちてとなまられろ")  # 这些只可能来自一段/五段


ProcessPath = os.getcwd()


def ConvertConjugate(InputText):
    global Output, LastLetter
    Output = []  # 保留查询的结果
    SearchInIndex(InputText)  # 查看是否收录在词典中
    LastLetter = InputText.replace("\n", "")[-1]
    ProcessText = InputText + "る"  # 一段动词的连用形1
    SearchInIndex(ProcessText)
    if LastLetter in NeedOnceProcess_itidann:
        print("词尾假名是：" + LastLetter + "有可能是一段动词")
        ProcessText = InputText[0:-1] + "る"
        SearchInIndex(ProcessText)
    elif LastLetter in NeedOnceProcess_godann:
        print("词尾假名是：" + LastLetter + "有可能是五段动词")
        ProcessText = ProcessNeedOnceProcess_Godan(InputText)
        SearchInIndex(ProcessText)
    elif LastLetter in NeedOnceProcess_adj:
        print("词尾假名是：" + LastLetter + "有可能是形容词")
        ProcessText = InputText[0:-1] + "い"
        SearchInIndex(ProcessText)
    elif LastLetter in NeedTwiceProcess_adj_godann:
        print("词尾假名是：" + LastLetter + "有可能是形容词，也有可能是五段动词")
        ProcessText = InputText[0:-1] + "い"
        SearchInIndex(ProcessText)
        ProcessText = GetGodannJiSho(InputText)
        SearchInIndex(ProcessText)
    elif LastLetter in NeedTwiceProcess_itidann_godann:
        print("词尾假名是：" + LastLetter + "有可能是一段动词，也有可能是五段动词")
        ProcessText = InputText[0:-1] + "る"
        SearchInIndex(ProcessText)
        ProcessText = GetGodannJiSho(InputText)
        SearchInIndex(ProcessText)
    elif LastLetter == "っ":
        print("词尾假名是：" + LastLetter + "有可能是五段动词")
        ProcessText = InputText[0:-1] + "る"
        SearchInIndex(ProcessText)
        ProcessText = InputText[0:-1] + "つ"
        SearchInIndex(ProcessText)
        ProcessText = InputText[0:-1] + "う"
        SearchInIndex(ProcessText)
        if InputText == "行っ":
            Output.append("行く")
            SearchInIndex(ProcessText)
            Output.append(InputText)
    elif LastLetter == "さ":
        print(
            "词尾假名是："
            + LastLetter
            + "有可能是形容词，也有可能是五段动词，也有可能是一段动词"
        )
        ProcessText = InputText[0:-1] + "い"
        SearchInIndex(ProcessText)
        ProcessText = InputText[0:-1] + "す"
        SearchInIndex(ProcessText)
        ProcessText = InputText[0:-1] + InputText[-1].replace(LastLetter, "る")
        SearchInIndex(ProcessText)
    elif LastLetter == "ん":
        print("词尾假名是：" + LastLetter + "有可能是一段动词，也有可能是五段动词")
        ProcessText = InputText[0:-1] + "む"
        SearchInIndex(ProcessText)
        ProcessText = InputText[0:-1] + "ぶ"
        SearchInIndex(ProcessText)
        ProcessText = InputText[0:-1] + "ぬ"
        SearchInIndex(ProcessText)
        ProcessText = InputText[0:-1] + "る"
        SearchInIndex(ProcessText)
    elif LastLetter == "い":
        print("词尾假名是：" + LastLetter + "有可能是五段动词活用，也有可能是辞書形")
        ProcessText = InputText[0:-1] + "う"
        SearchInIndex(ProcessText)
        ProcessText = InputText[0:-1] + "く"
        SearchInIndex(ProcessText)
        ProcessText = InputText[0:-1] + "ぐ"
        SearchInIndex(ProcessText)
    elif LastLetter == "ゃ":
        print("词尾假名是：" + LastLetter + "有可能是一段动词")
        ProcessText = InputText[0:-2] + "る"
        SearchInIndex(ProcessText)
    else:
        print("词尾假名出现例外情况！" + InputText)
        Output.append(InputText)
    Output.append(InputText)  # 任何情况下都返回复制的值，便于手动修改

    # 删除其中的重复值，只保留第一次的结果
    ProcessOutput = []
    for item in Output:
        if item not in ProcessOutput:
            item = DisambiguateCompound(item)
            ProcessOutput.append(item)

    # 注意，直接使用join遇到数字时会报错，但通过剪贴板获取的数字会被转为字符串
    CLipboradTexts = "\n".join(ProcessOutput)
    return CLipboradTexts


def DelWordRuby(ProcessText):
    reg = r"\([\u3040-\u309f]*?\)"  # 参考Unicode码值，只匹配平假名
    replacement = r""
    OutputText = re.sub(reg, replacement, ProcessText)
    return OutputText


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


InputText = "歩く"

# 预处理
InputText = del_ocr_error(InputText)
if "(" in InputText:  # 删除Word等使用的注音假名，注意是半角()
    InputText = DelWordRuby(InputText)
if re.search(r"^[\u30a0-\u30ff]*?$", InputText) != None:  # 转换片假名书写的单词
    InputText = convert_kata_to_hira(InputText)
if re.search(r"(\w{1})(々|〻|ゝ|ヽ)", InputText) != None:
    InputText = convert_repe_single_sign(InputText)
if re.search(r"^(.*?)(\w{1})(ヾ|ゞ)(.*?)$", InputText) != None:
    InputText = convert_repe_single_daku_sign(InputText)
if re.search(r"^(\w{2})(〳〵|／＼)(.*?)$", InputText) != None:
    InputText = convert_repe_double_sign(InputText)
if re.search(r"^(.*?)(〴〵|／″＼)(.*?)$", InputText) != None:
    InputText = convert_repe_double_daku_sign(InputText)


OutputText = ConvertConjugate(InputText)
print(OutputText)
EndTime = time.perf_counter()
print("耗时:%s毫秒" % (round((EndTime - StartTime) * 1000, 3)))

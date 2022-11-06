import os
import re
import time

'''
返回所有查询结果
'''
StartTime = time.perf_counter()


def GetGodannJiSho(InputText):  # 下表还可以再修改
    GodanLastLetter = set('えおかがきぎけげこごさしせそたちてとなにねのばびべぼまみめもらりれろわ')
    if LastLetter not in GodanLastLetter:
        print("非五段动词变形！")
    if LastLetter in 'がぎげご':
        GodannJiSho = InputText[0:-1] + "ぐ"
    elif LastLetter == 'と':
        GodannJiSho = InputText[0:-1]+"つ"
    elif LastLetter == 'ば':
        GodannJiSho = InputText[0:-1]+"ぶ"
    elif LastLetter == 'わ':
        GodannJiSho = InputText[0:-1] + "う"
    else:
        Jisho_Dic = {}
        GodanJishoLastLetter = set('うくすつぬぶむる')
        for i in GodanJishoLastLetter:
            Jisho_Dic[abs(ord(i)-ord(LastLetter))] = i  # 计算输入的假名与词尾原型假名之间的距离
        GodannJiSho = InputText[0:-1] + \
            Jisho_Dic.get(min(Jisho_Dic.keys()), '无法判断该五段假名的原型')
    return GodannJiSho


IndexTextSet = set()
with open('v3_index.txt', 'r', encoding='utf-8') as f:
    IndexText = f.readlines()
    for i in IndexText:
        IndexTextSet.add(i.replace('\n', ''))


def SearchInIndex(SearchText):
    print('尝试在索引中查找'+SearchText)
    if SearchText in IndexTextSet:
        global SearchResult
        SearchResult = SearchText
        Output.append(SearchResult)
        return SearchResult
    else:
        SearchResult = InputText+'无该索引'
        return False


def ProcessNeedOnceProcess_Godan(InputText):  # 请确保是五段动词活用可能出现的词尾再调用该函数
    if LastLetter in 'わえお':
        ProcessResult = InputText[0:-1]+'う'
    elif LastLetter in 'かきけこ':
        ProcessResult = InputText[0:-1]+'く'
    elif LastLetter in 'がぎげご':
        ProcessResult = InputText[0:-1]+'ぐ'
    elif LastLetter in 'しせ':
        ProcessResult = InputText[0:-1]+'す'
    elif LastLetter in 'にねの':
        ProcessResult = InputText[0:-1]+'ぬ'
    elif LastLetter in 'ばびべぼ':
        ProcessResult = InputText[0:-1]+'ぶ'
    elif LastLetter in 'めも':
        ProcessResult = InputText[0:-1] + 'む'
    elif LastLetter in 'り':
        ProcessResult = InputText[0:-1] + 'る'
    else:
        ProcessResult = InputText
        print(ProcessResult+"ProcessNeedOnceProcess_Godan异常")
    return ProcessResult


NeedOnceProcess_itidann = set('、ずよぬ')
NeedOnceProcess_godann = set('わえおがきぎげこごしせにねのばびべぼめもり')
NeedOnceProcess_adj = set('くうす')


NeedTwiceProcess_adj_godann = set('かけみそ')  # 这几个词尾来源：形容词/五段
NeedTwiceProcess_itidann_godann = set('たちてとなまられろ')  # 这些只可能来自一段/五段


ProcessPath = os.getcwd()


def ConvertConjugate(InputText):
    global Output, LastLetter
    Output = []  # 保留查询的结果
    SearchInIndex(InputText)  # 查看是否收录在词典中
    LastLetter = InputText.replace('\n', '')[-1]
    ProcessText = InputText+'る'  # 一段动词的连用形1
    SearchInIndex(ProcessText)
    if LastLetter in NeedOnceProcess_itidann:
        print('词尾假名是：'+LastLetter+'有可能是一段动词')
        ProcessText = InputText[0:-1]+'る'
        SearchInIndex(ProcessText)
    elif LastLetter in NeedOnceProcess_godann:
        print('词尾假名是：'+LastLetter+'有可能是五段动词')
        ProcessText = ProcessNeedOnceProcess_Godan(InputText)
        SearchInIndex(ProcessText)
    elif LastLetter in NeedOnceProcess_adj:
        print('词尾假名是：'+LastLetter+'有可能是形容词')
        ProcessText = InputText[0:-1]+'い'
        SearchInIndex(ProcessText)
    elif LastLetter in NeedTwiceProcess_adj_godann:
        print('词尾假名是：'+LastLetter+'有可能是形容词，也有可能是五段动词')
        ProcessText = InputText[0:-1] + 'い'
        SearchInIndex(ProcessText)
        ProcessText = GetGodannJiSho(InputText)
        SearchInIndex(ProcessText)
    elif LastLetter in NeedTwiceProcess_itidann_godann:
        print('词尾假名是：'+LastLetter+'有可能是一段动词，也有可能是五段动词')
        ProcessText = InputText[0:-1] + 'る'
        SearchInIndex(ProcessText)
        ProcessText = GetGodannJiSho(InputText)
        SearchInIndex(ProcessText)
    elif LastLetter == 'っ':
        print('词尾假名是：'+LastLetter+'有可能是五段动词')
        ProcessText = InputText[0:-1] + 'る'
        SearchInIndex(ProcessText)
        ProcessText = InputText[0:-1]+'つ'
        SearchInIndex(ProcessText)
        ProcessText = InputText[0:-1] + 'う'
        SearchInIndex(ProcessText)
        if InputText == '行っ':
            Output.append('行く')
            SearchInIndex(ProcessText)
            Output.append(InputText)
    elif LastLetter == 'さ':
        print('词尾假名是：'+LastLetter+'有可能是形容词，也有可能是五段动词')
        ProcessText = InputText[0:-1]+'い'
        SearchInIndex(ProcessText)

        ProcessText = InputText[0:-1]+'す'
        SearchInIndex(ProcessText)

        ProcessText = InputText[0:-1] + \
            InputText[-1].replace(LastLetter, 'る')
        SearchInIndex(ProcessText)
    elif LastLetter == 'ん':
        print('词尾假名是：'+LastLetter+'有可能是形容词，也有可能是五段动词')
        ProcessText = InputText[0:-1]+'む'
        SearchInIndex(ProcessText)
        ProcessText = InputText[0:-1]+'ぶ'
        SearchInIndex(ProcessText)
        ProcessText = InputText[0:-1] + 'ぬ'
        SearchInIndex(ProcessText)
        ProcessText = InputText[0:-1] + 'る'
        SearchInIndex(ProcessText)
    elif LastLetter == "い":
        print('词尾假名是：'+LastLetter+'有可能是五段动词')
        ProcessText = InputText[0:-1] + 'う'
        SearchInIndex(ProcessText)
        ProcessText = InputText[0:-1] + 'く'
        SearchInIndex(ProcessText)
        ProcessText = InputText[0:-1] + 'ぐ'
        SearchInIndex(ProcessText)
    elif LastLetter == 'ゃ':
        print('词尾假名是：'+LastLetter+'有可能是一段动词')
        ProcessText = InputText[0:-2] + 'る'
        SearchInIndex(ProcessText)
    else:
        print("词尾假名出现例外情况！"+InputText)
        Output.append(InputText)
    Output.append(InputText)  # 任何情况下都返回复制的值，便于手动修改

    # 删除其中的重复值，只保留第一次的结果
    ProcessOutput = []
    for item in Output:
        if item not in ProcessOutput:
            ProcessOutput.append(item)

    # 注意，直接使用join遇到数字时会报错，但通过剪贴板获取的数字会被转为字符串
    CLipboradTexts = '\n'.join(ProcessOutput)
    return CLipboradTexts


def DelWordRuby(ProcessText):
    reg = r'\([\u3040-\u309f]*?\)'  # 参考Unicode码值，只匹配平假名
    replacement = r''
    OutputText = re.sub(reg, replacement, ProcessText)
    return OutputText


def ConverHina2kata(InputText):
    ProcessTexts = []
    for gana in InputText:
        if 12448 < int(ord(gana)) < 12543:  # 匹配片假名
            hira = chr(int(ord(gana) - 96))
            ProcessTexts.append(hira)
    OutputText = ''.join(ProcessTexts)
    return OutputText


def ConverRepeSingleSign(InputText):
    # 这些符号只代表一个假名或者汉字，注意ゝヽ不一定出现在单词的结尾部分，例如：やがて再び唇をわなゝかした
    reg = r'(\w{1})(々|〻|ゝ|ヽ)'
    OutputText = re.sub(reg, r'\1\1', InputText)
    return OutputText


def ConverRepeSingleDakuSign(InputText):
    reg = r'^(.*?)(\w{1})(ヾ|ゞ)(.*?)$'
    ProcessText = re.match(reg, InputText)
    OutputText = ProcessText.group(
        1)+ProcessText.group(2)+chr(int(ord(ProcessText.group(2)))+1)+ProcessText.group(4)
    return OutputText


def ConverRepeDoubleSign(InputText):
    reg = r'^(\w{2})(〳〵|／＼)(.*?)$'  # 这些符号代表2个假名或者汉字
    OutputText = re.sub(reg, r'\1\1\3', InputText)
    return OutputText


def ConverRepeDoubleDakuSign(InputText):
    ProcessText = re.match(r'^(.*?)(〴〵|／″＼)(.*?)$', InputText)
    if re.search(r'[^\u3040-\u30ff]', ProcessText.group(1)) != None:  # 注意：代わる〴〵
        print('now')
        reg = r'^(.*?)(〴〵|／″＼)(.*?)$'
        OutputText = re.sub(reg, r'\1\1\3', InputText)
    else:
        reg = r'^(\w{1})(\w{1})(〴〵|／″＼)$'  # 第一个分组是需要浊化的假名，第二个分组不需要处理
        sub = r'\1\2'
        ProcessText = re.match(reg, InputText)
        OutputText = ProcessText.group(
            1)+ProcessText.group(2)+chr(int(ord(ProcessText.group(2)))+1)
        ProcessText = re.sub(reg, sub, InputText)
        OutputText = ProcessText + \
            chr(int(ord(ProcessText[0]))+1)+ProcessText[1]
    return OutputText


def DelOCRError(InputText):
    InputText = InputText.replace(' ', '')  # 半角空格
    OutputText = InputText.replace('\n', '')
    return OutputText


InputText = ''

# 预处理
InputText = DelOCRError(InputText)
if '(' in InputText:  # 删除Word等使用的注音假名，注意是半角()
    InputText = DelWordRuby(InputText)
if re.search(r'^[\u30a0-\u30ff]*?$', InputText) != None:  # 转换片假名书写的单词
    InputText = ConverHina2kata(InputText)
if re.search(r'(\w{1})(々|〻|ゝ|ヽ)', InputText) != None:
    InputText = ConverRepeSingleSign(InputText)
if re.search(r'^(.*?)(\w{1})(ヾ|ゞ)(.*?)$', InputText) != None:
    InputText = ConverRepeSingleDakuSign(InputText)
if re.search(r'^(\w{2})(〳〵|／＼)(.*?)$', InputText) != None:
    InputText = ConverRepeDoubleSign(InputText)
if re.search(r'^(.*?)(〴〵|／″＼)(.*?)$', InputText) != None:
    InputText = ConverRepeDoubleDakuSign(InputText)


OutputText = ConvertConjugate(InputText)
print(OutputText)
EndTime = time.perf_counter()
print('耗时:%s毫秒' % (round((EndTime - StartTime)*1000, 3)))

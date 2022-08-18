import os
import time

'''
返回所有查询结果
'''
StartTime = time.perf_counter()


def GetGodannJiSho(InputText):  # 下表还可以再修改
    GodanLastLetter = ["え", "お", "か", "が", "き", "ぎ", "け", "げ", "こ", "ご", "さ", "し", "せ", "そ", "た", "ち",
                       "て", "と", "な", "に", "ね", "の", "ば", "び", "べ", "ぼ", "ま", "み", "め", "も", "ら", "り", "れ", "ろ", "わ"]
    if LastLetter not in GodanLastLetter:
        print("非五段动词变形！")
    if LastLetter in ["が", "ぎ", "げ", "ご"]:
        GodannJiSho = InputText[0:-1] + "ぐ"
    elif LastLetter == "と":
        GodannJiSho = InputText[0:-1]+"つ"
    elif LastLetter == "ば":
        GodannJiSho = InputText[0:-1]+"ぶ"
    elif LastLetter == "わ":
        GodannJiSho = InputText[0:-1] + "う"
    else:
        Jisho_Dic = {}
        GodanJishoLastLetter = ['う', 'く', 'す', 'つ', 'ぬ', 'ぶ', 'む', 'る']
        for i in GodanJishoLastLetter:
            Jisho_Dic[abs(ord(i)-ord(LastLetter))] = i  # 计算输入的假名与词尾原型假名之间的距离
        GodannJiSho = InputText[0:-1] + \
            Jisho_Dic.get(min(Jisho_Dic.keys()), '无法判断该五段假名的原型')
    return GodannJiSho


IndexTextList = []
with open('v3_index.txt', 'r', encoding='utf-8') as f:
    IndexText = f.readlines()
    for i in IndexText:
        IndexTextList.append(i.replace('\n', ''))


def SearchInIndex(SearchText):
    print('尝试在索引中查找'+SearchText)
    if SearchText in IndexTextList:
        global SearchResult
        SearchResult = SearchText
        Output.append(SearchResult)
        return SearchResult
    else:
        SearchResult = InputText+'无该索引'
        return False


def ProcessNeedOnceProcess_Godan(InputText):
    if LastLetter in ["わ", "え", "お"]:
        ProcessResult = InputText[0:-1]+InputText[-1].replace(LastLetter, 'う')
    elif LastLetter in ["か", "き", "け", "こ"]:
        ProcessResult = InputText[0:-1]+InputText[-1].replace(LastLetter, 'く')
    elif LastLetter in ["が", "ぎ", "げ", "ご"]:
        ProcessResult = InputText[0:-1]+InputText[-1].replace(LastLetter, 'ぐ')
    elif LastLetter in ["し", "せ"]:
        ProcessResult = InputText[0:-1]+InputText[-1].replace(LastLetter, 'す')
    elif LastLetter in ["に", "ね", "の"]:
        ProcessResult = InputText[0:-1]+InputText[-1].replace(LastLetter, 'ぬ')
    elif LastLetter in ["ば", "び", "べ", "ぼ"]:
        ProcessResult = InputText[0:-1]+InputText[-1].replace(LastLetter, 'ぶ')
    elif LastLetter in ["め", 'も']:
        ProcessResult = InputText[0:-1]+InputText[-1].replace(LastLetter, 'む')
    elif LastLetter in ["り"]:
        ProcessResult = InputText[0:-1]+InputText[-1].replace(LastLetter, 'る')
    else:
        ProcessResult = InputText
        print(ProcessResult+"ProcessNeedOnceProcess_Godan异常")
    return ProcessResult


NoNeedProcess = ['ぐ', 'つ', 'ぶ', 'む', 'る']

NeedOnceProcess = ['ご', 'に', 'び', '、', 'し', 'も', 'お', 'ず', 'が', 'せ', 'ぎ', 'べ',
                   'ぐ', 'ぼ', 'げ', 'る', 'よ', 'え', 'き', 'り', 'ば', 'わ', 'め', 'の', 'ね', 'こ']

NeedOnceProcess_itidann = ['、', 'ず', 'よ']
NeedOnceProcess_godann = ["ご", "に", "び", "し", "も", "お", "が", "せ",
                          "ぎ", "べ", "ぼ", "げ", "え", "き", "り", "ば", "わ", "め", "の", "ね", "こ"]

NeedTwiceProcess = ["か", "す", "た", "ら", "け", "み", "ろ",
                    "ま", "そ", "ぬ", "れ", "な", "く", "と", "う", "て", "ち"]

NeedTwiceProcess_Jisho = ['す', 'ぬ', 'く', 'う']  # 这几个词尾假名可能是来自：原型

NeedTwiceProcess_adj = ['か', 'け', 'み', 'そ']  # 这几个词尾来源：形容词/一段/五段

NeedTwiceProcess_itidann = ['た', 'ら', 'ろ', 'ま',
                            'れ', 'な', 'と', 'て', 'ち']  # 这些只可能来自一段/五段


ProcessPath = os.getcwd()


def ConvertConjugate(InputText):
    global Output, LastLetter
    Output = []  # 保留查询的结果

    SearchInIndex(InputText)  # 查看是否收录在词典中
    LastLetter = InputText.replace('\n', '')[-1]

    ProcessText = InputText+'る'  # 一段动词的连用形1
    SearchInIndex(ProcessText)
    if LastLetter in NoNeedProcess:
        print('不用处理的假名')
        ProcessText = InputText
        SearchInIndex(ProcessText)
    elif LastLetter in NeedTwiceProcess_Jisho:
        ProcessText = InputText[0:-1]+InputText[-1].replace(LastLetter, 'い')
        SearchInIndex(ProcessText)
        ProcessText = InputText[0:-1]+InputText[-1].replace(LastLetter, 'る')
        SearchInIndex(ProcessText)
    elif LastLetter in NeedOnceProcess_itidann:
        ProcessText = InputText[0:-1]+InputText[-1].replace(LastLetter, 'る')
        SearchInIndex(ProcessText)
        ProcessText = ProcessNeedOnceProcess_Godan(InputText)
        SearchInIndex(ProcessText)
    elif LastLetter in NeedOnceProcess_godann:
        ProcessText = ProcessNeedOnceProcess_Godan(InputText)
        SearchInIndex(ProcessText)
        ProcessText = ProcessText+'る'
        SearchInIndex(ProcessText)
    elif LastLetter in NeedTwiceProcess:
        ProcessText = InputText  # 原型
        SearchInIndex(ProcessText)
        ProcessText = InputText[0:-1] + \
            InputText[-1].replace(LastLetter, 'い')  # 形容词
        SearchInIndex(ProcessText)
        ProcessText = InputText[0:-1] + \
            InputText[-1].replace(LastLetter, 'る')
        SearchInIndex(ProcessText)
        ProcessText = GetGodannJiSho(InputText)
        SearchInIndex(ProcessText)
    elif LastLetter == 'っ':  # る五段/つ/う
        ProcessText = InputText[0:-1]+InputText[-1].replace(LastLetter, 'る')
        SearchInIndex(ProcessText)
        ProcessText = InputText[0:-1]+InputText[-1].replace(LastLetter, 'つ')
        SearchInIndex(ProcessText)
        ProcessText = InputText[0:-1] + \
            InputText[-1].replace(LastLetter, 'う')
        SearchInIndex(ProcessText)
        if InputText == '行っ':
            Output.append('行く')
            SearchInIndex(ProcessText)
            Output.append(InputText)
    elif LastLetter == 'さ':
        ProcessText = InputText[0:-1]+InputText[-1].replace(LastLetter, 'い')
        SearchInIndex(ProcessText)

        ProcessText = InputText[0:-1]+InputText[-1].replace(LastLetter, 'す')
        SearchInIndex(ProcessText)

        ProcessText = InputText[0:-1] + \
            InputText[-1].replace(LastLetter, 'る')
        SearchInIndex(ProcessText)
    elif LastLetter == 'ん':
        ProcessText = InputText[0:-1]+InputText[-1].replace(LastLetter, 'む')
        SearchInIndex(ProcessText)
        ProcessText = InputText[0:-1]+InputText[-1].replace(LastLetter, 'ぶ')
        SearchInIndex(ProcessText)
        ProcessText = InputText[0:-1] + \
            InputText[-1].replace(LastLetter, 'ぬ')
        SearchInIndex(ProcessText)
        ProcessText = InputText[0:-1] + \
            InputText[-1].replace(LastLetter, 'る')
        SearchInIndex(ProcessText)
    elif LastLetter == "い":
        ProcessText = InputText[0:-1]+InputText[-1].replace(LastLetter, 'う')
        SearchInIndex(ProcessText)
        ProcessText = InputText[0:-1] + \
            InputText[-1].replace(LastLetter, 'く')
        SearchInIndex(ProcessText)
        ProcessText = InputText[0:-1] + \
            InputText[-1].replace(LastLetter, 'ぐ')
        SearchInIndex(ProcessText)
    elif LastLetter == 'ゃ':
        ProcessText = InputText[0:-2]+InputText[-2:].replace('ちゃ', 'る')
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


InputText = '行っ'
OutputText = ConvertConjugate(InputText)
print(OutputText)
EndTime = time.perf_counter()
print('耗时:%s毫秒' % (round((EndTime - StartTime)*1000, 3)))

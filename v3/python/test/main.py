import os
import re
import time

'''
返回所有查询结果
'''
StartTime = time.perf_counter()


def GetGodannJiSho(InputText):  # 下表还可以再修改
    GodanLastLetter = 'えおかがきぎけげこごさしせそたちてとなにねのばびべぼまみめもらりれろわ'
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
        GodanJishoLastLetter = 'うくすつぬぶむる'
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




NeedOnceProcess_itidann = '、ずよぬ'
NeedOnceProcess_godann = 'わえおがきぎげこごしせにねのばびべぼめもり'
NeedOnceProcess_adj = 'くうす'

NeedTwiceProcess = 'かすたらけみろまそぬれなくとうてち'

NeedTwiceProcess_Jisho = 'すぬくう'  # 这几个词尾假名可能是来自：原型

NeedTwiceProcess_adj = 'かけみそ'  # 这几个词尾来源：形容词/一段/五段

NeedTwiceProcess_itidann = 'たらろまれなとてち'  # 这些只可能来自一段/五段


ProcessPath = os.getcwd()


def ConvertConjugate(InputText):
    global Output, LastLetter
    Output = []  # 保留查询的结果

    SearchInIndex(InputText)  # 查看是否收录在词典中
    LastLetter = InputText.replace('\n', '')[-1]

    ProcessText = InputText+'る'  # 一段动词的连用形1
    SearchInIndex(ProcessText)
    if LastLetter in NeedTwiceProcess_Jisho:
        ProcessText = InputText[0:-1] + 'い'
        SearchInIndex(ProcessText)
        ProcessText = InputText[0:-1] + 'る'
        SearchInIndex(ProcessText)
    elif LastLetter in NeedOnceProcess_itidann:
        ProcessText = InputText[0:-1]+'る'
        SearchInIndex(ProcessText)
    elif LastLetter in NeedOnceProcess_godann:
        ProcessText = ProcessNeedOnceProcess_Godan(InputText)
        SearchInIndex(ProcessText)
    elif LastLetter in NeedOnceProcess_adj:
        ProcessText = InputText[0:1]+'い'
        SearchInIndex(ProcessText)
    elif LastLetter in NeedTwiceProcess:
        ProcessText = InputText  # 原型
        SearchInIndex(ProcessText)
        ProcessText = InputText[0:-1] + 'い'  # 形容词
        SearchInIndex(ProcessText)
        ProcessText = InputText[0:-1] + 'る'
        SearchInIndex(ProcessText)
        ProcessText = GetGodannJiSho(InputText)
        SearchInIndex(ProcessText)
    elif LastLetter == 'っ':  # る五段/つ/う
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
        ProcessText = InputText[0:-1]+'い'
        SearchInIndex(ProcessText)

        ProcessText = InputText[0:-1]+'す'
        SearchInIndex(ProcessText)

        ProcessText = InputText[0:-1] + \
            InputText[-1].replace(LastLetter, 'る')
        SearchInIndex(ProcessText)
    elif LastLetter == 'ん':
        ProcessText = InputText[0:-1]+'む'
        SearchInIndex(ProcessText)
        ProcessText = InputText[0:-1]+'ぶ'
        SearchInIndex(ProcessText)
        ProcessText = InputText[0:-1] + 'ぬ'
        SearchInIndex(ProcessText)
        ProcessText = InputText[0:-1] + 'る'
        SearchInIndex(ProcessText)
    elif LastLetter == "い":
        ProcessText = InputText[0:-1] + 'う'
        SearchInIndex(ProcessText)
        ProcessText = InputText[0:-1] + 'く'
        SearchInIndex(ProcessText)
        ProcessText = InputText[0:-1] + 'ぐ'
        SearchInIndex(ProcessText)
    elif LastLetter == 'ゃ':
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


with open('temp.txt', 'r', encoding='utf-8') as f, open('save.txt', 'w', encoding='utf-8')as s:
    FileContextList = f.readlines()
    i = 0
    Len = len(FileContextList)
    for line in FileContextList:
        reg = r'^(.*?)\t'
        NonJishoText = re.search(reg, line.replace('\n', ''))
        InputText = NonJishoText.group().replace('\t', '')
        Output = []
        ConvertConjugate(InputText)
        s.write(str(Output).replace("'", "")+'\t'+line)
        i += 1
        print(str(i/Len))
os.system('python review_v3.py')
EndTime = time.perf_counter()
print('耗时:%s毫秒' % (round((EndTime - StartTime)*1000, 3)))

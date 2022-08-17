


import os
import re
import time

'''
这个脚本理论上只会返回1个结果，现已放弃维护，如有需要请自行维护，截至2022-08-17，本算法准确度如下所示，注意我使用了pypy3内核进行加速
![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com/20220817180608.png)
'''
StartTime = time.perf_counter()

def GetGodannJiSho(InputText):  # 下表还可以再修改
    GodanLastLetter = "えおかがきぎけげこごさしせそたちてとなにねのばびべぼまみめもらりれろわ"
    if LastLetter not in GodanLastLetter:
        print("非五段动词变形！")
    if LastLetter in "がぎげご":
        GodannJiSho = InputText.replace(LastLetter, "ぐ")
    elif LastLetter == "と":
        GodannJiSho = InputText.replace(LastLetter, "つ")
    elif LastLetter == "ば":
        GodannJiSho = InputText.replace(LastLetter, "ぶ")
    elif LastLetter == "わ":
        GodannJiSho = InputText.replace(LastLetter, "う")
    else:
        Jisho_Dic = {}
        GodanJishoLastLetter = "うくすつぬぶむる"
        for i in GodanJishoLastLetter:
            Jisho_Dic[abs(ord(i)-ord(LastLetter))] = i  # 计算输入的假名与词尾原型假名之间的距离
        GodannJiSho = InputText.replace(LastLetter, Jisho_Dic.get(
            min(Jisho_Dic.keys()), '无法判断该五段假名的原型'))
    return GodannJiSho


def SearchInIndex(InputText):
    # print('尝试在索引中查找'+InputText)
    if InputText in IndexTextList:
        global SearchResult
        SearchResult = InputText
        Output.add(SearchResult)
        return SearchResult
    else:
        SearchResult = InputText+'无该索引'
        return False


def ProcessNeedOnceProcess_Godan(InputText):
    if LastLetter in "わえお":
        ProcessResult = InputText[0:-1]+InputText[-1].replace(LastLetter, 'う')
    elif LastLetter in "かきけこ":
        ProcessResult = InputText[0:-1]+InputText[-1].replace(LastLetter, 'く')
    elif LastLetter in "がぎげご":
        ProcessResult = InputText[0:-1]+InputText[-1].replace(LastLetter, 'ぐ')
    elif LastLetter in "しせ":
        ProcessResult = InputText[0:-1]+InputText[-1].replace(LastLetter, 'す')
    elif LastLetter in "にねの":
        ProcessResult = InputText[0:-1]+InputText[-1].replace(LastLetter, 'ぬ')
    elif LastLetter in "ばびべぼ":
        ProcessResult = InputText[0:-1]+InputText[-1].replace(LastLetter, 'ぶ')
    elif LastLetter in "めも":
        ProcessResult = InputText[0:-1]+InputText[-1].replace(LastLetter, 'む')
    elif LastLetter in "り":
        ProcessResult = InputText[0:-1]+InputText[-1].replace(LastLetter, 'る')
    else:
        ProcessResult = InputText
        print(ProcessResult+"ProcessNeedOnceProcess_Godan异常")
    return ProcessResult


def Process(InputText):
    if LastLetter in NoNeedProcess:
        print('不用处理的假名')
        ProcessText = InputText
        if SearchInIndex(ProcessText) == False:
            Output.add(InputText)
    elif LastLetter in NeedOnceProcess_itidann:
        ProcessText = InputText[0:-1]+InputText[-1].replace(LastLetter, 'る')
        if SearchInIndex(ProcessText) == False:
            Output.add(InputText)
    elif LastLetter in NeedOnceProcess_godann:
        ProcessText = ProcessNeedOnceProcess_Godan(InputText)
        if SearchInIndex(ProcessText) == False:
            ProcessText = ProcessText+'る'
            if SearchInIndex(ProcessText) == False:
                Output.add(InputText)
    elif LastLetter in NeedTwiceProcess:
        print('至少需要处理2次')
        ProcessText = InputText  # 原型
        if SearchInIndex(ProcessText) == False:  # 形容词/一段/五段
            print('不是原型')
            ProcessText = InputText[0:-1] + \
                InputText[-1].replace(LastLetter, 'い')  # 形容词
            if SearchInIndex(ProcessText) == False:  # 一段/五段
                print('不是形容词')
                ProcessText = InputText[0:-1] + \
                    InputText[-1].replace(LastLetter, 'る')
                if SearchInIndex(ProcessText) == False:  # 五段
                    print('不是一段动词尝试在五段动词中查找')
                    ProcessText = GetGodannJiSho(InputText)
                    print('ま'+ProcessText)
                    if SearchInIndex(ProcessText) == False:
                        Output.add(InputText)
    elif LastLetter == 'っ':  # る五段/つ/う
        ProcessText = InputText[0:-1]+InputText[-1].replace(LastLetter, 'る')
        if SearchInIndex(ProcessText) == False:
            ProcessText = InputText[0:-1]+InputText[-1].replace(LastLetter, 'つ')
            if SearchInIndex(ProcessText) == False:
                ProcessText = InputText[0:-1] + \
                    InputText[-1].replace(LastLetter, 'う')
                if InputText == '行っ':
                    Output.add('行く')
                    if SearchInIndex(ProcessText) == False:
                        Output.add(InputText)
    elif LastLetter == 'さ':
        # print('尝试在形容词中进行查找')
        ProcessText = InputText[0:-1]+InputText[-1].replace(LastLetter, 'い')
        if SearchInIndex(ProcessText) == False:
            # print('尝试在五段动词中查找')
            ProcessText = InputText[0:-1]+InputText[-1].replace(LastLetter, 'す')
            if SearchInIndex(ProcessText) == False:
                # print('尝试在一段动词中查找')
                ProcessText = InputText[0:-1] + \
                    InputText[-1].replace(LastLetter, 'る')
                if SearchInIndex(ProcessText) == False:
                    Output.add(InputText)
    elif LastLetter == 'ん':
        ProcessText = InputText[0:-1]+InputText[-1].replace(LastLetter, 'む')
        if SearchInIndex(ProcessText) == False:
            ProcessText = InputText[0:-1]+InputText[-1].replace(LastLetter, 'ぶ')
            if SearchInIndex(ProcessText) == False:
                ProcessText = InputText[0:-1] + \
                    InputText[-1].replace(LastLetter, 'ぬ')
                if SearchInIndex(ProcessText) == False:
                    ProcessText = InputText[0:-1] + \
                        InputText[-1].replace(LastLetter, 'る')
                    if SearchInIndex(ProcessText) == False:
                        Output.add(InputText)
    elif LastLetter == "い":
        print('い有可能是形容词的原型，进行尝试性查找') # 没有必要，在正式开始查找前已经进行原型尝试
        ProcessText = InputText
        if SearchInIndex(ProcessText) == False:
            # print('尝试在在五段う查找')
            ProcessText = InputText[0:-1]+InputText[-1].replace(LastLetter, 'う')
            if SearchInIndex(ProcessText) == False:
                # print('尝试在五段く查找')
                ProcessText = InputText[0:-1] + \
                    InputText[-1].replace(LastLetter, 'く')
                if SearchInIndex(ProcessText) == False:
                    # print('尝试在五段ぐ查找')
                    ProcessText = InputText[0:-1] + \
                        InputText[-1].replace(LastLetter, 'ぐ')
                    if SearchInIndex(ProcessText) == False:
                        Output.add(InputText)
    elif LastLetter == 'ゃ':
        print('特殊词尾假名，单独处理')
        ProcessText = InputText[0:-2]+InputText[-2:].replace('ちゃ','る')
        if SearchInIndex(ProcessText) == False:
            print("找不到"+InputText + "原型")
            Output.add(InputText)
    else:
        print("找不到"+InputText + "原型")
        Output.add(InputText)


IndexTextDic = {}
IndexTextList = []
with open('v3_index.txt','r', encoding='utf-8') as f:
    IndexText = f.readlines()
    for i in IndexText:
        IndexTextList.append(i.replace('\n',''))


NoNeedProcess = "ぐつぶむる"

NeedOnceProcess = "ごにび、しもおずがせぎべぐぼげるよえきりばわめのねこ"

NeedOnceProcess_itidann = "、ずよ"
NeedOnceProcess_godann = "ごにびしもおがせぎべぼげえきりばわめのねこ"

NeedTwiceProcess = "かすたらけみろまそぬれなくとうてち"

NeedTwiceProcess_Jisho = "すぬくう" # 这几个词尾假名可能是来自：原型

NeedTwiceProcess_adj = "かけみそ" # 这几个词尾来源：形容词/一段/五段

NeedTwiceProcess_itidann = "たらろまれなとてち" # 这些只可能来自一段/五段

ProcessPath = os.getcwd()

with open('temp.txt','r', encoding='utf-8') as f, open('save.txt','w', encoding='utf-8')as s:
    FileContextList = f.readlines()
    i = 0
    Len = len(FileContextList)
    for line in FileContextList:
        reg = r'^(.*?)\t'
        NonJishoText = re.search(reg, line.replace('\n',''))
        InputText = NonJishoText.group().replace('\t','')
        LastLetter = InputText[-1]
        Output = set()
        ProcessText = InputText+'る' # 一段动词的连用形1
        SearchInIndex(ProcessText)
        Process(InputText)
        s.write(str(Output).replace("'","")+'\t'+line)
        i += 1
        print(str(i/Len))
os.system('review_v3.py')
EndTime = time.perf_counter()
print('耗时:%s毫秒' % (round((EndTime - StartTime)*1000, 3)))

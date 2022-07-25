
from base64 import encode
import os
from re import S


def GetGodannJiSho(InputText):  # 下表还可以再修改
    GodanLastLetter = ["え", "お", "か", "が", "き", "ぎ", "け", "げ", "こ", "ご", "さ", "し", "せ", "そ", "た", "ち",
                       "て", "と", "な", "に", "ね", "の", "ば", "び", "べ", "ぼ", "ま", "み", "め", "も", "ら", "り", "れ", "ろ", "わ"]
    if LastLetter not in GodanLastLetter:
        print("非五段动词变形！")
    if LastLetter in ["が", "ぎ", "げ", "ご"]:
        GodannJiSho = InputText.replace(LastLetter, "ぐ")
    elif LastLetter == "と":
        GodannJiSho = InputText.replace(LastLetter, "つ")
    elif LastLetter == "ば":
        GodannJiSho = InputText.replace(LastLetter, "ぶ")
    elif LastLetter == "わ":
        GodannJiSho = InputText.replace(LastLetter, "う")
    else:
        Jisho_Dic = {}
        GodanJishoLastLetter = ['う', 'く', 'す', 'つ', 'ぬ', 'ぶ', 'む', 'る']
        for i in GodanJishoLastLetter:
            Jisho_Dic[abs(ord(i)-ord(LastLetter))] = i
        GodannJiSho = InputText.replace(LastLetter, Jisho_Dic.get(
            min(Jisho_Dic.keys()), '无法判断该五段假名的原型'))
    return GodannJiSho


def SearchInIndex(InputText):
    print('在索引中查找'+InputText)
    if InputText in IndexTextList:
        global SearchResult
        SearchResult = InputText
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


ProcessPath = os.getcwd()

IndexTextDic = {}
IndexTextList = []
with open('v3_index.txt', 'r', encoding='utf-8') as f:
    IndexText = f.readlines()
    for i in IndexText:
        IndexTextList.append(i.replace('\n', ''))
    '''for i in IndexText:
        IndexTextDic[hash(i)] = IndexTextDic.get(i,0)'''


NoNeedProcess = ['ぐ', 'つ', 'ぶ', 'む', 'る']

NeedOnceProcess = ['ご', 'に', 'び', '、', 'し', 'も', 'お', 'ず', 'が', 'せ', 'ぎ', 'べ',
                   'ぐ', 'ぼ', 'げ', 'る', 'よ', 'え', 'き', 'り', 'ば', 'わ', 'め', 'の', 'ね', 'こ']

NeedOnceProcess_itidann = [ '、', 'ず', 'よ']
NeedOnceProcess_godann = ["ご", "に", "び", "し", "も", "お", "が", "せ",
                          "ぎ", "べ", "ぼ", "げ", "え", "き", "り", "ば", "わ", "め", "の", "ね", "こ"]

NeedTwiceProcess = ["か", "す", "た", "ら", "け", "み", "ろ",
                    "ま", "そ", "ぬ", "れ", "な", "く", "と", "う", "て", "ち"]

NeedTwiceProcess_Jisho = ['す', 'ぬ', 'く', 'う']  # 这几个词尾假名可能是来自：原型

NeedTwiceProcess_adj = ['か', 'け', 'み', 'そ']  # 这几个词尾来源：形容词/一段/五段

NeedTwiceProcess_itidann = ['た', 'ら', 'ろ', 'ま',
                            'れ', 'な', 'と', 'て', 'ち']  # 这些只可能来自一段/五段


ProcessPath = os.getcwd()


InputText = '相異なれ'
Output = []

LastLetter = InputText.replace('\n', '')[-1]
print(LastLetter)
if LastLetter in NoNeedProcess:
    print('不用处理的假名')
    ProcessText = InputText
    if SearchInIndex(ProcessText) == False:
        print("出现问题了，这里应该是词典收录的原型"+ProcessText)
elif LastLetter in NeedOnceProcess:
    #print('至少需要处理一次，因为无法确定词性')
    #if LastLetter in NeedOnceProcess_itidann:
        #print('一段动词特有的词尾假名')
        ProcessText = InputText[0:-1]+InputText[-1].replace(LastLetter, 'る')
        if SearchInIndex(ProcessText) == False:
            #print('非一段动词的特殊假名，尝试五段特殊变换假名中查找')
            #print("出现问题了，这里应该是词典收录的原型"+ProcessText)
            #if LastLetter in NeedOnceProcess_godann:
            ProcessText = ProcessNeedOnceProcess_Godan(InputText)
            if SearchInIndex(ProcessText) == False:
                    ProcessText = ProcessText+'る'
                    if SearchInIndex(ProcessText) == False:
                        print("找不到"+InputText + "原型")
                        print("出现问题了，这里应该是词典收录的原型"+ProcessText)
elif LastLetter in NeedTwiceProcess:
    print('至少需要处理2次')
    # if LastLetter in NeedTwiceProcess_Jisho: # 原型/形容词/一段/五段
    ProcessText = InputText  # 原型
    if SearchInIndex(ProcessText) == False:  # 形容词/一段/五段
        print('不是原型')
        ProcessText = InputText[0:-1]+InputText[-1].replace(LastLetter, 'い')  # 形容词
        if SearchInIndex(ProcessText) == False:  # 一段/五段
            print('不是形容词')
            ProcessText = InputText[0:-1]+InputText[-1].replace(LastLetter, 'る')
            #if SearchInIndex(ProcessText) == False:
                #print(SearchResult+'是原型,一段')  # 一段
            if SearchInIndex(ProcessText) == False:  # 五段
                print('不是一段动词尝试在五段动词中查找')
                ProcessText = GetGodannJiSho(InputText)
                SearchInIndex(ProcessText)
                print(SearchResult)
elif LastLetter == 'っ':  # る五段/つ/う
    ProcessText = InputText[0:-1]+InputText[-1].replace(LastLetter, 'る')
    if SearchInIndex(ProcessText) == False:
        ProcessText = InputText[0:-1]+InputText[-1].replace(LastLetter, 'つ')
        if SearchInIndex(ProcessText) == False:
            ProcessText = InputText[0:-1]+InputText[-1].replace(LastLetter, 'う')
            print(ProcessText)
elif LastLetter == 'さ':
    print('尝试在形容词中进行查找')
    ProcessText = InputText[0:-1]+InputText[-1].replace(LastLetter, 'い')
    if SearchInIndex(ProcessText) == False:
        print('尝试在五段动词中查找')
        ProcessText = InputText[0:-1]+InputText[-1].replace(LastLetter, 'す')
        if SearchInIndex(ProcessText) == False:
            print('尝试在一段动词中查找')
            ProcessText = InputText[0:-1]+InputText[-1].replace(LastLetter, 'る')
elif LastLetter == 'ん':
    ProcessText = InputText[0:-1]+InputText[-1].replace(LastLetter, 'む')
    if SearchInIndex(ProcessText) == False:
        ProcessText = InputText[0:-1]+InputText[-1].replace(LastLetter, 'ぶ')
        if SearchInIndex(ProcessText) == False:
            ProcessText = InputText[0:-1]+InputText[-1].replace(LastLetter, 'ぬ')
            if SearchInIndex(ProcessText) == False:
                ProcessText = InputText[0:-1]+InputText[-1].replace(LastLetter, 'る')
                # print(ProcessText)
elif LastLetter == "い":
    print('有可能是形容词的原型，进行尝试性查找')
    ProcessText = InputText
    if SearchInIndex(ProcessText) == False:
        print('尝试在在五段う查找')
        ProcessText = InputText[0:-1]+InputText[-1].replace(LastLetter, 'う')
        if SearchInIndex(ProcessText) == False:
            print('尝试在五段く查找')
            ProcessText = InputText[0:-1]+InputText[-1].replace(LastLetter, 'く')
            if SearchInIndex(ProcessText) == False:
                print('尝试在五段ぐ查找')
                ProcessText = InputText[0:-1]+InputText[-1].replace(LastLetter, 'ぐ')
elif LastLetter == 'ゃ':
    print('特殊词尾假名，单独处理')
    ProcessText = InputText[0:-2]+InputText[-2:].replace('ちゃ', 'る')
    if SearchInIndex(ProcessText) == False:
        print("找不到"+InputText + "原型")
else:
    ProcessText = InputText+'る'
    if SearchInIndex(ProcessText) == False:
        print("找不到"+InputText + "原型")
print(ProcessText)


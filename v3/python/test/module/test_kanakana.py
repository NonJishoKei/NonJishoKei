'''
计算输入值的Unicode码，并尝试将其转为平假名后在词典中进行查找
需要匹配的示例：
チョコチョコ（当有拗音时，单词长度就不是4了）
ヒト（不止有拟声拟态词会写假名）
不能匹配的：
タピる（部分合成的外来语，往往是固定说法，不要随意拆分不全是片假名的单词，因为权威的词典很可能不会收录转换后的写法）
'''
import re
import time
StartTime = time.perf_counter()
InputText = 'ちょこちょこ'


def ConverHina2kata(InputText):
    ProcessTexts = []
    for gana in InputText:
        if 12448 < int(ord(gana)) < 12543:  # 匹配片假名
            hira = chr(int(ord(gana) - 96))
            ProcessTexts.append(hira)
    OutputText = ''.join(ProcessTexts)
    return OutputText


if re.search(r'^[\u30a0-\u30ff]*?$', InputText) != None:
    print(ConverHina2kata(InputText))

EndTime = time.perf_counter()
print('耗时:%s毫秒' % (round((EndTime - StartTime)*1000, 3)))

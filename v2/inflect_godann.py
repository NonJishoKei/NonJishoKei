from dataclasses import replace
from msilib.schema import Error
import os
import re

ProessPath = os.getcwd()

InputFile = r'temp.txt'
OutputFile = r'save.txt'

with open(InputFile,
          'r', encoding='UTF-8') as f, open(OutputFile,
                                            'w',
                                            encoding='utf-8') as f2:
    for line in f:
        kana = line[-2]
        line = line.replace('（','')
        line =  line.replace('）','')
        dichtml = r'<section class="description"><a href="entry://'+line.replace('\n','')+r'#description">'+line.replace('\n','')+'</a>\n</section>\n</>'+'\n'
        if kana == 'う':
            line_1 = line[0:-2] + line[-2].replace("う", "わ" + '\n')+dichtml
            line_2 = line[0:-2] + line[-2].replace("う", "お" + '\n')+dichtml
            line_3 = line[0:-2] + line[-2].replace("う", "い" + '\n')+dichtml
            line_4 = line[0:-2] + line[-2].replace("う", "っ" + '\n')+dichtml
            line_5 = line[0:-2] + line[-2].replace("う", "え" + '\n')+dichtml
            f2.write(line_1+line_2+line_3+line_4+line_5)
        elif kana == 'く':
            line_1 = line[0:-2] + line[-2].replace("く", 'か' + '\n')+dichtml
            line_2 = line[0:-2] + line[-2].replace("く", 'こ' + '\n')+dichtml
            line_3 = line[0:-2] + line[-2].replace("く", 'き' + '\n')+dichtml
            line_4 = line[0:-2] + line[-2].replace("く", 'い' + '\n')+dichtml
            line_5 = line[0:-2] + line[-2].replace("く", 'け' + '\n')+dichtml
            f2.write(line_1+line_2+line_3+line_4+line_5)
        elif kana == 'ぐ':
            line_1 = line[0:-2] + line[-2].replace("ぐ", 'が' + '\n')+dichtml
            line_2 = line[0:-2] + line[-2].replace("ぐ", 'ぎ' + '\n')+dichtml
            line_3 = line[0:-2] + line[-2].replace("ぐ", 'げ' + '\n')+dichtml
            line_4 = line[0:-2] + line[-2].replace("ぐ", 'ご' + '\n')+dichtml
            line_5 = line[0:-2] + line[-2].replace("ぐ", 'い' + '\n')+dichtml
            f2.write(line_1+line_2+line_3+line_4+line_5)
        elif kana == 'す':
            line_1 = line[0:-2] + line[-2].replace("す", 'さ' + '\n')+dichtml
            line_2 = line[0:-2] + line[-2].replace("す", 'し' + '\n')+dichtml
            line_3 = line[0:-2] + line[-2].replace("す", 'せ' + '\n')+dichtml
            line_4 = line[0:-2] + line[-2].replace("す", 'そ' + '\n')+dichtml
            f2.write(line_1+line_2+line_3+line_4)
        elif kana == 'ず':
            print(line) # 没有的啦
        elif kana == 'つ':
            line_1 = line[0:-2] + line[-2].replace("つ", 'た' + '\n')+dichtml
            line_2 = line[0:-2] + line[-2].replace("つ", 'ち' + '\n')+dichtml
            line_3 = line[0:-2] + line[-2].replace("つ", 'て' + '\n')+dichtml
            line_4 = line[0:-2] + line[-2].replace("つ", 'と' + '\n')+dichtml
            line_5 = line[0:-2] + line[-2].replace("つ", 'っ' + '\n')+dichtml
            f2.write(line_1+line_2+line_3+line_4+line_5)
        elif kana == 'づ':
            print(line) #没有的啦
        elif kana == 'ぬ':
            line_1 = line[0:-2] + line[-2].replace("ぬ", 'な' + '\n')+dichtml
            line_2 = line[0:-2] + line[-2].replace("ぬ", 'に' + '\n')+dichtml
            line_3 = line[0:-2] + line[-2].replace("ぬ", 'ね' + '\n')+dichtml
            line_4 = line[0:-2] + line[-2].replace("ぬ", 'の' + '\n')+dichtml
            line_5 = line[0:-2] + line[-2].replace("ぬ", 'ん' + '\n')+dichtml
            f2.write(line_1+line_2+line_3+line_4+line_5)
        elif kana == 'ふ':
            print(line)#古语中才会出现
        elif kana == 'ぶ':
            line_1 = line[0:-2] + line[-2].replace("ぶ", 'ば' + '\n')+dichtml
            line_2 = line[0:-2] + line[-2].replace("ぶ", 'び' + '\n')+dichtml
            line_3 = line[0:-2] + line[-2].replace("ぶ", 'べ' + '\n')+dichtml
            line_4 = line[0:-2] + line[-2].replace("ぶ", 'ぼ' + '\n')+dichtml
            line_5 = line[0:-2] + line[-2].replace("ぶ", 'ん' + '\n')+dichtml
            f2.write(line_1+line_2+line_3+line_4+line_5)
        elif kana == 'ぷ':
            print(line)
        elif kana == 'む':
            line_1 = line[0:-2] + line[-2].replace("む", 'ま' + '\n')+dichtml
            line_2 = line[0:-2] + line[-2].replace("む", 'み' + '\n')+dichtml
            line_3 = line[0:-2] + line[-2].replace("む", 'め' + '\n')+dichtml
            line_4 = line[0:-2] + line[-2].replace("む", 'も' + '\n')+dichtml
            line_5 = line[0:-2] + line[-2].replace("む", 'ん' + '\n')+dichtml
            f2.write(line_1+line_2+line_3+line_4+line_5)
        elif kana == 'る':
            line_1 = line[0:-2] + line[-2].replace("る", 'ら' + '\n')+dichtml
            line_2 = line[0:-2] + line[-2].replace("る", 'り' + '\n')+dichtml
            line_3 = line[0:-2] + line[-2].replace("る", 'れ' + '\n')+dichtml
            line_4 = line[0:-2] + line[-2].replace("る", 'ろ' + '\n')+dichtml
            line_5 = line[0:-2] + line[-2].replace("る", 'っ' + '\n')+dichtml
            f2.write(line_1+line_2+line_3+line_4+line_5)
        else:
            print(line)

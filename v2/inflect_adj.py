from dataclasses import replace
from msilib.schema import Error
import os
import re

ProessPath = os.getcwd()

InputFile = r'temp.txt'
OutputFile = r'save.txt'
ErrorFile = r'error.md'


with open(InputFile,
          'r', encoding='UTF-8') as f, open(OutputFile,
                                            'w',
                                            encoding='utf-8') as f2, open(
                                                ErrorFile,
                                                'w',
                                                encoding='utf-8') as f3:
    for line in f:
        line =line.replace('\n','')
        dichtml = r'<section class="description"><a href="entry://'+line+r'#description">'+line+'</a>\n</section>\n</>'+'\n'
        line = line.replace('（','')
        line =  line.replace('）','')
        line_1 = line[0:-1] + line[-1].replace("い", "け" + '\n')+dichtml
        line_2 = line[0:-1] + line[-1].replace("い", "か" + '\n')+dichtml
        line_3 = line[0:-1] + line[-1].replace("い", "く" + '\n')+dichtml
        line_4 = line[0:-1] + line[-1].replace("い", "う" + '\n')+dichtml
        line_5 = line[0:-1] + line[-1].replace("い", "さ" + '\n')+dichtml
        line_6 = line[0:-1] + line[-1].replace("い", "み" + '\n')+dichtml # 部分形容词
        line_7 = line[0:-1] + line[-1].replace("い", "そ" + '\n')+dichtml # そうだ
        line_8 = line[0:-1] + line[-1].replace("い", "す" + '\n')+dichtml# すぎる
        f2.write(line_1+line_2+line_3+line_4+line_5+line_6+line_7+line_8)

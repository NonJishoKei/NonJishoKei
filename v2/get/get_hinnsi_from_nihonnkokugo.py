import os
import re

ProessPath = os.getcwd()

InputFile = r'temp.txt'
OutputFile = r'save.txt'

with open(InputFile,encoding="UTF-8") as f,open(OutputFile,'w',encoding='UTF-8') as s:
    for line in f:
        if '<partspeech>' in line:
            regex = r'(.*?)\t(.*?)<div class="titleText">(.*?)</div>(.*?)<partspeech>(.*?)</partspeech>(.*?)$'
            replacement = r"\3\t\5" # 注意，第一列数据不是真正的书写方法
            line = re.sub(regex, replacement, line)
            s.write(line)
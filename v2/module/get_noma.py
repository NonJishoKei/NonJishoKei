import os
import re

ProessPath = os.getcwd()

InputFile = r'temp.txt'
OutputFile = r'save.txt'

OutputFileContext = []
with open(InputFile, encoding="UTF-8") as f:
    for line in f:
        regex = r'【(.)\1】'  # 【(.)\1(.)\2】
        if re.search(regex, line) != None:
            #replacement = r'\2'+'々'
            #line = re.sub(r'(.*?)【(.)\2】', replacement, line) # 明明白白 这样的四字词
            #line =  line+dichtml
            OutputFileContext.append(line)
        else:
            continue


with open(OutputFile, 'w', encoding='UTF-8') as s:
    for i in OutputFileContext:
        s.writelines(i)

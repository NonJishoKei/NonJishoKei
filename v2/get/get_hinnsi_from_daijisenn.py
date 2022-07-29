import os
import re

ProessPath = os.getcwd()

InputFile = r'temp.txt'
OutpurFile = r'save.txt'

OutputFileContext = []
with open(InputFile,encoding="UTF-8") as f:
    for line in f:
        if '<span class="hinshi">' in line:
            regex = r'(.*?)	(.*?)<span class="hinshi">(.*?)</span>(.*?)$'
            replacement = r'\1'+'\t'+r'\3'
            line = re.sub(regex, replacement, line)
            OutputFileContext.append(line)
        else:
            print(line)

with open(OutpurFile,'w',encoding='UTF-8') as s:
    for i in OutputFileContext:
        s.writelines(i)

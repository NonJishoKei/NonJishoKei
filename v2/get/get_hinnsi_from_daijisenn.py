import os
import re

ProessPath = os.getcwd()

InputFile = r'temp.md'
OutpurFile = r'save.md'

OutpurFileContext = []
with open(InputFile,encoding="UTF-8") as f:
    for line in f:
        if '<span class="hinshi">' in line:
            regex = r'(.*?)	(.*?)<span class="hinshi">(.*?)</span>(.*?)$'
            replacement = r'\1'+'\t'+r'\3'
            line = re.sub(regex, replacement, line)
            OutpurFileContext.append(line)
        else:
            print(line)

with open(OutpurFile,'w',encoding='UTF-8') as s:
    for i in OutpurFileContext:
        s.writelines(i)

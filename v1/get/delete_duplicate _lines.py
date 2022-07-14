import os

ProessPath = os.getcwd()

InputFile = r'temp.md'
OutpurFile = r'save.md'

FileContextSet =set()
with open(InputFile,encoding="UTF-8") as f:
    for line in f:
        FileContextSet.add(line) # 如果不在，返回None 

OutpurFileContext = list (FileContextSet)
with open(OutpurFile,'w',encoding='UTF-8') as s:
    for i in OutpurFileContext:
        s.writelines(i)

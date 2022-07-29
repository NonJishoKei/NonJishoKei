import os

ProessPath = os.getcwd()

InputFile = r'temp.txt'
OutputFile = r'save.txt'

FileContextSet =set()
with open(InputFile,encoding="UTF-8") as f:
    for line in f:
        FileContextSet.add(line) # 如果不在，返回None 

OutputFileContext = list (FileContextSet)
with open(OutputFile,'w',encoding='UTF-8') as s:
    for i in OutputFileContext:
        s.writelines(i)


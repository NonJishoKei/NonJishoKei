from calendar import prcal
import os

ProcessPath = os.chdir('..\\')
ProcessPath = os.getcwd()
ProcessFile = r'v3_index.txt'
LastLetters = {}
number = 1
with open(ProcessFile,'r',encoding='utf-8') as f,open('v3_index_analsis.txt','w',encoding='utf-8')as s:
    for line in f:
        line = line.replace('\n','')
        LastLetter = line[-1]
        LastLetters[LastLetter] = LastLetters.get(LastLetter,1)+1
    #print(list(LastLetters)) # 字典会直接转成只含键名的列表
    #print(type(LastLetters.items()))# <class 'dict_items'>
    for i in LastLetters.items():
        OutputLine = str(i).replace(')','\n')
        OutputLine = OutputLine.replace("',",'\t')
        OutputLine = OutputLine.replace("('",'')
        s.write(OutputLine)
        
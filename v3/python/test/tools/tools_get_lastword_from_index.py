'''
分析索引文件中所有单词词尾假名的规律
'''
import os

ProcessPath = os.chdir('..')
ProcessPath = os.getcwd()
ProcessFile = r'v3_index.txt'
LastLetters = {}
number = 1
with open(ProcessFile,'r',encoding='utf-8') as f,open('v3_index_analsis.txt','w',encoding='utf-8')as s:
    for line in f:
        line = line.replace('\n','')
        LastLetter = line[-1]
        LastLetters[LastLetter] = LastLetters.get(LastLetter,1)+1
    for i in LastLetters.items():
        OutputLine = str(i).replace(')','\n')
        OutputLine = OutputLine.replace("',",'\t')
        OutputLine = OutputLine.replace("('",'')
        s.write(OutputLine)
        
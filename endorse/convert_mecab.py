
import os
import re
import time
from pathlib import Path
import MeCab

'''
调用 Mecab 推导辞書形
'''

StartTime = time.perf_counter()

path = os.getcwd()+r"\testfiles\test"+'\\'  # 加载测试文件
FileNames = list(Path(path).glob("**/*_get_mecab.txt"))
dic_path = os.getcwd()+r'\unidic-cwj-3.1.1'+'\\'
tagger = MeCab.Tagger(
    '-r nul -d {} -Ochasen'.format(dic_path).replace('\\', '/'))


def ConvertProcess(File):
    InputFileName = os.path.abspath(File)
    OutputFileName = os.path.abspath(
        File).replace("_get_mecab.txt", "_convert_mecab.txt")
    with open(InputFileName, 'r', encoding='utf-8') as InputFile, open(OutputFileName, 'w', encoding='utf-8')as OutputFile:
        for line in InputFile.readlines():
            if line != "\n":
                reg = r'(.*?)\t(.*?)\t(.*?)'  # よっ	因る
                lineReg = re.search(reg, line)
                MecabResult = tagger.parse(
                    lineReg.group(1)).split("\t")[0]  # 使用Mecab测试剪贴板环境下的效果
                AnswerResult = lineReg.group(2)
                OutputFile.write(MecabResult+"\t"+AnswerResult+"\n")


def ProcessFiles():
    file = (i for i in FileNames)  # 迭代器数据类型
    for i in range(len(FileNames)):
        global FileNumber
        FileNumber = i
        ProcessFile = next(file)
        ConvertProcess(ProcessFile)
        Now = round((i / len(FileNames)) * 100)
        Done = '█' * int(Now)
        Undo = '_' * (100 - int(Now))
        print("\r{:^3.0f}%[{}->{}]".format(Now, Done, Undo), end='')
    Now = 100
    Done = '█' * int(Now)
    Undo = '_' * (100 - int(Now))
    print("\r{:^3.0f}%[{}->{}]".format(Now, Done, Undo), end='\n')


print("开始使用Mecab推导")
ProcessFiles()

EndTime = time.perf_counter()
print('Mecab推导耗时:%s毫秒' % (round((EndTime - StartTime)*1000, 3)))

os.system('python review_mecab.py')

import re
import MeCab
import os
import time
from pathlib import Path

'''
通过 Mecab 比较读音，进而判断结果是否一致
'''

StartTime = time.perf_counter()


path = os.getcwd()+r"\testfiles\test"+'\\'  # 加载测试文件
FileNames = list(Path(path).glob("**/*_convert_mecab.txt"))
dic_path = os.getcwd()+r'\unidic-cwj-3.1.1'+'\\'
tagger = MeCab.Tagger(
    '-r nul -d {} -Ochasen'.format(dic_path).replace('\\', '/'))


def GetYomi(InputText):  # 通过Mecab查询读音判读是否是同一个单词
    YomikateKata = tagger.parse(InputText).split("\t")[2]  # 返回推导结果的片假名
    YomikataHira = ConverHina2kata(YomikateKata)
    return YomikataHira


def ConverHina2kata(InputText):  # 转换片假名到平假名
    ProcessTexts = []
    for gana in InputText:
        if 12448 < int(ord(gana)) < 12543:  # 匹配片假名
            hira = chr(int(ord(gana) - 96))
            ProcessTexts.append(hira)
    OutputText = ''.join(ProcessTexts)
    return OutputText


def Process(File):
    InputFileName = os.path.abspath(File)
    OutputFileName = os.path.abspath(
        File).replace("_convert_mecab.txt", "_review_mecab.txt")
    with open(InputFileName, 'r', encoding='utf-8') as InputFile, open(OutputFileName, 'w', encoding='utf-8')as OutputFile:
        for line in InputFile.readlines():
            if line != "\n":
                reg = r'(.*?)\t(.*?)\n'  # よっ	因る
                lineReg = re.search(reg, line)
                Yomi_MecabResult = GetYomi(lineReg.group(1))
                AnswerResult = lineReg.group(2)
                Yomi_AnswerResult = GetYomi(AnswerResult)
                if Yomi_AnswerResult == Yomi_MecabResult:
                    OutputFile.write('True\t'+line)
                else:
                    OutputFile.write('Fasle\t'+line)


def ProcessFiles():
    file = (i for i in FileNames)  # 迭代器数据类型
    for i in range(len(FileNames)):
        global FileNumber
        FileNumber = i
        ProcessFile = next(file)
        Process(ProcessFile)
        Now = round((i / len(FileNames)) * 100)
        Done = '█' * int(Now)
        Undo = '_' * (100 - int(Now))
        print("\r{:^3.0f}%[{}->{}]".format(Now, Done, Undo), end='')
    Now = 100
    Done = '█' * int(Now)
    Undo = '_' * (100 - int(Now))
    print("\r{:^3.0f}%[{}->{}]".format(Now, Done, Undo), end='\n')


print("开始验证Mecab准确性")
ProcessFiles()

EndTime = time.perf_counter()
# os.system("test_coverage.py")
os.system("py review_coverage.py")

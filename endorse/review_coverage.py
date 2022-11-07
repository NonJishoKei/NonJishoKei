import re
import os
from pathlib import Path

'''
统计判断结果
'''

path = os.getcwd()+r"\testfiles\test"+'\\'  # 加载测试文件
NoJishoFileNames = list(Path(path).glob("**/*_review_nojishokei.txt"))
MecabFileNames = list(Path(path).glob("**/*_review_mecab.txt"))


MecabTruePercent = []
MecabFalsePercent = []


def MecabReviewProcess(File):
    reg = re.compile(r'(.*?)\t(.*?)\t(.*?)\n')
    InputFileName = os.path.abspath(File)
    with open(InputFileName, 'r', encoding='utf-8') as InputFile:
        for line in InputFile.readlines():
            if line != "\n":
                lineReg = re.search(reg, line)
                if "True" in lineReg.group(1):
                    MecabTruePercent.append(lineReg.group(1))
                else:
                    MecabFalsePercent.append(lineReg.group(1))
                Jishokei.add(lineReg.group(3))


NonJishoTruePercent = []
NonJishoFalsePercent = []


def NonJishoReviewProcess(File):
    reg = re.compile(r'(.*?)\t(.*?)\t(.*?)\n')
    InputFileName = os.path.abspath(File)
    with open(InputFileName, 'r', encoding='utf-8') as InputFile:
        for line in InputFile.readlines():
            if line != "\n":
                lineReg = re.search(reg, line)
                if "True" in lineReg.group(1):
                    NonJishoTruePercent.append(lineReg.group(1))
                else:
                    NonJishoFalsePercent.append(lineReg.group(1))
                Jishokei.add(lineReg.group(3))


def MecabProcessFiles(FileNames):
    global NonJishoKei, Jishokei
    NonJishoKei = set()
    Jishokei = set()
    file = (i for i in FileNames)  # 迭代器数据类型
    for i in range(len(FileNames)):
        global FileNumber, true, false
        true = 0
        false = 0
        FileNumber = i
        ProcessFile = next(file)
        MecabReviewProcess(ProcessFile)
        Now = round((i / len(FileNames)) * 100)
        Done = '█' * int(Now)
        Undo = '_' * (100 - int(Now))
        print("\r{:^3.0f}%[{}->{}]".format(Now, Done, Undo), end='')
    Now = 100
    Done = '█' * int(Now)
    Undo = '_' * (100 - int(Now))
    print("\r{:^3.0f}%[{}->{}]".format(Now, Done, Undo), end='\n')
    True_Percent = str(round(
        len(MecabTruePercent)/(len(MecabTruePercent)+len(MecabFalsePercent))*100, 3))+"%"
    return True_Percent


def NonJishoProcessFiles(FileNames):
    global NonJishoKei, Jishokei
    NonJishoKei = set()
    Jishokei = set()
    file = (i for i in FileNames)  # 迭代器数据类型
    for i in range(len(FileNames)):
        global FileNumber, true, false
        true = 0
        false = 0
        FileNumber = i
        ProcessFile = next(file)
        NonJishoReviewProcess(ProcessFile)
        Now = round((i / len(FileNames)) * 100)
        Done = '█' * int(Now)
        Undo = '_' * (100 - int(Now))
        print("\r{:^3.0f}%[{}->{}]".format(Now, Done, Undo), end='')
    Now = 100
    Done = '█' * int(Now)
    Undo = '_' * (100 - int(Now))
    print("\r{:^3.0f}%[{}->{}]".format(Now, Done, Undo), end='\n')
    True_Percent = str(round(
        len(NonJishoTruePercent)/(len(NonJishoTruePercent)+len(NonJishoFalsePercent))*100, 3))+"%"
    return True_Percent


print("计算准确度")
print("非辞書算法准确度："+NonJishoProcessFiles(NoJishoFileNames))
NoJishoKei_Cverage = str(len(NonJishoKei))
Jishokei_Coverage = str(len(Jishokei))
print("Mecab算法准确度："+MecabProcessFiles(MecabFileNames))
Jishokei_Coverage = str(len(Jishokei))
print("覆盖辞書形："+Jishokei_Coverage)

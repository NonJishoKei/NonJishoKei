import re
import MeCab
import os
from pathlib import Path
import MeCab

'''
请注意，该脚本只能由main.py从目录下调用，单独使用注意检查文件路径
'''


path = os.getcwd()+r"\testfiles\test"+'\\'  # 加载测试文件
FileNames = list(Path(path).glob("**/*_convert_nonjishokei.txt"))
dic_path = os.getcwd()+r'\unidic-cwj-3.1.1'+'\\'
tagger2 = MeCab.Tagger(
    '-r nul -d {} -Ochasen'.format(dic_path).replace('\\', '/'))


def GetYomi(InputText):  # 通过Mecab查询读音判读是否是同一个单词
    YomikateKata = tagger2.parse(InputText).split("\t")[2]  # 返回推导结果的片假名
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


def JudegHina(InputText):  # 判断是否全是平假名
    ProcessTexts = []
    for gana in InputText:
        if 12352 < int(ord(gana)) < 12449:  # 匹配平假名
            ProcessTexts.append(True)
        else:
            ProcessTexts.append(False)
    if all(ProcessTexts) == True:  # 判断是否全由平假名组成
        return True
    else:
        return False


def Process(File):
    InputFileName = os.path.abspath(File)
    OutputFileName = os.path.abspath(
        File).replace("_convert_nonjishokei.txt", "_review_nojishokei.txt")
    with open(InputFileName, 'r', encoding='utf-8') as InputFile, open(OutputFileName, 'w', encoding='utf-8')as OutputFile:
        for line in InputFile.readlines():
            reg = r'\[(.*?)\]\t(.*?)'  # [よる, よう, ]	よっ	因る
            lineReg = re.search(reg, line)
            MecabResult = lineReg.group(1)
            Yomi_MecabResult = GetYomi(MecabResult)
            NonJishoKeiList = lineReg.group(1).split(",")
            ResultList = []
            for NonJishoKeiResult in NonJishoKeiList:
                if JudegHina == True:
                    Yomi_NonJishoKeiResult = NonJishoKeiResult  # 复合动词通过Mecab返回的读音存在一定问题，故复合动词推导的结果
                else:
                    Yomi_NonJishoKeiResult = GetYomi(NonJishoKeiResult)
                if Yomi_NonJishoKeiResult == Yomi_MecabResult:
                    ResultList.append(True)
                else:
                    ResultList.append(False)
            if any(ResultList) == True:
                OutputFile.write('True\t'+line)
            else:
                OutputFile.write('Fasle\t'+line)
            '''测试不单独处理复合动词对结果影响

                Yomi_NonJishoKeiResult = GetYomi(NonJishoKeiResult)
                if Yomi_NonJishoKeiResult == Yomi_MecabResult:
                    ResultList.append(True)
                else:
                    ResultList.append(False)
            if any(ResultList) == True:
                OutputFile.write('True\t'+line)
            else:
                OutputFile.write('Fasle\t'+line)
                '''


def ProcessFiles():
    file = (i for i in FileNames)  # 迭代器数据类型
    for i in range(len(FileNames)):
        global FileNumber, true, false
        true = 0
        false = 0
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


print("开始验证非辞書准确性")
ProcessFiles()

os.system('python convert_mecab.py')

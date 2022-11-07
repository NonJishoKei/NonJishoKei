import MeCab
import os
from pathlib import Path

dic_path = os.getcwd()+r'\unidic-cwj-3.1.1'+'\\'
tagger = MeCab.Tagger(
    '-r nul -d {} -Ochasen'.format(dic_path).replace('\\', '/'))  # 调整 Mecab 输出格式
path = os.getcwd()+r"\testfiles\test"+'\\'  # 加载测试文件
FileNames = list(Path(path).glob("**/*_temp.txt"))  # 为测试文件添加统一的后缀名便于重复测试


def ConvertProcess(InputFile):
    InputFileName = os.path.abspath(InputFile)
    OutputMecabFileName = os.path.abspath(
        InputFile).replace(".txt", "_get_mecab.txt")
    OutputNonJishoFileName = os.path.abspath(
        InputFile).replace(".txt", "_get_nonjishokei.txt")
    with open(InputFileName, "r", encoding="utf-8", errors='ignore') as InputFile, open(OutputMecabFileName, "w", encoding="utf-8", errors='ignore') as SaveMecabFile, open(OutputNonJishoFileName, "w", encoding="utf-8") as SaveNonJishoFile:
        try:
            for line in InputFile:
                if line != "\n":
                    for line in line.split("。"):
                        result = tagger.parse(line).split("\n")  # 分析句子
                        for item in result:
                            if "感動詞-一般" in item:  # 跳过，
                                pass
                            elif "動詞-一般" in item:
                                if "意志推量形" in item:  # 调整分词结果 隠そう→隠そ
                                    SaveMecabFile.write(
                                        item.replace("EOS", "")+"\t"+"\n")  # +line
                                    SaveNonJishoFile.write(
                                        item[0:-1].replace("EOS", "")+"\t"+"\n")
                                else:
                                    SaveMecabFile.write(item.replace(
                                        "EOS", "")+"\t"+"\n")  # +line
                                    SaveNonJishoFile.write(
                                        item.replace("EOS", "")+"\t"+"\n")
                            elif "形容詞-一般" in item:
                                if "語幹-一般" in item:  # 分词结果不一致，无法调整
                                    pass
                                elif "形容詞	仮定形-一般" in item:
                                    SaveNonJishoFile.write(
                                        item[0:-1].replace("EOS", "")+"\t"+"\n")
                                    SaveMecabFile.write(
                                        item.replace("EOS", "")+"\t"+"\n")
                                elif "形容詞	連用形-促音便" in item:  # 形容词的かった活用结果不一致
                                    SaveNonJishoFile.write(
                                        item[0:-1].replace("EOS", "")+"\t"+"\n")
                                    SaveMecabFile.write(
                                        item.replace("EOS", "")+"\t"+"\n")
                                else:
                                    SaveNonJishoFile.write(
                                        item.replace("EOS", "")+"\t"+"\n")
                                    SaveMecabFile.write(
                                        item.replace("EOS", "")+"\t"+"\n")
        except UnicodeDecodeError:  # 维基百科语料中含有部分特殊符号
            print("编码错误")


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


print("开始转换语料")
ProcessFiles()

os.system('py convert_nonjishkei.py')

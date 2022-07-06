# 提取拟声拟态词，词头可以利用GoldenDic生成并导出
import os

# 获取当前工作目录，打开工作目录下的txt文件
file = '..\待处理.txt'
file_for_save = "..\目标.txt"  # 此处是生成的文件的名字和路径
Error_Lines_Save = "..\异常.txt"  # 若出现异常，异常行保存的文件的位置

with open(file,
          'r', encoding='UTF-8') as f, open(file_for_save,
                                            'w',
                                            encoding='utf-8') as f2, open(
                                                Error_Lines_Save,
                                                'w',
                                                encoding='utf-8') as f3:
    for line in f:
        kana = line[-2]
        if kana == 'う':
            line = line[0:-2] + line[-2].replace("う", "わ" + '\n')
            f2.write(line)
        elif kana == 'く':
            line = line[0:-2] + line[-2].replace("く", 'か' + '\n')
            f2.write(line)
        elif kana == 'ぐ':
            line = line[0:-2] + line[-2].replace("ぐ", 'が' + '\n')
            f2.write(line)
        elif kana == 'す':
            line = line[0:-2] + line[-2].replace("す", 'さ' + '\n')
            f2.write(line)
        elif kana == 'ず':
            line = line[0:-2] + line[-2].replace("ず", 'ざ' + '\n')
            f2.write(line)
        elif kana == 'つ':
            line = line[0:-2] + line[-2].replace("つ", 'た' + '\n')
            f2.write(line)
        elif kana == 'づ':
            line = line[0:-2] + line[-2].replace("づ", 'だ' + '\n')
            f2.write(line)
        elif kana == 'ぬ':
            line = line[0:-2] + line[-2].replace("ぬ", 'な' + '\n')
            f2.write(line)
        elif kana == 'ふ':
            line = line[0:-2] + line[-2].replace("ふ", 'は' + '\n')
            f2.write(line)
        elif kana == 'ぶ':
            line = line[0:-2] + line[-2].replace("ぶ", 'ば' + '\n')
            f2.write(line)
        elif kana == 'ぷ':
            line = line[0:-2] + line[-2].replace("ぷ", 'ぱ' + '\n')
            f2.write(line)
        elif kana == 'む':
            line = line[0:-2] + line[-2].replace("む", 'ま' + '\n')
            f2.write(line)
        elif kana == 'る':
            line = line[0:-2] + line[-2].replace("る", 'ら' + '\n')
            f2.write(line)
        else:
            f2.write(line)

from typing import Text
from openccpy.opencc import *
import re
import os

'''
请注意，使用这种方法并不能完全得到所有对应的日文汉字，如果你有更好的方法，欢迎发送邮件到NoHeartPen@outlook.com与我交流
'''

# 获取当前工作目录，打开工作目录下的txt文件
file = os.getcwd() + '/待处理.txt'
file_for_save = os.getcwd() + "/目标.txt"  # 此处是生成的文件的名字和路径
Error_Lines_Save = os.getcwd() + "/异常.txt"  # 若出现异常，异常行保存的文件的位置


def convert(jas):
    jas_kanji = list(jas.group())
    zns = []
    for i in jas_kanji:
        zn = Opencc.to_simple(i)
        print(zn)
        zns.append(zn)
    print(zns)
    return zns


with open(file,
          'r', encoding='UTF-8') as file, open(file_done,
                                               'w',
                                               encoding='UTF-8') as file_done:
    for line in file:
        pattern = re.compile('(.*?)\t')
        result = pattern.match(line)
        if result:
            new_line = str(convert(result)) + "\n"
            file_done.write(new_line)
        else:
            file_done.write(line + "\n")

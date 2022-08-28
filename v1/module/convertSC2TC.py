from typing import Text
from openccpy.opencc import *
import re

'''
请注意，使用这种方法并不能完全得到所有对应的日文汉字，如果你有更好的方法，欢迎发送邮件到NoHeartPen@outlook.com与我交流
'''


file = r'..\temp.txt'# 获取当前工作目录，打开工作目录下的txt文件
file_for_save = r'..\save.txt'  # 此处是生成的文件的名字和路径


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
          'r', encoding='UTF-8') as file, open(file_for_save,
                                               'w',
                                               encoding='UTF-8') as file_done:
    for line in file:
        pattern = re.compile('(.*?)\t')
        result = pattern.match(line)
        if result:
            new_line = str(convert(result)) + '\n'
            file_done.write(new_line)
        else:
            file_done.write(line + '\n')

#
import os
import re

# 获取当前工作目录，打开工作目录下的txt文件
file = os.getcwd() + '\待处理.txt'
file_for_save = os.getcwd() + "\目标.txt"  #此处是生成的文件的名字和路径
Error_Lines_Save = os.getcwd() + "\异常.txt"  #若出现异常，异常行保存的文件的位置

with open(file,
          'r', encoding='UTF-8') as f, open(file_for_save,
                                            'w',
                                            encoding='utf-8') as f2, open(
                                                Error_Lines_Save,
                                                'w',
                                                encoding='utf-8') as f3:
    for line in f:
        if 'い\t' in line:
            f2.write(line)

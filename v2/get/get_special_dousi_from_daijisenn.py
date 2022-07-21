'''
处理提取的词条，拆分植（え）付ける这样可以灵活书写的词条为植え付ける和植付ける
'''

from dataclasses import replace
from msilib.schema import Error
import os
import re

ProessPath = os.getcwd()

InputFile = r'temp.txt'
OutputFile = r'save.txt'

with open(InputFile,
          'r', encoding='UTF-8') as f, open(OutputFile,
                                            'w',
                                            encoding='utf-8') as f2:
    for line in f:
        if '（' in line :
            line_first = line.replace('（','')
            line_first =  line_first.replace('）','')
            f2.write(line_first)
            regex = r'（(.*?)）'
            line_second = re.sub(regex,'',line)
            f2.write(line_second)
        else:
            f2.write(line)
            

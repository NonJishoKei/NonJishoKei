import os
import re
'''
请注意，这是从GetDict导出的txt源文件中提取词典的解释项，也就是没有@@@跳转的项目
'''

# 获取当前工作目录，打开工作目录下的txt文件
file = os.getcwd() + '/待处理.txt'
file_for_save = os.getcwd() + "/目标.txt"  # 此处是生成的文件的名字和路径
Error_Lines_Save = os.getcwd() + "/异常.txt"  # 若出现异常，异常行保存的文件的位置

with open(file,
          'r', encoding='UTF-8') as f, open(file_for_save,
                                            'w',
                                            encoding='utf-8') as f2, open(
                                                file_for_save,
                                                'w',
                                                encoding='utf-8') as f3:
    pattern = re.compile('([^\t]*?)\t@@@LINK=(.*?)$')
    for line in f:
        result = pattern.match(line)
        if result:
            continue
        else:
            f2.write(line)

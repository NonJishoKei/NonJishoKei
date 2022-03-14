import re


# 获取当前工作目录，打开工作目录下的txt文件
file = '..\待处理.txt'
file_for_save = "..\目标.txt"  # 此处是生成的文件的名字和路径
Error_Lines_Save = "..\异常.txt"  # 若出现异常，异常行保存的文件的位置

with open(file, 'r', encoding='UTF-8') as f, open(file_for_save, 'w', encoding='utf-8') as f2, open(file_for_save, 'w', encoding='utf-8') as f3:
    pattern = re.compile('([^\t]*?)\t@@@LINK=(.*?)$')
    for line in f:
        result = pattern.match(line)
        if result:
            f2.write(line)
        else:
            # 匹配不成功，说明是“单词 解释“行，跳过，直接输出
            continue

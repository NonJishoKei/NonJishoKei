'''
提取处理形容词的变形，目前为止发现的变形有如下六种：

さ（名词）
し（古语名词）
く（副词）
か（った，过去）
け（れば）
み（名词，部分形容词有）

如果你发现了遗漏的，可发送邮件到：NoHeartPen@outlook.com，也欢迎与我讨论其他相关问题

'''

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
        line = line[0:-2] + line[-2].replace("い", "み" + '\n')
        f2.write(line)

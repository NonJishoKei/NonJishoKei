'''
请注意，这个脚本还有待完善，另外，这个文件操作的是由GetDict导出的源文件，不是GoldeDic导出的词条
'''

# 获取当前工作目录，打开工作目录下的txt文件
file = '..\待处理.txt'
file_for_save = "..\目标.txt"  # 此处是生成的文件的名字和路径
Error_Lines_Save = "..\异常.txt"  # 若出现异常，异常行保存的文件的位置

with open(file,
          'r', encoding='UTF-8') as file, open(file_for_save,
                                               'w',
                                               encoding='UTF-8') as file_done:
    for line in file:
        if '<a name="HATSUON" id="HATSUON"></a>' in line:
            file_done.write(line)
        else:
            continue

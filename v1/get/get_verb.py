# 提取所有动词
# 获取当前工作目录，打开工作目录下的txt文件
file = '..\待处理.txt'
file_for_save = "..\目标.txt"  # 此处是生成的文件的名字和路径
Error_Lines_Save = "..\异常.txt"  # 若出现异常，异常行保存的文件的位置

with open(file, 'r', encoding='UTF-8') as f, open(file_for_save, 'w', encoding='utf-8') as f2, open(Error_Lines_Save, 'w', encoding='utf-8') as f3:
    for line in f:
        if '】' in line:
            continue
        elif 'う\n' in line:
            f2.write(line)
        elif 'く\n' in line:
            f2.write(line)
        elif 'ぐ\n' in line:
            f2.write(line)
        elif 'す\n' in line:
            f2.write(line)
        elif 'ず\n' in line:
            f2.write(line)
        elif 'つ\n' in line:
            f2.write(line)
        elif 'づ\n' in line:
            f2.write(line)
        elif 'ぬ\n' in line:
            f2.write(line)
        elif 'ふ\n' in line:
            f2.write(line)
        elif 'ぶ\n' in line:
            f2.write(line)
        elif 'ぷ\n' in line:
            f2.write(line)
        elif 'む\n' in line:
            f2.write(line)
        elif 'ゆ\n' in line:
            f2.write(line)
        elif 'る\n' in line:
            f2.write(line)
# 处理那些连二音变特殊的动词

file = '..\temp.txt'# 获取当前工作目录，打开工作目录下的txt文件
file_for_save = '..\save.txt'  # 此处是生成的文件的名字和路径

with open(file,
          'r', encoding='UTF-8') as f, open(file_for_save,
                                            'w',
                                            encoding='utf-8') as f2:
    for line in f:
        kana = line[-2]
        if kana == 'う':
            line = line[0:-2] + line[-2].replace('う', 'っ' + '\n')
            f2.write(line)
        elif kana == 'く':
            line = line[0:-2] + line[-2].replace('く', 'い' + '\n')
            f2.write(line)
        elif kana == 'ぐ':
            line = line[0:-2] + line[-2].replace('ぐ', 'い' + '\n')
            f2.write(line)
        elif kana == 'す':
            f2.write(line)  # し
        elif kana == 'ず':
            f2.write(line)  # 有这样的动词么？
        elif kana == 'つ':
            line = line[0:-2] + line[-2].replace('つ', 'っ' + '\n')
            f2.write(line)
        elif kana == 'づ':
            line = line[0:-2] + line[-2].replace('づ',
                                                 'っ' + '\n')  # 不管了，就按照つ来处理吧
            f2.write(line)
        elif kana == 'ぬ':
            line = line[0:-2] + line[-2].replace('ぬ', 'ん' + '\n')
            f2.write(line)
        elif kana == 'ふ':
            f2.write(line)  # 好像没有这样的动词吧
        elif kana == 'ぶ':
            line = line[0:-2] + line[-2].replace('ぶ', 'ん' + '\n')
            f2.write(line)
        elif kana == 'ぷ':
            f2.write(line)  # 好像没有这样的动词吧
        elif kana == 'む':
            line = line[0:-2] + line[-2].replace('む', 'ん' + '\n')
            f2.write(line)
        elif kana == 'る':
            line = line[0:-2] + line[-2].replace('る', 'っ' + '\n')
            f2.write(line)
        else:
            f2.write(line)

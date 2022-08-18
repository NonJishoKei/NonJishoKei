import os

'''
删除不是以假名结尾的词条，同时清除重复的单词，使用前注意手动修改文件名为temp.txt
'''

##ProcessPath = os.chdir('..')

with open(r'temp.txt', 'r', encoding='utf-8') as f, open(r'save.txt', 'w', encoding='utf-8')as s:
    for line in f:
        if line != '\n\n': # 跳过空行
            line = line.replace('\n', '')
            if 12353 < ord(line[-1]) < 12435:
                s.write(line+'\n') # 只保留以假名结尾的词条
            else:
                continue
        else:
            print(line)

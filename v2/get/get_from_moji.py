import os
import re

ProcessPath = os.getcwd()

with open(r'temp.txt', 'r', encoding='utf-8') as f, open(r'save.txt', 'w', encoding='utf-8') as s:
    InputFileList = f.readlines()
    for line in InputFileList:
        if '@@@LINK=' in line :
            continue
        elif re.search(r'class="cixing_title">(.*?)</div>', line):  # 查找词性标签 哎，不搞了，太费力了，直接借助v3的规律来吧
            regex = r'^(.*?)\t(.*?)class="cixing_title">(.*?)</div>(.*?)$'
            replacement = r'\1'+'\t'+r'\3'+'\n'
            line = re.sub(regex, replacement, line)
            s.write(line)
        else:
            continue
        '''
            if '】（' in line:
                continue
            else:
                regex = r'^(.*?)】\t(.*?)$'
                replacement = r'\1'+'\n'
                line = re.sub(regex, replacement, line)
                s.write(line)'''
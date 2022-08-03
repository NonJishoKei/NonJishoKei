'''
检查输入的内容中是否有假名注音的语法()，通过正则提取真正需要查找的部分
测试用例“
食(た)べる
魂(こん)不(ふ)守(しゅ)舎(しゃ)
'''

import re


InputText = '食(た)べる'

def DelRuby(ProcessText):
    reg = r'\((.*?)\)'
    replacement = r''
    OutputText = re.sub(reg,replacement,ProcessText)
    return OutputText

print(DelRuby(InputText))

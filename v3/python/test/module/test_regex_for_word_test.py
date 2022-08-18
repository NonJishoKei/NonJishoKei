'''
检查输入的内容中是否有假名注音的语法()，通过正则提取真正需要查找的部分
测试用例“
食(た)べる
魂(こん)不(ふ)守(しゅ)舎(しゃ)
'''

import re
import time

StartTime = time.perf_counter()
InputText = 'ご飯を食(たな)べた'
def DelWordRuby(ProcessText):
    reg = r'\([\u3040-\u309f]*?\)'# 参考Unicode码值，只匹配平假名
    replacement = r''
    OutputText = re.sub(reg,replacement,ProcessText)
    return OutputText

if '(' in InputText:
    InpuText = DelWordRuby(InputText)

print(InpuText)
EndTime = time.perf_counter()
print('耗时:%s毫秒' % (round((EndTime - StartTime)*1000, 3)))
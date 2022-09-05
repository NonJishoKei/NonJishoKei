'''
自动转换那些日语独有的标记，本项目参考了一份来自日本文化厅的文件
々〻（汉字重复标记，后者主要用于手写，但考虑到OCR等场景，算作一类）例子：度々、度〻、明々白々
ゝゞヽヾ（假名的重复标记，多见于比较老的文章）例子：こゝろ、ほヾ
〳〵／＼（前者是Unicode编码，后者来自青空文库）例子：いよ〳〵、しげ／＼（注意这种字符串的\通过pyperclip传递时不会被转义）
〴〵／″＼（前者是Unicode编码，后者来自青空文库）例子：しみ〴〵、しみ／″＼
'''
import re
import time
import pyperclip

StartTime = time.perf_counter()
InputText = pyperclip.paste()


def ConverRepeSingleSign(InputText):
    # 这些符号只代表一个假名或者汉字，注意ゝヽ不一定出现在单词的结尾部分，例如：やがて再び唇をわなゝかした
    reg = r'(\w{1})(々|〻|ゝ|ヽ)'
    OutputText = re.sub(reg, r'\1\1', InputText)
    return OutputText


def ConverRepeSingleDakuSign(InputText):
    reg = r'^(.*?)(\w{1})(ヾ|ゞ)(.*?)$'
    ProcessText = re.match(reg, InputText)
    OutputText = ProcessText.group(
        1)+ProcessText.group(2)+chr(int(ord(ProcessText.group(2)))+1)+ProcessText.group(4)
    return OutputText


def ConverRepeDoubleSign(InputText):
    reg = r'^(\w{2})(〳〵|／＼)(.*?)$'  # 这些符号代表2个假名或者汉字
    OutputText = re.sub(reg, r'\1\1\3', InputText)
    return OutputText


def ConverRepeDoubleDakuSign(InputText):
    ProcessText = re.match(r'^(.*?)(〴〵|／″＼)(.*?)$', InputText)
    if re.search(r'[^\u3040-\u30ff]', ProcessText.group(1)) != None:  # 注意：代わる〴〵
        print('now')
        reg = r'^(.*?)(〴〵|／″＼)(.*?)$'
        OutputText = re.sub(reg, r'\1\1\3', InputText)
    else:
        reg = r'^(\w{1})(\w{1})(〴〵|／″＼)$'  # 第一个分组是需要浊化的假名，第二个分组不需要处理
        sub = r'\1\2'
        ProcessText = re.match(reg, InputText)
        OutputText = ProcessText.group(
            1)+ProcessText.group(2)+chr(int(ord(ProcessText.group(2)))+1)
        ProcessText = re.sub(reg, sub, InputText)
        OutputText = ProcessText + \
            chr(int(ord(ProcessText[0]))+1)+ProcessText[1]
    return OutputText


if re.search(r'(\w{1})(々|〻|ゝ|ヽ)', InputText) != None:
    print(ConverRepeSingleSign(InputText))

if re.search(r'^(.*?)(\w{1})(ヾ|ゞ)(.*?)$', InputText) != None:
    print(ConverRepeSingleDakuSign(InputText))

if re.search(r'^(\w{2})(〳〵|／＼)(.*?)$', InputText) != None:
    print(ConverRepeDoubleSign(InputText))

if re.search(r'^(.*?)(〴〵|／″＼)(.*?)$', InputText) != None:
    print(ConverRepeDoubleDakuSign(InputText))

EndTime = time.perf_counter()
print('耗时:%s毫秒' % (round((EndTime - StartTime)*1000, 3)))

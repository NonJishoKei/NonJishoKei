# 提取拟声拟态词，词头可以利用GoldenDic生成并导出

def format_list2str(list_element):
    list_element = str(list_element)
    list_element = list_element.replace(",", "")
    list_element = list_element.replace("[", "")
    list_element = list_element.replace("]", "")
    str_element = list_element.replace("'", "")
    return str_element


# 日文假名转换
def hiragara_katakana(hiragara_word):
    katakana_word = []
    word_list = list(hiragara_word)
    for hiragara in word_list:
        katakana_code = int(ord(hiragara))
        if 12352 < katakana_code < 12438:
            katakana = chr(katakana_code + 96)
        else:
            katakana = hiragara
        katakana_word.append(katakana)
    return katakana_word


InputFile = r'temp.md'
OutpurFile = r'save.md'

OutpurFileContext = []
with open(InputFile,encoding="UTF-8") as f:
    for line in f:
        line = hiragara_katakana(line)
        line = format_list2str(line)
        #f2.write(str(line.replace(' ', '')) + '\n')
with open(OutpurFile,'w',encoding='UTF-8') as s:
    for i in OutpurFileContext:
        s.writelines(i)
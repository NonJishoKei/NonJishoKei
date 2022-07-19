'''
提取所有平假名词头
'''


# 格式化列表
def format_list2str(list_element):
    list_element = str(list_element)
    list_element = list_element.replace(",", "")
    list_element = list_element.replace("[", "")
    list_element = list_element.replace("]", "")
    str_element = list_element.replace("'", "")
    return str_element


# 日文纯假名词头提取
def getgara_word(word):
    gara_word = []
    word_list = list(word)
    for gara in word_list:
        gara_code = int(ord(gara))
        if 12352 < gara_code < 12438:
            gara = chr(gara_code)
        else:
            gara = gara+'@@@@@@@@'
        gara_word.append(gara)
    return gara_word

InputFile = r'temp.md'
OutpurFile = r'save.md'

OutpurFileContext = []
with open(InputFile,encoding="UTF-8") as f:
    for line in f:
        line = getgara_word(line)
        line = format_list2str(line)
        OutpurFileContext.append(line.replace(" ",'')+'\n')
with open(OutpurFile,'w',encoding='UTF-8') as s:
    for i in OutpurFileContext:
        s.writelines(i)

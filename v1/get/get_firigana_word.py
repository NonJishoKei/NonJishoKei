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
            continue
        gara_word.append(gara)
    return gara_word


# 获取当前工作目录，打开工作目录下的txt文件
file = '..\待处理.txt'
file_for_save = "..\目标.txt"  # 此处是生成的文件的名字和路径
Error_Lines_Save = "..\异常.txt"  # 若出现异常，异常行保存的文件的位置

with open(file,
          'r', encoding='UTF-8') as f, open(file_for_save,
                                            'w',
                                            encoding='utf-8') as f2, open(
                                                Error_Lines_Save,
                                                'w',
                                                encoding='utf-8') as f3:
    for line in f:
        line = getgara_word(line)
        line = format_list2str(line)
        f2.write(str(line.replace(' ', '')) + '\n')

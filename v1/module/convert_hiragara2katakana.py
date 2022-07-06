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
        line = hiragara_katakana(line)
        line = format_list2str(line)
        f2.write(str(line.replace(' ', '')) + '\n')

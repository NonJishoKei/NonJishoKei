import os

ProessPath = os.getcwd()

InputFile = r'temp.txt'
OutputFile = r'save.txt'


with open(InputFile,
          'r', encoding='UTF-8') as f, open(OutputFile,
                                            'w',
                                            encoding='utf-8') as f2:
    for line in f:
        kana = line[-2]
        line = line.replace('（', '')
        line = line.replace('）', '')
        dichtml = r'<section class="description"><a href="entry://' + \
            line.replace('\n', '')+r'#description">' + \
            line.replace('\n', '')+'</a>\n</section>\n</>'+'\n'

        line_1 = line[0:-2] + line[-2].replace("る", "ろ" + '\n')+dichtml
        line_2 = line[0:-2] + line[-2].replace("る", "よ" + '\n')+dichtml
        line_3 = line[0:-2] + line[-2].replace("る", "な" + '\n')+dichtml
        line_4 = line[0:-2] + line[-2].replace("る", "ま" + '\n')+dichtml
        line_5 = line[0:-2] + line[-2].replace("る", "た" + '\n')+dichtml
        line_6 = line[0:-2] + line[-2].replace("る", "れ" + '\n')+dichtml
        line_7 = line[0:-2] + line[-2].replace("る", "て" + '\n')+dichtml
        line_8 = line[0:-2] + line[-2].replace("る", "ら" + '\n')+dichtml
        line_9 = line[0:-2] + line[-2].replace("る", "さ" + '\n')+dichtml
        line_10 = line[0:-2] + line[-2].replace("る", "ず" + '\n')+dichtml
        line_11 = line[0:-2] + line[-2].replace("る", "ぬ" + '\n')+dichtml
        line_12 = line[0:-2] + line[-2].replace("る", "、" + '\n')+dichtml
        line_13 = line[0:-2] + '\n'+dichtml # 部分合成词无法通过
        line_14 = line[0:-2] + line[-2].replace("る", "ん" + '\n')+dichtml
        f2.write(line_1+line_2+line_3+line_4+line_5+line_6 +
                 line_7+line_8+line_9+line_10+line_11+line_12+line_13+line_14)

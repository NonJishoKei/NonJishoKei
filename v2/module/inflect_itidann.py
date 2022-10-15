import os

ProessPath = os.getcwd()

InputFile = r'temp.txt'
OutputFile = r'save.txt'


def InflectItidan():
    with open(r"index\itidann.txt",
              'r', encoding='UTF-8') as InputFile, open(r"process\itidann.txt",
                                                        'w',
                                                        encoding='utf-8') as OutputFile:
        for line in InputFile:
            if line == "":
                line = line.replace('\n', '')
                dichtml = r'<section class="description"><a href="entry://' + \
                    line+r'#description">' + \
                    line+'</a>\n</section>\n</>'+'\n'

                line_1 = line[0:-1] + line[-1].replace("る", "ろ" + '\n')+dichtml
                line_2 = line[0:-1] + line[-1].replace("る", "よ" + '\n')+dichtml
                line_3 = line[0:-1] + \
                    line[-1].replace("る", "な" + '\n')+dichtml  # ながら
                line_4 = line[0:-1] + \
                    line[-1].replace("る", "ま" + '\n')+dichtml  # 敬体
                line_5 = line[0:-1] + \
                    line[-1].replace("る", "た" + '\n')+dichtml  # 简体过去
                line_6 = line[0:-1] + \
                    line[-1].replace("る", "れ" + '\n')+dichtml  # 假定れば
                line_7 = line[0:-1] + \
                    line[-1].replace("る", "て" + '\n')+dichtml  # ている
                line_8 = line[0:-1] + \
                    line[-1].replace("る", "ら" + '\n')+dichtml  # 否定
                line_9 = line[0:-1] + \
                    line[-1].replace("る", "さ" + '\n')+dichtml  # 使役态
                line_10 = line[0:-1] + \
                    line[-1].replace("る", "ず" + '\n')+dichtml  # 古语否定，现代残留
                line_11 = line[0:-1] + \
                    line[-1].replace("る", "ぬ" + '\n')+dichtml  # 古语否定，现代残留
                line_12 = line[0:-1] + \
                    line[-1].replace("る", "、" + '\n')+dichtml
                line_13 = line[0:-1] + '\n'+dichtml  # 部分合成词无法通过
                line_14 = line[0:-1] + \
                    line[-1].replace("る", "ん" + '\n')+dichtml  # 口语否定
                line_15 = line[0:-1] + \
                    line[-1].replace("る", "と" + '\n')+dichtml  # 口语ておく
                line_16 = line[0:-1] + \
                    line[-1].replace("る", "ち" + '\n')+dichtml  # 口语 てしまう
                line_17 = line[0:-1] + \
                    line[-1].replace("る", "ちゃ" + '\n')+dichtml  # 同上，划词
                OutputFile.write(line_1+line_2+line_3+line_4+line_5+line_6 +
                                 line_7+line_8+line_9+line_10+line_11+line_12+line_13+line_14+line_15+line_16+line_17)


InflectItidan()

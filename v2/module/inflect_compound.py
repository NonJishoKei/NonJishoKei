import re


def InflectGodanCompound():
    with open(r"index\godann_compound.txt",
              'r', encoding='UTF-8') as InputFile, open(r"process\godann_compound.txt",
                                                        'w',
                                                        encoding='utf-8') as OutputFile:
        for line in InputFile:
            line = line.replace('\n', '')
            if line != "":
                Regex = re.compile(r"^(.*?)\t(.*?)$")
                line = re.search(Regex, line)
                kana = line.group(1)[-1]  # 请注意，这种方法要求文件以空行结尾
                dichtml = r'<section class="description"><a href="entry://' + \
                    line.group(2).replace('\n', '')+r'#description">' + \
                    line.group(2).replace('\n', '') + \
                    '</a>\n</section>\n</>'+'\n'
                OutputFile.write(line.group(1)+"\n"+dichtml)  # 异形词跳转
                if kana == 'う':
                    line_1 = line.group(1)[0:-1] + \
                        line.group(1)[-1].replace("う", "わ" + '\n')+dichtml
                    line_2 = line.group(1)[0:-1] + \
                        line.group(1)[-1].replace("う", "お" + '\n')+dichtml
                    line_3 = line.group(1)[0:-1] + \
                        line.group(1)[-1].replace("う", "い" + '\n')+dichtml
                    line_4 = line.group(1)[0:-1] + \
                        line.group(1)[-1].replace("う", "っ" + '\n')+dichtml
                    line_5 = line.group(1)[0:-1] + \
                        line.group(1)[-1].replace("う", "え" + '\n')+dichtml
                    OutputFile.write(line_1+line_2+line_3+line_4+line_5)
                elif kana == 'く':
                    line_1 = line.group(1)[0:-1] + \
                        line.group(1)[-1].replace("く", 'か' + '\n')+dichtml
                    line_2 = line.group(1)[0:-1] + \
                        line.group(1)[-1].replace("く", 'こ' + '\n')+dichtml
                    line_3 = line.group(1)[0:-1] + \
                        line.group(1)[-1].replace("く", 'き' + '\n')+dichtml
                    line_4 = line.group(1)[0:-1] + \
                        line.group(1)[-1].replace("く", 'い' + '\n')+dichtml
                    line_5 = line.group(1)[0:-1] + \
                        line.group(1)[-1].replace("く", 'け' + '\n')+dichtml
                    OutputFile.write(line_1+line_2+line_3+line_4+line_5)
                elif kana == 'ぐ':
                    line_1 = line.group(1)[0:-1] + \
                        line.group(1)[-1].replace("ぐ", 'が' + '\n')+dichtml
                    line_2 = line.group(1)[0:-1] + \
                        line.group(1)[-1].replace("ぐ", 'ぎ' + '\n')+dichtml
                    line_3 = line.group(1)[0:-1] + \
                        line.group(1)[-1].replace("ぐ", 'げ' + '\n')+dichtml
                    line_4 = line.group(1)[0:-1] + \
                        line.group(1)[-1].replace("ぐ", 'ご' + '\n')+dichtml
                    line_5 = line.group(1)[0:-1] + \
                        line.group(1)[-1].replace("ぐ", 'い' + '\n')+dichtml
                    OutputFile.write(line_1+line_2+line_3+line_4+line_5)
                elif kana == 'す':
                    line_1 = line.group(1)[0:-1] + \
                        line.group(1)[-1].replace("す", 'さ' + '\n')+dichtml
                    line_2 = line.group(1)[0:-1] + \
                        line.group(1)[-1].replace("す", 'し' + '\n')+dichtml
                    line_3 = line.group(1)[0:-1] + \
                        line.group(1)[-1].replace("す", 'せ' + '\n')+dichtml
                    line_4 = line.group(1)[0:-1] + \
                        line.group(1)[-1].replace("す", 'そ' + '\n')+dichtml
                    OutputFile.write(line_1+line_2+line_3+line_4)
                elif kana == 'ず':
                    print(line)  # 没有的啦
                elif kana == 'つ':
                    line_1 = line.group(1)[0:-1] + \
                        line.group(1)[-1].replace("つ", 'た' + '\n')+dichtml
                    line_2 = line.group(1)[0:-1] + \
                        line.group(1)[-1].replace("つ", 'ち' + '\n')+dichtml
                    line_3 = line.group(1)[0:-1] + \
                        line.group(1)[-1].replace("つ", 'て' + '\n')+dichtml
                    line_4 = line.group(1)[0:-1] + \
                        line.group(1)[-1].replace("つ", 'と' + '\n')+dichtml
                    line_5 = line.group(1)[0:-1] + \
                        line.group(1)[-1].replace("つ", 'っ' + '\n')+dichtml
                    OutputFile.write(line_1+line_2+line_3+line_4+line_5)
                elif kana == 'づ':
                    print(line)  # 没有的啦
                elif kana == 'ぬ':
                    line_1 = line.group(1)[0:-1] + \
                        line.group(1)[-1].replace("ぬ", 'な' + '\n')+dichtml
                    line_2 = line.group(1)[0:-1] + \
                        line.group(1)[-1].replace("ぬ", 'に' + '\n')+dichtml
                    line_3 = line.group(1)[0:-1] + \
                        line.group(1)[-1].replace("ぬ", 'ね' + '\n')+dichtml
                    line_4 = line.group(1)[0:-1] + \
                        line.group(1)[-1].replace("ぬ", 'の' + '\n')+dichtml
                    line_5 = line.group(1)[0:-1] + \
                        line.group(1)[-1].replace("ぬ", 'ん' + '\n')+dichtml
                    OutputFile.write(line_1+line_2+line_3+line_4+line_5)
                elif kana == 'ふ':
                    print(line)  # 古语中才会出现
                elif kana == 'ぶ':
                    line_1 = line.group(1)[0:-1] + \
                        line.group(1)[-1].replace("ぶ", 'ば' + '\n')+dichtml
                    line_2 = line.group(1)[0:-1] + \
                        line.group(1)[-1].replace("ぶ", 'び' + '\n')+dichtml
                    line_3 = line.group(1)[0:-1] + \
                        line.group(1)[-1].replace("ぶ", 'べ' + '\n')+dichtml
                    line_4 = line.group(1)[0:-1] + \
                        line.group(1)[-1].replace("ぶ", 'ぼ' + '\n')+dichtml
                    line_5 = line.group(1)[0:-1] + \
                        line.group(1)[-1].replace("ぶ", 'ん' + '\n')+dichtml
                    OutputFile.write(line_1+line_2+line_3+line_4+line_5)
                elif kana == 'ぷ':
                    print(line)
                elif kana == 'む':
                    line_1 = line.group(1)[0:-1] + \
                        line.group(1)[-1].replace("む", 'ま' + '\n')+dichtml
                    line_2 = line.group(1)[0:-1] + \
                        line.group(1)[-1].replace("む", 'み' + '\n')+dichtml
                    line_3 = line.group(1)[0:-1] + \
                        line.group(1)[-1].replace("む", 'め' + '\n')+dichtml
                    line_4 = line.group(1)[0:-1] + \
                        line.group(1)[-1].replace("む", 'も' + '\n')+dichtml
                    line_5 = line.group(1)[0:-1] + \
                        line.group(1)[-1].replace("む", 'ん' + '\n')+dichtml
                    OutputFile.write(line_1+line_2+line_3+line_4+line_5)
                elif kana == 'る':
                    line_1 = line.group(1)[0:-1] + \
                        line.group(1)[-1].replace("る", 'ら' + '\n')+dichtml
                    line_2 = line.group(1)[0:-1] + \
                        line.group(1)[-1].replace("る", 'り' + '\n')+dichtml
                    line_3 = line.group(1)[0:-1] + \
                        line.group(1)[-1].replace("る", 'れ' + '\n')+dichtml
                    line_4 = line.group(1)[0:-1] + \
                        line.group(1)[-1].replace("る", 'ろ' + '\n')+dichtml
                    line_5 = line.group(1)[0:-1] + \
                        line.group(1)[-1].replace("る", 'っ' + '\n')+dichtml
                    OutputFile.write(line_1+line_2+line_3+line_4+line_5)
                else:
                    print(line)
        print("五段复合动词异形词处理完成！")


def InflectItidanCompound():
    with open(r"index\itidann_compound.txt",
              'r', encoding='UTF-8') as InputFile, open(r"process\itidann_compound.txt",
                                                        'w',
                                                        encoding='utf-8') as OutputFile:
        for line in InputFile:
            line = line.replace('\n', '')
            if line != "":
                Regex = re.compile(r"^(.*?)\t(.*?)$")
                line = re.search(Regex, line)
                dichtml = r'<section class="description"><a href="entry://' + \
                    line.group(2).replace('\n', '')+r'#description">' + \
                    line.group(2).replace('\n', '') + \
                    '</a>\n</section>\n</>'+'\n'

                line_1 = line.group(
                    1)[0:-1] + line.group(1)[-1].replace("る", "ろ" + '\n')+dichtml
                line_2 = line.group(
                    1)[0:-1] + line.group(1)[-1].replace("る", "よ" + '\n')+dichtml
                line_3 = line.group(1)[0:-1] + \
                    line.group(1)[-1].replace("る", "な" + '\n')+dichtml  # ながら
                line_4 = line.group(1)[0:-1] + \
                    line.group(1)[-1].replace("る", "ま" + '\n')+dichtml  # ます
                line_5 = line.group(1)[0:-1] + \
                    line.group(1)[-1].replace("る", "た" + '\n')+dichtml  # た
                line_6 = line.group(1)[0:-1] + \
                    line.group(1)[-1].replace("る", "れ" + '\n')+dichtml  # 假定れば
                line_7 = line.group(1)[0:-1] + \
                    line.group(1)[-1].replace("る", "て" + '\n')+dichtml  # ている
                line_8 = line.group(1)[0:-1] + \
                    line.group(1)[-1].replace("る", "ら" + '\n')+dichtml  # られる
                line_9 = line.group(1)[0:-1] + \
                    line.group(1)[-1].replace("る", "さ" + '\n')+dichtml  # 使役态
                line_10 = line.group(1)[0:-1] + \
                    line.group(1)[-1].replace("る", "ず" + '\n') + \
                    dichtml  # 古语否定，现代残留
                line_11 = line.group(1)[0:-1] + \
                    line.group(1)[-1].replace("る", "ぬ" + '\n') + \
                    dichtml  # 古语否定，现代残留
                line_12 = line.group(1)[0:-1] + \
                    line.group(1)[-1].replace("る", "、" + '\n')+dichtml
                line_13 = line.group(1)[0:-1] + '\n'+dichtml  # 单独查询复合词
                line_14 = line.group(1)[0:-1] + \
                    line.group(1)[-1].replace("る", "ん" + '\n')+dichtml  # 口语否定
                line_15 = line.group(1)[0:-1] + \
                    line.group(1)[-1].replace("る", "と" + '\n')+dichtml  # 口语ておく
                line_16 = line.group(1)[0:-1] + \
                    line.group(1)[-1].replace("る", "ち" + '\n') + \
                    dichtml  # 口语 てしまう
                line_17 = line.group(1)[0:-1] + \
                    line.group(1)[-1].replace("る", "ちゃ" + '\n') + \
                    dichtml  # 同上，划词
                line_18 = line.group(1)[0:-1] + \
                    line.group(1)[-1].replace("る", "せ" + '\n') + \
                    dichtml  # させる约音
                OutputFile.write(line_1+line_2+line_3+line_4+line_5+line_6 +
                                 line_7+line_8+line_9+line_10+line_11+line_12+line_13+line_14+line_15+line_16+line_17+line_18)
                OutputFile.write(line.group(1)+"\n"+dichtml)
        print("一段复合动词异形词处理完成！")


InflectGodanCompound()
InflectItidanCompound()

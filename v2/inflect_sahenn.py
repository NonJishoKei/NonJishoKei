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
        dichtml = r'<section class="description"><a href="entry://'+line.replace('\n','')+r'#description">'+line.replace('\n','')+'</a>\n</section>\n</>'+'\n'
        line = line.replace('（','')
        line =  line.replace('）','')
        if r'する' in line:
            line_1 = line[0:-3] + line[-3:-1].replace("する", "し" + '\n')+dichtml
            line_2 = line[0:-3] + line[-3:-1].replace("する", "せ" + '\n')+dichtml
            line_3 = line[0:-3] + line[-3:-1].replace("する", "さ" + '\n')+dichtml
            line_4 = line[0:-3] + line[-3:-1].replace("する", "すれ" + '\n')+dichtml
            line_5 = line[0:-3] + line[-3:-1].replace("する", "しろ" + '\n')+dichtml
            line_6 = line[0:-3] + line[-3:-1].replace("する", "せよ" + '\n')+dichtml
            line_7 = line[0:-3] + line[-3:-1].replace("する", "そ" + '\n')+dichtml
            f2.write(line_1+line_2+line_3+line_4+line_5+line_6+line_7)
        elif r'ずる' in line:
            line_1 = line[0:-3] + line[-3:-1].replace("ずる", "じ" + '\n')+dichtml
            line_2 = line[0:-3] + line[-3:-1].replace("ずる", "ぜ" + '\n')+dichtml
            line_3 = line[0:-3] + line[-3:-1].replace("ずる", "ずれ" + '\n')+dichtml
            line_4 = line[0:-3] + line[-3:-1].replace("ずる", "じる" + '\n')+dichtml
            line_5 = line[0:-3] + line[-3:-1].replace("ずる", "じろ" + '\n')+dichtml
            line_6 = line[0:-3] + line[-3:-1].replace("ずる", "じよ" + '\n')+dichtml
            line_7 = line[0:-3] + line[-3:-1].replace("ずる", "ぜよ" + '\n')+dichtml
            f2.write(line_1+line_2+line_3+line_4+line_5+line_6+line_7)
        elif r'す' in line:
            line_1 = line[0:-2] + line[-2].replace("す", "じ" + '\n')+dichtml
            f2.write(line_1)
        elif r'ず' in line:
            line_1 = line[0:-2] + line[-2].replace("ず", "じ" + '\n')+dichtml
            f2.write(line_1)
        else:
            print(line)
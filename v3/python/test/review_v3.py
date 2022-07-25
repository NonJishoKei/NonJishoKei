import os
import re

ProcessPath = os.getcwd()
true = 0
false = 0
lineresult = ''
with open(r'save.txt', 'r', encoding='utf-8') as f,open(r'review_v3.txt','w',encoding='utf-8')as s:
    for i in f.readlines():
        reg = r'^(.*?)\t(.*?)\t(.*?)$'
        line = re.search(reg, i)
        if line.group(1) != line.group(3):
            false += 1
            s.write('Fasle\t'+i)
        elif line.group(1) == line.group(3):
            true += 1
            s.write('True\t'+i)
        else:
            print(i)
print("本次算法准确率："+str(round((true/(true+false))*100,3))+"%")

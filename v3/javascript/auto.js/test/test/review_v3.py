import os
import re

'''
这个脚本用于检查Auto.js版本的算法准确性
'''

ProcessPath = os.getcwd()
true = 0
false = 0
lineresult = ''
with open(r'save.txt', 'r', encoding='utf-8') as f,open(r'review_v3.txt','w',encoding='utf-8')as s:
    for i in f.readlines():
        if i  == ',る\t\n' :
            continue
        else:
            reg = r'^(.*?)\t(.*?)\t(.*?)$'
            line = re.search(reg, i)
            if  line.group(3) not in line.group(1) :
                false += 1
                s.write('Fasle\t'+i)
            elif  line.group(3) in line.group(1) :
                true += 1
                s.write('True\t'+i)
            else:
                print(i)
print("本次算法准确率："+str(round((true/(true+false))*100,3))+"%")
input("按任意键关闭弹窗")

import re
import os

file = os.getcwd()+r'\\待处理.txt'
file_done= os.getcwd()+r'\\目标.txt'


with open(file, 'r', encoding='UTF-8') as file, open(file_done,'w',encoding='UTF-8')as file_done:
        for line in file:
            if '<a name="HATSUON" id="HATSUON"></a>' in line: 
                file_done.write(line)
            else:                                                                                                                                          
                continue





import os

'''
清理重复行
'''

ProessPath = os.getcwd()

InputFile = r'temp.txt'
OutpurFile = r'save.txt'

FileContextSet = set()
with open(InputFile, "r", encoding="utf-8") as f:
    Context = f.read()
    Context = Context.replace('\n', '')
    Context = Context.replace('</>', '</>\n')
    Line = Context.split('\n')
    for i in Line:
        FileContextSet.add(i)

OutputFileContext = list(FileContextSet)
with open(OutpurFile, 'w', encoding='UTF-8') as s:
    for i in OutputFileContext:
        i =i.replace('<section class="description">','\n<section class="description">')
        if '</a>' in i:
            i =i.replace('</a>','</a>\n')
        i =i.replace('</section></>','</section>\n</>\n')
        s.writelines(i)

'''
FileContextSet =set()
with open(InputFile,encoding="UTF-8") as f:
    for line in f:
        FileContextSet.add(line) # 如果不在，返回None 

OutpurFileContext = list (FileContextSet)
with open(OutpurFile,'w',encoding='UTF-8') as s:
    for i in OutpurFileContext:
        s.writelines(i)
'''

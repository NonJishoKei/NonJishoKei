import re
import os
from pathlib import Path

# 创建工作目录
process_path = ".\.process\dics"
if os.path.exists(process_path) == False:
    os.makedirs(process_path)

# 扫描用户自定义的词典索引
index_file = "..\index\index.txt"
index_group = set()
with open(index_file, "r", encoding="utf-8") as file:
    for line in file:
        line = line.replace("\n", "")
        index_group.add(line)

path = "..\index"
p = Path(path)
FileList = list(p.glob("**/*.txt"))
for file in FileList:
    filename = os.path.basename(file)
    if filename != "index.txt":
        if filename != "hiragrana.txt":
            with open(str(file), "r", encoding="utf-8") as inputfile, open(
                ".process\\" + filename, "w", encoding="utf-8"
            ) as outputfile:
                for line in inputfile:
                    line = line.replace("\n", "")
                    varriant = line.split("\t")[0]
                    jishokei = line.split("\t")[1]
                    dichtml = (
                        r'<section class="description"><a href="entry://'
                        + jishokei
                        + r'">'
                        + jishokei
                        + "</a>\n</section>\n</>"
                        + "\n"
                    )  #
                    if jishokei in index_group:
                        if varriant not in index_group:
                            outputfile.write(varriant + "\n" + dichtml)
        else:
            pass  #

os.system("copy .process\*.txt done.txt")  # 合并待添加的词头

import re
import os
from pathlib import Path

# 调用 pyglossary 转换，请注意，是从 mdx 转为idx格式，修改txt源码需要请重新打包
mdx_idx_path = os.getcwd() + "\\.process\\dics\\"
p = Path(mdx_idx_path)
file_list = list(p.glob("**/*.mdx"))
print(file_list)
for file in file_list:
    print(file)
    filename = os.path.abspath(file)
    dic_name = os.path.basename(file).replace(".mdx", "")  # 最终看到的字典名称，与文件名无关
    file_dir_name = os.path.dirname(file).split("\\")[-1]
    os.system(
        "pyglossary "
        + filename
        + " "
        + file_dir_name
        + " --read-format=OctopusMdict --write-format=Stardict --name="
        + dic_name
    )  # 命令行输入 pyglossary -h 查看更多转换格式

print("转换完成:)")

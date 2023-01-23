import re
import os
from pathlib import Path

os.system("python add_index.py")

# 将所有mdx解压为txt
print("开始解压词典")
path = os.getcwd()
p = Path(path)
file_list = list(p.glob("**/*.mdx"))
for file in file_list:
    mdx_file_name = os.path.basename(file)
    mdx_extract_path = path + "\\.process\\dics\\" + mdx_file_name.replace("mdx", "")
    print("mdict -x " + mdx_file_name + " -d " + mdx_extract_path)
    os.system("mdict -x " + mdx_file_name + " -d " + mdx_extract_path)
    mdd_file_path = os.path.abspath(file).replace(".mdx", ".mdd")

    # 如果mdx2all文件夹下有mdd文件，那么复制到相应的mdx解压路径，在重新打包后可以被pyglossary识别，生成的idx文件可以显示图片
    if os.path.exists(path) != None:
        mdd_file_name = os.path.basename(mdd_file_path)
        mdd_copy_path = mdx_extract_path + "\\" + mdd_file_name
        os.system("copy " + mdd_file_path + " " + mdd_copy_path)

# 添加补充的词条
path = os.getcwd() + "\\.process\\dics\\"
p = Path(path)
file_list = list(p.glob("**/*.txt"))
for file in file_list:
    with open("done.txt", "r", encoding="utf-8") as inputfile, open(
        file, "a", encoding="utf-8"
    ) as outputfile, open("error.txt", "w", encoding="utf-8") as errorfile:
        inputfiletext = inputfile.read().replace("\x1a", "")  # 添加补充的词头，删除特殊标记

        # 删除重复行
        OutputFileContext = set()
        Context = inputfiletext.replace("\n", "")
        Context = Context.replace("</>", "</>\n")
        Line = Context.split("\n")
        for item in Line:
            OutputFileContext.add(item)

        # 生成打包文件
        error_line_reg = re.compile(
            r'^<section class="description">'
        )  # 不符合mdx文件格式规范会导致打包时报错
        for item in OutputFileContext:
            if re.search(error_line_reg, item) != None:
                print("出现空行异常，请注意检查！\n" + item)
                errorfile.write(item)
            item = item.replace(
                '<section class="description">', '\n<section class="description">'
            )
            if "</a>" in item:
                item = item.replace("</a>", "</a>\n")
            item = item.replace("</section></>", "</section>\n</>\n")
            outputfile.write(item)

# 打包添加好词条的文件
os.system("python repack_mdx.py")

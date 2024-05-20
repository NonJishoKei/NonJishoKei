"""
打包 mdx 文件
"""

import datetime
import glob
import logging
import os
import re
import zipfile
from textwrap import dedent

import main

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
os.chdir(CURRENT_PATH)


rule_path = os.path.join(CURRENT_PATH, r"rule")
INDEX_PATH = os.path.join(CURRENT_PATH, r"index")
PROCESS_PATH = os.path.join(CURRENT_PATH, r"process")


def compress_file(input_filename, output_filename):
    """压缩文件"""
    release_pub_path = os.path.join(CURRENT_PATH, "release_pub")
    output_filename = os.path.join(release_pub_path, output_filename)
    with zipfile.ZipFile(output_filename, "w") as zip_ref:
        zip_ref.write(input_filename)


def check_pack_file():
    """检查打包文件"""
    # 合并所有词条
    source_dir = os.path.join(CURRENT_PATH, "process")
    process_pack_file = os.path.join(source_dir, "pack_process.txt")
    release_pack_file = os.path.join(source_dir, "pack_release.txt")
    # 获取所有 .txt 文件的路径
    source_files = glob.glob(os.path.join(source_dir, "*.txt"))
    for file in source_files:
        with open(file, "r", encoding="utf-8") as source_file, open(
            process_pack_file, "a", encoding="utf-8"
        ) as pack_process_file:
            pack_process_file.write(source_file.read())

    # 清理重复行
    process_pack_set = set()
    with open(process_pack_file, "r", encoding="utf-8") as input_file, open(
        release_pack_file, "w", encoding="utf-8"
    ) as output_file:
        for line in input_file:
            if line != "":
                line = line.strip("\n")
                nonjishokei = line.split("\t")[0]
                jishokei = line.split("\t")[1]
                dichtml = (
                    r'<section class="description"><a href="entry://'
                    + jishokei
                    + r'#description">'
                    + jishokei
                    + "</a>\n</section>\n</>"
                    + "\n"
                )
                process_pack_text = nonjishokei + "\n" + dichtml
                process_pack_set.add(process_pack_text)
        for process_pack_line in process_pack_set:
            output_file.writelines(process_pack_line)
    return process_pack_file, release_pack_file


def add_description():
    """更新描述文件"""
    update_date = datetime.datetime.now().strftime("%Y-%m-%d")

    release_pub_path = os.path.join(CURRENT_PATH, "release_pub")
    description_text = dedent(
        f"""<p>NonJishoKei For mdx: What You See Is What You Get</p>
    <p>updateDate: {update_date}</p>
    <p>For feedback: <a href="https://github.com/NoHeartPen/NonJishoKei">https://github.com/NoHeartPen/NonJishoKei</a> </p>
    """
    )
    description_html_file = os.path.join(release_pub_path, "description.html")
    with open(description_html_file, encoding="utf-8", mode="w") as f:
        f.write(description_text)


def pack2mdx():
    """使用 mdict-utils 打包为mdx文件"""
    process_pack_file, release_pack_file = check_pack_file()
    add_description()

    release_path = os.path.join(CURRENT_PATH, "release_pub")
    title_file = os.path.join(release_path, "title.html")
    description_file = os.path.join(release_path, "description.html")
    mdx_file = os.path.join(release_path, "NonJishoKei.mdx")
    pack_config = f"--title {title_file} --description {description_file}"
    pack_cmd = f"mdict {pack_config} -a {release_pack_file} {mdx_file}"
    # 打包
    os.system(pack_cmd)
    # 删除过程文件
    os.remove(process_pack_file)
    os.remove(release_pack_file)
    update_date = datetime.datetime.now().strftime("%Y-%m-%d")
    compress_file(mdx_file, f"NonJishoKei_v2_{update_date}.zip")


main.inflect_nonjishokei()
pack2mdx()

import os

# 重新打包
root_path = os.getcwd()
process_path = root_path + "\\.process\\dics\\"
for process_root_path, dic_dirs, dic_files in os.walk(process_path):
    for dic_dir in dic_dirs:
        os.chdir(process_root_path + dic_dir)
        file_dir_name = process_path + dic_dir + "\\" + dic_dir
        os.system("mdict -a " + dic_dir + ".mdx.txt " + file_dir_name + ".mdx")

os.chdir(root_path)  # 切换工作路径到项目根目录

os.system("python convert_idx.py")  # 调用转换为idx的脚本

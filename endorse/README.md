# 介绍

本文件夹主要用于验证日本語非辞書形辞典算法的可靠度。

## 思路

通过调用 Mecab 对语料进行分词处理，

![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20221107190449.png)

获取其中的`動詞`和`形容詞`部分，即模拟剪贴板查词的使用场景：

![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20221107190414.png)

然后调用本项目的 v3 版本算法进行推导，验证并统计推导结果。

![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20221107190623.png)

# 复现指南

## 配置 Mecab

如果没有使用过 Mecab 请不要跳过这部分。

这里只介绍 Windows 端安装方法，其他平台请参考官网首页[MeCab: Yet Another Part-of-Speech and Morphological Analyzer](https://taku910.github.io/mecab/#download)

Windows 端可以使用官网提供二进制文件下载链接：[https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7WElGUGt6ejlpVXc](https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7WElGUGt6ejlpVXc)

安装时注意勾选`utf-8`编码；另外，可以更改程序安装路径，反正安装完成后都要手动将安装路径下的`bin`文件夹手动添加到系统环境变量 Path。

确认安装好 Mecab 后，使用`pip install mecab-python3 `安装 Python 调用 Mecab 的第三方库。

然后到[Unidic 辞書](https://clrd.ninjal.ac.jp/unidic/)下载`unidic-cwj-3.1.1-full.zip`，解压到根目录，注意文件夹名要是`unidic-cwj-3.1.1`，如果不是，请修改每个脚本的`dic_path`。

![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20221107190047.png)

然后到 Mecab 的**安装**路径，在`dic`文件夹下找到`ipadic`文件夹里面的`dicrc`，用记事本打开，把内容复制到`unidic-cwj-3.1.1`文件夹下的同名文件中。

运行[test_macab.py](test_macab.py)测试 Mecab 是否安装成功。

## 测试

确认 Mecab 安装成功后，将要测试的语料放到[testfiles](testfiles)文件夹并解压，然后修改文件夹名为 test。

[testfiles](testfiles)有测试文件（青空文库和维基百科）备份下载链接，注意测试前要把解压后的文件夹名修改为 test。
![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20221107190145.png)

语料准备工作完成后，运行[get_mecab.py](get_mecab.py)脚本，等待片刻即可。

![|500](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20221106131719.png)
如果是其他语料，请确认文件名以是`_temp.txt`结尾（txt 是后缀名）

![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20221107095616.png)

或者修改[get_mecab.py]()中的`FileNames = list(Path(path).glob("**/*_temp.txt")) `。

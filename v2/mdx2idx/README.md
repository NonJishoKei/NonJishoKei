# 快速上手

请下载《日本語非辞書形辞典》项目`v2`文件夹下的**所有**文件，在`mdx2idx`文件夹，运行`add_index.py`脚本，脚本运行成功会生成一个名为`done`的txt文件。

将想转换的 mdx 词典用 getDic 等软件解压为 txt 文件，把`add_index.py`脚本生成的`done`的txt文件添加到解压后的 txt 文件中（注意 mdx 源文件的格式要求），然后打包为 mdx，再使用 PyGlossary 将重新打包的 mdx 转为 idx 即可。关于 PyGlossary 的使用方法，可以参考项目官网 https://github.com/ilius/pyglossary 和这篇教程 [PyGlossary：将不同格式的字典转换成 Kindle 字典](https://bookfere.com/post/883.html)

# 高级指南

## 批量转换

如果希望快速转换多本词典，请通过命令行`pip install -r requirements.txt`安装相关依赖（请在`mdx2idx`文件夹下使用这条命令）。

将所有 mdx 文件放到`mdx2idx`文件夹下，运行`main.py`脚本，等待片刻即可。

## 自定义索引

由于 idx 的跳转特性，转换好的词典可能会包含一些无法跳转的链接。如果不想在这些无意义的跳转链接中浪费时间，可以将`v2`文件夹下`index`内的`index.txt`里的内容删除，然后替换为想转换的词典的词条，再执行`main.py`。

词条导出方法：可以使用 GoldenDict，在词典详情界面右键查看词条然后导出的文本，不需要删除`たべる【食べる】`这样的词条，脚本会自动处理，也不需要包含词性。

## 多语言支持

如果将`index.txt`替换为其他按照`词形变化	原型`格式储存的数据，比如：
```
perceived	perceive
perceived	perceive
perceives	perceive
perceiving	perceive
```

那么，本项目提供的脚本就可以用于其他语言的 mdx 转 idx。由于精力有限，本项目暂不提供这样的数据，有需要的同学请自行尝试。

英语的词形变化数据可以参考：[Free English to Chinese Dictionary Database](https://github.com/skywind3000/ECDICT)

## 转换 mdd 文件

如果希望转换 mdd 文件，请将 mdd 文件和 mdx 一起放在`mdx2idx`文件夹下，然后运行`main.py`。

请注意：这种方式只能保证 PyGlossary 会识别并处理 mdd 文件，转换的 idx 可能存在图片显示为`[image]`的情况。

## 删除 HTML 标签

PyGlossary 不会处理不被 idx 支持的 mdx 源文件语法，有需要和有时间的同学可以参考这部分的内容，自行修改`.process`文件夹下`dics`解压出的源文件，修改完成后，请运行`pack_mdx.py`，不要运行`main.py`文件。

1. 不支持`<a class="link" href="javascript:;">(.*?)</a>`跳转语法
	1. 替换参考正则：`<a href="entry://\1">\1</a>`
2. 不支持`<img alt="" src="data:image/png;base64,(.*?)>`这样含有 base64 码的图像标签
	1. 替换参考正则：替换为空即可
	2. StarDict似乎不支持图片，可以考虑手动删除图片标签`<img (.*?)>`
3. `<span>(.*?)</span>`标签：
	1. 替换参考正则：替换为空即可
	2. PyGlossary 似乎会按照特殊的格式渲染该标签的文本
……（欢迎补充反馈）

## 转换为其他格式

pyglossary 提供如下格式转换支持：

<img src="https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20230123195705.png" width="500">

有需要的同学请自行修改`convert_idx.py`的内容。

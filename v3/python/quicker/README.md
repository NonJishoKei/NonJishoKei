前排提示：这个项目是日本語非辞書形辞書_v3版本的Demo产品，可能会遇到不少问题，欢迎留言反馈:)

另外，文档发布在[v3_For_Quicker_Demo · 语雀 (yuque.com)](https://www.yuque.com/noheartpen/hbrngk/pnc58s/edit#1713e6a0)

# 最终效果

直接上图😎
![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//20220725_111313.gif)
（实际使用应该没有看起来的这么卡，演示时有停顿）

# 下载

[https://wwp.lanzouf.com/b011uva4d](https://wwp.lanzouf.com/b011uva4d) 密码:e3h4

注意：
1. 最好找个地方专门放，完成设置后，不要随便删也不要随便移动`main.exe`和`v3_index.txt`
2. 解压路径中最好不要有空格
3. 目前需要与[Quicker](https://getquicker.net/)配合使用，直接双击exe没有反应是正常的:)

# 使用方法

## 粘贴动作（必看）

[YiDicForSaladict](https://getquicker.net/Sharedaction?code=7c631fb6-0bb9-4f72-7598-08da6d59e93b)

[YiDicEBWin](https://getquicker.net/Sharedaction?code=9f4b70fd-7ff0-4ce5-758c-08da6d59e93b)

## 基础设置（必看）

打开Quicker，粘贴动作，然后右键打开编辑，双击`运行脚本`
![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20220725102614.png)

在`脚本内容`中填入下载的exe文件的路径（Win11的可以通过右键点击然后`复制文件路径`获取，双引号可以不删）

接着在下面的`工作目录`填入文件夹的路径，去掉双引号和main.exe就可以了。
![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20220725091604.png)

到这里基本设置就完成了。下面介绍高级选项。

## 沙拉词典 (必看)

如果沙拉词典的`在独立窗口搜索剪贴板内容`的快捷键不是`Alt+C`，还需要进行修改。
![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20220724204140.png)


打开编辑页面，`模拟按键B（参数）`
![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20220725083226.png)

参考[快捷键语法](https://getquicker.net/KC/Help/Doc/sendKeys)，填入你喜欢的快捷键即可
![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20220725083254.png)


## EBWin （非必看）

默认的分享的动作需要自己提前打开EBWin才可以用，如果希望每次选中文本后直接启动软件查词，那么还需要另外的设置。

先把电脑上的EBWin软件打开，然后打开`YiDicForEBWin`的编辑界面

双击下面的`激活进程主窗口`
![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20220725103344.png)

点击下面的红框
![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20220725104354.png)

会发现切换到了EBWin的界面，随便点击EBWin顶部状态栏的一个位置
![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20220725103944.png)

会发现，软件路径就自动填好了
![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20220725104305.png)

如果上述方法搞不定的话，自己手动填也行。

当然，你也可以根据自己的需要，填入自己喜欢的词典软件，只是这样一来，需要改`程序路径`和`进程名称/pid`2个地方。

# Todo
- [ ] 正则支持
	- [ ] 在MS Word中或是像`軋(きし)み合(あ)わない`这样的句子划词翻译，正则可以直接处理为軋み合わ
	- [ ] `々ゝゞ/\/″\`
	- [ ] `<ruby></ruby>`（浏览器内划词）
- [ ] 验证算法真实准确度
	- [ ] 跟进日本語非辞書形辞書_v2的进度
		- [x] 0722
	- [ ] 有Mecab分词语料的同学欢迎发送到 NoHeartPen@outlook.com ，只需要`書字形`和`書字形基本形`2列的数据即可，感激不尽:)
- [ ] ……
欢迎提出其他意见

# 大致思路

举个例子简单说明下脚本的工作原理，方便大家结合自己的需要修改。

对于`ご飯を食べたい`这个句子，我们用鼠标选中`食べた`按下快捷键，Quicker会将选中的文字复制到剪贴板，然后启动电脑上的`main.exe`文件，这个exe文件会读取剪贴板，获取到最近一次复制的内容，即`食べた`。

然后程序会读取最右侧的假名即`た`，根据v2版本的词条规律我们可以知道，`た`出现在词尾假名说明要么是一段动词，要么是五段动词（注：技术细节处会给出这么假设的相关数据）。

我们先假设它是五段动词，然后程序会将`た`替换为`つ`，然后在这个`v3_index.txt`文件中查找有没有`食べつ`这个动词。
……
找了一圈没有，那说明这个我们的假设是错误的。

然后程序会验证另一种假设：将词尾`た`替换为`る`，然后再去`v3_index.txt`文件中查找`食べる`，很幸运，这次找到了。

程序会将找到的`食べる`写入剪贴板，Quicker检测到剪贴板内容发生变化后就会调起词典软件了（所以你也可以在支持mdx的GoldenDic上用，享受双倍的快乐）。

另外，`v3_index.txt`里面保存的原型数量也会影响最终的效果，可以自由向里面添加收集到的单词。

# 技术细节

可能有人会好奇，最近怎么突然高产了起来~~开始刷版本号~~，v2版本都才出一周多，怎么这么快v3版本就来了。

这是因为v3版本其实是v2版本的逆过程，而且v3版本之后的改进在很大程度上取决于v2版本的成果，所以先制作了这么一个小工具，供有兴趣的同学折腾。

接下来是正文：

如果有人分析过v2版本的源文件，就会注意到穷举出的变形的词尾假名似乎重复率有点高呀，有没有什么规律呢？
![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20220725115735.png)

我们把词尾部分都提取出来，整理下得到下面这个表格：
![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20220725113051.png)

查阅这个表格我们就知道`た`只能由一段和五段动词产生，但具体是谁我们只能采用笨办法：查原型来判断。
![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20220725114212.png)

虽然有一半左右的的词尾假名都只有一种来源，但在丢失了上下文的情况下，我们可能都需要进行3次替换和3次遍历查找，不过好在即使是最差的情况，大多数人的电脑应该也能满足日常的需要。
![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20220725122338.png)

不过，即使把v2的172580个词条都给查一遍，也只要~~区区~~6分钟
![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20220725125027.png)
~~所以这算法也没有那么烂吧……QAQ~~

最后，手动@MOJi、@沙拉词典、@EBWin、@欧路词典、@Yomichan、@AnkiHelper等开发者，~~最强~~开源日语取词算法的Python版本已经托管在Github上啦，欢迎PR和提交issue呀:)
[https://github.com/NoHeartPen/JapaneseConjugation](https://github.com/NoHeartPen/JapaneseConjugation)
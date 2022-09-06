前排说明：这个版本目前需要和 Android 端的的一款自动化软件 Auto.js 配合使用，iOS 端的同学就不要照本宣科了。另外，上手难度（可能）非常大，实际体验也比较一言难尽，请先仔细阅读本文档，确认自己有能力、有时间、有需要再动手遇到问题可以到 GitHub 处留言，或者通过 NoHeartPen@outlook.com 与我联系。

# 最终效果

<img src="https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//2022-09-06-12-13-01-27.gif" width="500">

如上所示，实际使用可能会存在较为明显的卡顿感（实际推导过程并没有消耗太多时间），所以这个版本的真正意义是为之后将在沙拉查词提交的 PR 进行测试和优化，并不适合一般用户折腾。如果你不太擅长计算机操作，请直接忽略这个版本。

# 下载

GitHub/Gitee：下载`main.js`、`sendclip_url.js`、`v3_index.txt`这3个文件即可
如果你不在项目的 README 页面，请通过下面的方式下载：
蓝奏云：[https://wwp.lanzouy.com/b01208k2j](https://wwp.lanzouy.com/b01208k2j)
密码:862e（更新会稍有延迟）

注意：
1.  不要修改`v3_index.txt`和`sendclip_url.js`的文件名。

# 上手步骤

请根据自己的喜好，选择以下三个版本的 Auto.js 下载安装到手机：
[Auto.js Pro](https://pro.autojs.org/)：原项目的付费版本，稳定好用
[AutoX.js](http://doc.autoxjs.com/#/)：基于[Auto.js](https://github.com/hyb1996/Auto.js)的开源免费版本，由志愿者维护
[Auto.js](https://github.com/hyb1996/Auto.js)：开源免费，但开发者已明确表示不再维护，同时删除了打包过的文件，需要自己编译

由于 Auto.js 可以获取到非常敏感的信息和权限，请尽量通过以上推荐的3种方式下载安装。

不管使用的哪个版本的 Auto.js，以下统都以 Auto.js 指代。

安装 Auto.js 后请先确保授予了读取和修改剪贴板的权限。

如果使用 [Auto.js Pro](https://pro.autojs.org/)，可以将下载的文件放到设置的脚本路径；如果使用的是 [Auto.js](https://github.com/hyb1996/Auto.js) 或者 [AutoX.js](http://doc.autoxjs.com/#/)，请自己手动新建文件，并手动粘贴三个下载文件的内容。

做完准备工作后，点击 main.js 脚本的运行按钮，即可查询剪贴板内的单词的辞書形。

由于 Android 高版本系统对应用读取剪贴板的限制，必须要通过分屏的方法才能实时查阅剪贴板中的单词。（所以还想折腾么:)

另外，运行脚本前建议手动启动 MOJi，这样脚本可以快速切换到查词页面。

如果你信赖本脚本的的推导结果，可以打开 MOJi 辞書的`设置-高阶玩法-URLScheme-自动打开第一个搜索结果`，这样会自动进入第一个单词的详情页。

# 大致思路&技术细节

与 Python 即 Quicker 版本完全一致，感兴趣的话，参考 Python 版本的说明文档即可。

注：本文是日本語非辞書形辞典项目的 [JavaScript 版本](https://github.com/NoHeartPen/JapaneseConjugation/tree/master/v3/javascript/auto.js/moji)的说明文档。
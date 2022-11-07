# 所见所划，即为所查

作为一个比较懒的人，我十分在意每次查单词时手动打字浪费的时间

![班群_非辞書演示](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//班群_非辞書演示.gif)

在接触了几款支持剪贴板查英语单词的软件后，开始探索如何在日语上实现同样的功能。

电脑端

<img src="https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//_00_00_00-00_00_30.gif" width="500">

手机端

<img src="https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Screenrecorder-2022-03-11-09-59-12-769%2000_00_00-00_00_30.gif" width="500">

一开始只是想解决日语用言「活用形」与「辞書形」之间的差异，但在摸索过程中发现了其他可以优化的地方，于是将这一路的尝试集中汇总成一个项目——这就有了「日本語非辞書形辞典」。

本项目的“非辞書形”指的一个被《大辞泉》等权威辞典收录的单词在实际使用中出现的形态，不只是语法上的动词活用。

简单地说，本项目主要从如下 4 个方面对日语的剪贴板查词进行了优化：

## 简日汉字

相比于欧美国家，中国的学习者在起步阶段无疑会轻松很多，但进入一定阶段后可能会发现：简体字和漢字之间还是有很多微妙区别，尤其是文化相关的词汇：

```md
绫辻行人      綾辻行人
京极夏彦 京極夏彦

延历寺 延暦寺  
涩谷 渋谷

卢沟桥 盧溝橋  
王维 王維
```

更麻烦的是，日语漢字和繁体也不能完全划等号：

```md
简/繁/日：
儿童、兒童、児童
竞争、競爭、競争
```

……
（注：繁体字形参考《教育部國語辭典》）

有这方面的需要，请到[日简汉字字典项目](https://github.com/NoHeartPen/Kanji2Hanzi)处查看更多信息。

## 用言活用

这里的“用言”主要指的是动词。与英语不同，日语的活用会嵌套发生：

> 私はご飯を**食べて**いる（我正在吃晚饭）
> I am **having** dinner

> 私はご飯を**食べて**いた（当时，我正在吃晚饭）
> I was **having** dinner

> 私はご飯を**食べた**。（我吃了晚饭）
> I **had** dinner。

> 私はご飯を**食べな**かった（我没有吃晚饭）
> I didn't **have** dinner。

> 母親は私をご飯を**食べさ**せる。（妈妈让我吃晚饭）
> Mom lets me **have** supper

> 母親は私をご飯を**食べさ**せない。（妈妈不让我吃晚饭）
> Mom won't let me **have** dinner。

在上面 6 个例句中，英语只出现了 having、had 2 个「非辞書形」，而日语出现了 6 个传统语法观念下的「非辞書形」，但只关注词尾假名的话，就只有 3 个「非辞書形」。

这里强调只关注词尾假名是因为传统的日语语法对于`高かった`划分为`高かっ`和`た`2个部分，即`高かっ`才是活用形，但是本项目只关注与原型等长的部分即`高か`，所以使用本项目查词时请只划`高か`不要划`高かっ`（如果是词汇量较小的初学者，可以关注[日本語用言活用辞書 byGary](https://www.pdawiki.com/forum/forum.php?mod=viewthread&tid=40881&extra=page=2&filter=typeid&typeid=71)项目，该项目基于日语传统语法，划词时不需考虑原型与活用之间的差距）。

英语为了解决的这个问题，采用了穷举的做法。

但如果用按照传统的日语语法的思路穷举的话，日语的工作量将是一个天文数字；而按照传统语法的思路归纳规律也会面临同样的问题：因为我们不是在挑选经典的例句，而是在穷举所有可能会出现的句子。

所以，本项目与基于西方语言学理论的 Hunspell 技术和欧路词典采用的技术都不同：只关注「辞書形」词尾假名的变化。

这种方法大幅降低了工作量，但也对使用者的日语水平提出了更高的要求：必须要精准地判断出「辞書形」词尾假名的位置。

以下面这句话为例：

> これから雨が降ります。
> 彼はバスから降ります。

如果要查询 2 句话中的动词，第 1 句话对应的辞書形是降る，第 2 句话是降りる，所以我们应该选中`降り`来查第 1 句（和辞書形降る的字符数一致），选中`降りま`来查第 2 句（和辞書形降りる的字符数一致）。

但采取“正统”的日语语法分析，我们也要结合上下文才能判断出该选择`降りる`还是`降る`。

所以，日语的剪贴板查词优化有一个绕不开的优化点就是：既然能获取的上下文语境的极为有限，那么就应该返回所有可能存在的结果。

## 片假名使用习惯

以这句话中的拟声拟态词为例：`隅の方に小さくなって黙ってチョコチョコ働いていたものだから`。如果直接输入`チョコチョコ`，那么很多词典软件都不能给出正确的解释：
![|500](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20220310204031.png)

![|500](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20220310204259.png)

但是如果输入ちょこちょこ就能查到了：
![|500](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20220310204420.png)
![|500](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//6332f6ddb8ee53c5a0ea7bf0.jpg)

## 复合词书写

日常使用复合动词时，第一个或者第二个动词往往只写假名，即“异形词”：如果我们输入的是`沸きたつ`或者`わき立つ`，那很可能查不到结果，输入`沸き立つ`或者平假名`わきたつ`就能查到。

本项目使用日本国立国语研究所提供的[複合動詞レキシコン](https://vvlexicon.ninjal.ac.jp/)数据，对共计 2759 个复合动词及其活用做了相关优化（其中五段复合动词 1821 个，一段复合动词 936 个，还有 2 个`数え切れない`和`煮え切らない`一般以惯用句的形式出现，且不以动词规律活用，故已剔除）

# 项目版本

这个项目共有如下 3 个版本：

## [v1](v1)

v1 版本可以看作是这个项目的雏形，但由于做法过于乱暴——不基于品词，单从词尾假名进行分类并穷举非辞書形，现已不再维护，但核心的思路一直保留在 v2 和 v3 上。

## [v2](v2)

基于品词穷举；删除无意义、凭空捏造的用言变形。

v2 版本适合一般人使用：

只需要把 mdx 文件导入词典软件（比如 GoldenDict、EBWin、MDict、欧路词典），以后碰到动词变形都会给出对应的辞書形，点击给出链接跳转即可。

下载方式：

[GitHub](v2/release_pub) | [Gitee](v2/release_pub) 这 2 种方式更新频繁，但需要在 [Github](https://github.com/NoHeartPen/NonJishoKei) 或者 [Gitee](https://gitee.com/NoHeartPen/JapaneseConjugation) 的项目主页才能打开

[FreeMdict 论坛网盘](https://cloud.freemdict.com/index.php/s/Q62m2gk2dT5Lm99) | [蓝奏云](https://wwp.lanzouf.com/b011tnz6b) 密码:8yp8 这 2 种平台更新稍有延迟

## [v3](v3)

v3 版本提供的是推导辞書形的代码，使那些不支持 mdx 格式的词典软件也能有完美的划词体验。

由于使用了代码，有了更多可操作的空间，所以 v3 版本可以解决更多问题：

- Word 注音
- 踊り字

请注意：v3 版本只提供辞書形推导的的代码，需要嵌入词典软件或者和其他工具配合才能使用，上手有一定难度。

建议大家向词典软件的开发者推荐这个项目，由 Ta 们进行适配，节省大家宝贵的时间。

@[沙拉词典](https://saladict.crimx.com/)，@[MOJi 插件](https://www.mojidict.com/article/1BvHLjMm8u)，@[欧路词典](https://www.eudic.net/v4/en/app/eudic)，@[rikaikun](https://github.com/melink14/rikaikun)，@[Yomichan](https://github.com/FooSoft/yomichan)，@[AnkiHelper](https://github.com/mmjang/ankihelper)，@汉王词典笔，@网易有道词典笔……

目前已经有 Python 和 JavaScript 2 种版本，欢迎贡献其他语言版本

### Python 版本

<img src="https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//20220725_111313.gif" width="500">

使用方法请参考 [README](v3\python\quicker\README.md) 文档。

### JavaScript 版本

<img src="https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//2022-09-06-12-13-01-27.gif" width="500">

使用方法请参考 [README](v3\javascript\auto.js\moji\README.md) 文档。

# [tools](tools)

参与该项目过程中可能会用到的工具和一些资料。

如果你遇到问题，欢迎与我交流，我的邮箱是 NoHeartPen@outlook.com

# [endorse](endorse)

本项目在剪贴板查词的使用场景下的准确率远超传统的 NLP 工具（比如 Mecab ），有关下图的更多内容下图请到[endorse](endorse)文件夹。

![|500](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20221106131719.png)
（使用语料：青空文库 DVD-ROM 2007 年 10 月 1 日時点）
![|500](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//Pasted_image_20221106152040.png)
（使用语料：维基百科 20221020 数据，下载自：[https://dumps.wikimedia.org/jawiki/](https://dumps.wikimedia.org/jawiki/)）

本项目能达到 99%的准确率主要原因有 2 点：

1. 会返回所有可能的结果；
2. 通过限定输入降低了工作量——只划与原型等长的“非辞書形”这个做法绕开了动词活用嵌套和接续语法等棘手问题

虽然 Mecab 的准确率只有 70%左右，但这不意味着 Mecab 的算法有什么大的问题。因为 Mecab 并不是为剪贴板这样能获取的上下文语境信息极为有限的使用场景而设计的工具。但是，这个2者的准确率可以说明：“日语的形态分析（形態素解析）最好返回**所有**可能的辞書形”。

# 鸣谢

首先，感谢网友[满星 MAX](https://space.bilibili.com/571730518/dynamic) 、[MrCorn0-0](https://github.com/MrCorn0-0)等人，Ta 们在这方面的尝试为项目提供了宝贵的技术经验：

- [hunspell_ja_JP](https://github.com/MrCorn0-0/hunspell_ja_JP)
- [日本語用言活用辞書 byGary](https://www.pdawiki.com/forum/forum.php?mod=viewthread&tid=40881&extra=page=2&filter=typeid&typeid=71)
- [日本語活用形辞書](https://forum.freemdict.com/t/topic/12031)
- [Python 辅助 MDX 转 MOBI（以 AHD5th 为例）](https://www.bilibili.com/read/cv11110087)
- [英语词汇构词法规则库（三合一版）（亦：英语变形词规则库）](https://www.bilibili.com/read/cv11110160)

感谢我的同学 LHY、LRY 和 amob、cinnamon 等网友：Ta 们在项目尚处于初期，热情地参与进来，并提供了若干珍贵的建议和反馈，让项目一步一步完善到现在 ；也感谢 YL、ZY、CKR、DSL 等诸位老师：虽然没有在项目上提供直接的指导，但正是诸位老师在日语上的深厚造诣和对我的悉心栽培让我有兴趣、也有能力完成这个项目；

最后，非常感谢日本国立国语研究所的诸位老师们：虽然素未谋面，但 Ta 们整理分享的数据、公开的论文、举办的讲座也是我数次能从“山重水复疑无路”的死胡同中挣脱出来的关键。

# 支持项目

作为一个业余维护的个人项目，感谢大家一路以来的支持！

如果愿意帮助维持这个项目继续推进可以：

- 让更多开发者发现这个项目：在[Github 主页](https://github.com/NoHeartPen/JapaneseConjugation)，点击右上角的`★Star`按钮收藏本项目、向日语词典软件的开发者推荐这套解决方法；
- 为项目修改错别字用词、提出建议、也可以直接提交代码；
- 打赏作者请他喝瓶 AD 钙；

注意：本项目完全开源、免费，请确认是出于心情愉悦自愿对作者个人的赠与支持，而非购买行为。本人不承诺、不提供任何针对该赠与的回报性质服务，感谢理解:)

微信：

<img src="https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//202208051503.png" width="250" />

支付宝：

<img src="https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//62ecaedf702c5dcb9c2eb4be.jpg" width="250" />

# 许可证

版权所有 (c) 2022 NoHeartPen 和其他贡献者。保留所有权利。

若无特殊说明，本项目的代码使用[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0.html)进行许可，其他文件使用[署名 4.0 国际 (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.zh)协议共享。

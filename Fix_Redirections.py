import re
import os
'''
请注意，该脚本来自满星MAX的这篇[Python辅助MDX转MOBI（以AHD5th为例）](https://www.pdawiki.com/forum/thread-36130-1-1.html)，
我只是将之用于解决@@@的跳转语法问题，并没有仔细研究过代码，
另外，注意这个脚本有一个十分关键的`wordforms`文件夹，请不要随意删除，否则你很可能要到[forms-EN.txt](https://github.com/Tvangeste/dsl2mobi/tree/master/wordforms)这里重新下载
'''

# 获取当前工作目录，打开工作目录下的txt文件
file = os.getcwd() + '/待处理.txt'
file_for_save = os.getcwd() + "/目标.txt"  # 此处是生成的文件的名字和路径
Error_Lines_Save = os.getcwd() + "/异常.txt"  # 若出现异常，异常行保存的文件的位置


def ReturnMeaning(word):  # 此函数用于确定目标词是否存在，因为可能存在空跳转的现象，即@@@LINK后所跟的目标词并不存在。
    pattern = re.compile(r'%s\t(.*)$' % word, re.IGNORECASE)
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            result = pattern.match(line)
            if result:
                return result.group(1)


def Judging(jumping_word, target_word):
    # 此函数传入跳转词和目标词，以判断跳转词是否是目标词的一个简单的变形词。比如跳转词advocating就是目标词advocate的一个简单变形。
    if '+' in target_word:  # 词头可能含有一些奇怪的特殊字符比如“+”号，此处转义以免传入正则表达式中产生干扰
        target_word = target_word.replace('+', '\\+')
    p1 = re.compile('%s: (.*)$' % target_word, re.IGNORECASE)
    p2 = re.compile(', ')
    l1 = []
    with open(".\\wordforms\\forms-EN.txt", 'r', encoding='utf-8') as f:
        for line in f:
            result = p1.match(line)
            if not result:
                continue
            new = p2.split(result.group(1))
            l1.append(new)
    # print(l1)
    if l1:
        l2 = [i for k in l1 for i in k]
        l3 = list(set(l2))
        # print(l3)
        if jumping_word in l3:
            return True
        else:
            return False
    else:
        return False


if __name__ == '__main__':
    with open(file, 'r',
              encoding='utf-8') as f, open(file_for_save,
                                           'w',
                                           encoding='utf-8') as f2, open(
                                               Error_Lines_Save,
                                               'w',
                                               encoding='utf-8') as f3:
        pattern = re.compile('([^\t]*?)\t@@@LINK=(.*?)$'
                             )  #正则表达式，匹配如advocating @@@LINK=advocate形式的行
        parttern_multi_words = re.compile(
            r'\s')  #该正则用来判断是否是词组或短语，词组或短语较难处理，本文不涉及。
        for line in f:
            result = pattern.match(line)  #开始匹配
            try:
                if result:  # 若匹配成功
                    Jumping_word = result.group(1)  #以上面的例子为例，advocating为跳转词
                    Linking_word = result.group(2)  #advocate为目标词
                    if Linking_word.endswith(
                            '\\n'
                    ):  # 此处因词典而异，这里是因为这本AHD词典目标词后面存在两个字符串'\n'，详见帖子上面的截图。
                        Linking_word = Linking_word.replace('\\n',
                                                            '')  # 接上。去除无用的字符串
                    matched = ReturnMeaning(
                        Linking_word)  # 遍历词典中所有词条以确定是否有advocate的意项
                    if matched:  #若匹配到了，则往下进一步处理；此处判断结构不用else，因为没匹配到说明是无效的空跳转，不用保存
                        multi_words = parttern_multi_words.split(
                            Linking_word)  #以空格来分割该词
                        if len(
                                multi_words
                        ) != 1:  #若不等于1说明是词组或短语动词，这样去就没必要进一步匹配forms-En.txt了，直接写入
                            new_line = pattern.sub('\\1' + '\t' + matched,
                                                   line)
                            f2.write(new_line)
                        else:
                            z = Judging(
                                Jumping_word, Linking_word
                            )  # 否则判断跳转词是不是只是目标词的一个简单变形，比如 advocating <=> advocate，在forms-En.txt中查找
                            if z:  # 如果是就跳过，不保存。因为后面会直接为单词原型生成一系列跳转词。比如advocate举例，若不这样处理，那结果就是advocating, advocates等等近乎一样的词条都有advocate词条的解释，占用大量空间
                                print('变形词跳过：%s' % Jumping_word)
                                continue
                            print('跳转词意项写入：%s' % Jumping_word)
                            new_line = pattern.sub(
                                '\\1' + '\t' + matched, line
                            )  #否则替换成“跳转词   目标词的意项内容”的形式，如此kindle方能解决kindle查词出现@@@LINK=XXXX的问题
                            f2.write(new_line)  #写入

                else:  #匹配不成功，说面是“单词 解释“行，跳过，直接输出
                    f2.write(line)
                    print('写入解释项：%s' % line.split('\t')[0])
            except:  #异常行保存
                f3.write(line)

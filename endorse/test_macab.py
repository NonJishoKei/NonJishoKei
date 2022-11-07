import os
import MeCab

dic_path = os.getcwd()+r'\unidic-cwj-3.1.1'+'\\'
tagger = MeCab.Tagger(
    '-r nul -d {} -Ochasen'.format(dic_path).replace('\\', '/'))

text = "あいしる"
print(type(tagger.parse(text)))
print(tagger.parse(text).split("\n"))
print(tagger.parse(text))

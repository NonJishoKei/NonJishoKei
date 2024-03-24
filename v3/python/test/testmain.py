""" main.py 单元测试"""

import unittest

from main import scan_input_string


class TestMain(unittest.TestCase):
    """测试 main.py 中的方法"""

    def test_scan_input_string(self):
        """测试 main.py 中的 scan_input_string 方法"""
        # 形容词测试
        # 高か
        self.assertIn("高い", scan_input_string("高かろう"))
        self.assertIn("高い", scan_input_string("高かった"))
        self.assertIn("高い", scan_input_string("高かったり"))

        # 高く
        # 高くて
        self.assertIn("高い", scan_input_string("高くて"))
        # 高くない
        self.assertIn("高い", scan_input_string("高くない"))
        # 高くても
        self.assertIn("高い", scan_input_string("高くても"))
        # 高くても
        self.assertIn("高い", scan_input_string("高くても"))
        # 高くとも
        self.assertIn("高い", scan_input_string("高くとも"))
        # 高くなる
        self.assertIn("高い", scan_input_string("高くなる"))
        # 高くする
        self.assertIn("高い", scan_input_string("高くする"))

        # 高け
        # 高ければ
        self.assertIn("高い", scan_input_string("高ければ"))

        # 高さ
        self.assertIn("高い", scan_input_string("高さ"))

        # 高す
        self.assertIn("高い", scan_input_string("高すぎる"))

        # 高み
        self.assertIn("高い", scan_input_string("高み"))

        # 高そう
        self.assertIn("高い", scan_input_string("高そう"))

        # 一段动词测试
        # 食べろ
        self.assertIn("食べる", scan_input_string("食べろ"))
        # 食べよ
        self.assertIn("食べる", scan_input_string("食べよう"))
        # 食べな
        self.assertIn("食べる", scan_input_string("食べない"))
        self.assertIn("食べる", scan_input_string("食べなかった"))
        self.assertIn("食べる", scan_input_string("食べながら"))
        self.assertIn("食べる", scan_input_string("食べなければならない"))
        # 食べま
        self.assertIn("食べる", scan_input_string("食べます"))
        self.assertIn("食べる", scan_input_string("食べません"))
        self.assertIn("食べる", scan_input_string("食べました"))
        self.assertIn("食べる", scan_input_string("食べませんでした"))
        self.assertIn("食べる", scan_input_string("食べましょう"))
        # 食べた
        self.assertIn("食べる", scan_input_string("食べた"))
        self.assertIn("食べる", scan_input_string("食べたい"))
        self.assertIn("食べる", scan_input_string("食べたくない"))
        # インドでは牛肉を売ったり、食べたりしたと思われた人が殺害される事件も起きている。
        # https://yourei.jp/%E9%A3%9F%E3%81%B9%E3%82%8B
        self.assertIn("食べる", scan_input_string("食べたり"))
        # 食べれ
        self.assertIn("食べる", scan_input_string("食べれる"))
        self.assertIn("食べる", scan_input_string("食べれない"))
        self.assertIn("食べる", scan_input_string("食べれば"))
        # 食べて
        self.assertIn("食べる", scan_input_string("食べている"))
        self.assertIn("食べる", scan_input_string("食べていない"))
        self.assertIn("食べる", scan_input_string("食べていた"))
        self.assertIn("食べる", scan_input_string("食べても"))
        # 食べら
        self.assertIn("食べる", scan_input_string("食べられる"))
        # 食べさ
        self.assertIn("食べる", scan_input_string("食べさせる"))
        # (疲れているあなたのために（東日本大震災）：こころの散歩道)
        # 寝食を忘れている人がいたら、無理にでも、寝かせましょう。　 食べさせましょう。
        # http://www.n-seiryo.ac.jp/~usui/saigai/2011sanrikuoki_eq/tukare.html
        self.assertIn("食べる", scan_input_string("食べさせましょう。"))
        # 食べず
        # https://ja.hinative.com/questions/24501639
        self.assertIn("食べる", scan_input_string("食べずに、待っていてください。"))
        # 食べぬ
        self.assertIn("食べる", scan_input_string("食べぬけど、待っていてください。"))
        # 食べ、
        # https://yourei.jp/%E9%A3%9F%E3%81%B9%E3%82%8B
        # 昼はそばなどを軽く食べ、夜は酒の肴をあてにひたすら酒を飲んでいた。
        self.assertIn("食べる", scan_input_string("食べ、夜は酒の肴をあてにひたす"))
        # 食べと
        # https://zh.hinative.com/questions/19258409
        # 食べといて=食べておいて＝食べてください
        self.assertIn("食べる", scan_input_string("食べといて"))
        # 食べち
        self.assertIn("食べる", scan_input_string("食べちゃった"))
        # 食べせ
        # 「食べせる」より、「食べさせる」のほうが正しいと思うが、「あるもの (存在するもの) すべては正しい（Whatever is, is right.）」
        # https://tsukubawebcorpus.jp/headword/V.00051/#SS57
        # (赤ちゃんの月齢別ＱÅ集〜育児の心得〜)
        # 離乳食はほしがるだけ食べせても大丈夫？
        self.assertIn("食べる", scan_input_string("食べせても大丈夫"))
        # 日本人がフランスに住むと食生活はこう変わる！　海外のグルメ事情　文化交流　ヨーロッパ　EU　留学　 メシクエブログ〜それいけ神動画〜/ウェブリブログ)
        # 何となくトンペー食べせずにはいられなくなりました。
        self.assertIn("食べる", scan_input_string("食べせずにはいられなくなりました。"))
        # (お客様の声 | 餃子通販 ぎょうざの宝永　札幌本店)
        # 忙しくお仕事大変でしょうがお体大事になさって、もっともっと美味しいぎょうざを研究なさって私達に食べせて下さい
        self.assertIn("食べる", scan_input_string("食べせて下さい"))
        # 食べん
        # https://zh.hinative.com/questions/23333121
        # 「食べんの？」は、普通は「食べるの？」の「る」が「ん」になったものですが、関西の方言などで「食べないの？」という意味になることもあります
        self.assertIn("食べる", scan_input_string("食べんの？"))

        # 複合動詞
        self.assertIn("食べる", scan_input_string("食べ始める"))
        # これ美味しそうですねえ。　 食べに行きたいなあ。
        # http://ameblo.jp/closdesoleil/entry-11091942958.html
        self.assertIn("食べる", scan_input_string("食べに行きたいなあ。"))

        self.assertIn("教える", scan_input_string("教えざるを得ない"))

        # カ行五段动词
        # 書か-ない/ず/ぬ/れる/せる/せられる/される
        self.assertIn("書く", scan_input_string("書かない"))
        self.assertIn("書く", scan_input_string("書かず"))
        self.assertIn("書く", scan_input_string("書かぬ"))
        self.assertIn("書く", scan_input_string("書かれる"))
        self.assertIn("書く", scan_input_string("書かせる"))
        self.assertIn("書く", scan_input_string("書かせられる"))
        self.assertIn("書く", scan_input_string("書かされる"))
        # 書き-たい/ます/そうだ/ながら/つつ
        self.assertIn("書く", scan_input_string("書きたい"))
        self.assertIn("書く", scan_input_string("書きます"))
        self.assertIn("書く", scan_input_string("書きそうだ"))
        self.assertIn("書く", scan_input_string("書きながら"))
        self.assertIn("書く", scan_input_string("書きつつ"))
        # 書い-て/た/たり/ても
        self.assertIn("書く", scan_input_string("書いて"))
        self.assertIn("書く", scan_input_string("書いた"))
        self.assertIn("書く", scan_input_string("書いたり"))
        self.assertIn("書く", scan_input_string("書いても"))
        # 書け・書け-ば/る
        self.assertIn("書く", scan_input_string("書け"))
        self.assertIn("書く", scan_input_string("書けば"))
        self.assertIn("書く", scan_input_string("書ける"))
        # 書こう
        self.assertIn("書く", scan_input_string("書こう"))

        # ガ行
        # 泳が-ない/ず/ぬ/れる/せる/せられる/される
        self.assertIn("泳ぐ", scan_input_string("泳がない"))
        self.assertIn("泳ぐ", scan_input_string("泳がず"))
        self.assertIn("泳ぐ", scan_input_string("泳がぬ"))
        self.assertIn("泳ぐ", scan_input_string("泳がれる"))
        self.assertIn("泳ぐ", scan_input_string("泳がせる"))
        self.assertIn("泳ぐ", scan_input_string("泳がせられる"))
        self.assertIn("泳ぐ", scan_input_string("泳がされる"))
        # 泳ぎ-たい/ます/そうだ/ながら/つつ
        self.assertIn("泳ぐ", scan_input_string("泳ぎたい"))
        self.assertIn("泳ぐ", scan_input_string("泳ぎます"))
        self.assertIn("泳ぐ", scan_input_string("泳ぎそうだ"))
        self.assertIn("泳ぐ", scan_input_string("泳ぎながら"))
        self.assertIn("泳ぐ", scan_input_string("泳ぎつつ"))
        # 泳い-で/だ/だり/でも
        self.assertIn("泳ぐ", scan_input_string("泳いで"))
        self.assertIn("泳ぐ", scan_input_string("泳いだ"))
        self.assertIn("泳ぐ", scan_input_string("泳いだり"))
        self.assertIn("泳ぐ", scan_input_string("泳いでも"))
        # 泳げ・泳げ-ば/る
        self.assertIn("泳ぐ", scan_input_string("泳げ"))
        self.assertIn("泳ぐ", scan_input_string("泳げば"))
        self.assertIn("泳ぐ", scan_input_string("泳げる"))
        # 泳ごう
        self.assertIn("泳ぐ", scan_input_string("泳ごう"))

        # サ行
        # 指さ-ない/ず/ぬ/れる/せる/せられる
        self.assertIn("指す", scan_input_string("指さない"))
        self.assertIn("指す", scan_input_string("指さず"))
        self.assertIn("指す", scan_input_string("指さぬ"))
        self.assertIn("指す", scan_input_string("指される"))
        self.assertIn("指す", scan_input_string("指させる"))
        self.assertIn("指す", scan_input_string("指させられる"))
        # 指し-たい/ます/そうだ/ながら/つつ/て/た/たり/ても
        self.assertIn("指す", scan_input_string("指したい"))
        self.assertIn("指す", scan_input_string("指します"))
        self.assertIn("指す", scan_input_string("指しそうだ"))
        self.assertIn("指す", scan_input_string("指しながら"))
        self.assertIn("指す", scan_input_string("指しつつ"))
        self.assertIn("指す", scan_input_string("指して"))
        self.assertIn("指す", scan_input_string("指した"))
        self.assertIn("指す", scan_input_string("指したり"))
        self.assertIn("指す", scan_input_string("指しても"))
        # 指せ・指せ-ば/る
        self.assertIn("指す", scan_input_string("指せ"))
        self.assertIn("指す", scan_input_string("指せば"))
        self.assertIn("指す", scan_input_string("指せる"))
        # 指そう
        self.assertIn("指す", scan_input_string("指そう"))

        # タ行
        # 立た-ない/ず/ぬ/れる/せる/せられる/される
        self.assertIn("立つ", scan_input_string("立たない"))
        self.assertIn("立つ", scan_input_string("立たず"))
        self.assertIn("立つ", scan_input_string("立たぬ"))
        self.assertIn("立つ", scan_input_string("立たされる"))
        self.assertIn("立つ", scan_input_string("立たさせる"))
        self.assertIn("立つ", scan_input_string("立たさせられる"))
        self.assertIn("立つ", scan_input_string("立たされる"))
        # 立ち-たい/ます/そうだ/ながら/つつ
        self.assertIn("立つ", scan_input_string("立ちたい"))
        self.assertIn("立つ", scan_input_string("立ちます"))
        self.assertIn("立つ", scan_input_string("立ちそうだ"))
        self.assertIn("立つ", scan_input_string("立ちながら"))
        self.assertIn("立つ", scan_input_string("立ちつつ"))
        # 立て・立てば/る
        self.assertIn("立つ", scan_input_string("立て"))
        self.assertIn("立つ", scan_input_string("立てば"))
        self.assertIn("立つ", scan_input_string("立てる"))
        # 立とう
        self.assertIn("立つ", scan_input_string("立とう"))
        # 立って/た/たり/ても
        self.assertIn("立つ", scan_input_string("立って"))
        self.assertIn("立つ", scan_input_string("立った"))
        self.assertIn("立つ", scan_input_string("立ったり"))
        self.assertIn("立つ", scan_input_string("立っても"))

        # ナ行
        # 死な-ない/ず/ぬ/れる/せる/せられる/される
        self.assertIn("死ぬ", scan_input_string("死なない"))
        self.assertIn("死ぬ", scan_input_string("死なず"))
        self.assertIn("死ぬ", scan_input_string("死なぬ"))
        self.assertIn("死ぬ", scan_input_string("死なれる"))
        self.assertIn("死ぬ", scan_input_string("死なせる"))
        self.assertIn("死ぬ", scan_input_string("死なせられる"))
        self.assertIn("死ぬ", scan_input_string("死なされる"))
        # 死に-たい/ます/そうだ/ながら/つつ
        self.assertIn("死ぬ", scan_input_string("死にたい"))
        self.assertIn("死ぬ", scan_input_string("死にます"))
        self.assertIn("死ぬ", scan_input_string("死にそうだ"))
        self.assertIn("死ぬ", scan_input_string("死にながら"))
        self.assertIn("死ぬ", scan_input_string("死につつ"))
        # 死ね・死ね-ば/る
        self.assertIn("死ぬ", scan_input_string("死ね"))
        self.assertIn("死ぬ", scan_input_string("死ねば"))
        self.assertIn("死ぬ", scan_input_string("死ねる"))
        # 死の-う
        self.assertIn("死ぬ", scan_input_string("死のう"))
        # 中島美嘉 - 僕が死のうと思ったのは
        self.assertIn("死ぬ", scan_input_string("死のうと思ったのは"))
        # 死ん-で/だ/だり/でも
        self.assertIn("死ぬ", scan_input_string("死ん"))
        self.assertIn("死ぬ", scan_input_string("死んで"))
        self.assertIn("死ぬ", scan_input_string("死んだ"))
        self.assertIn("死ぬ", scan_input_string("死んだり"))
        self.assertIn("死ぬ", scan_input_string("死んでも"))

        # バ行
        # 飛ば-ない/ず/ぬ/れる/せる/せられる/される
        self.assertIn("飛ぶ", scan_input_string("飛ば"))
        self.assertIn("飛ぶ", scan_input_string("飛ばない"))
        self.assertIn("飛ぶ", scan_input_string("飛ばず"))
        self.assertIn("飛ぶ", scan_input_string("飛ばぬ"))
        self.assertIn("飛ぶ", scan_input_string("飛ばれる"))
        self.assertIn("飛ぶ", scan_input_string("飛ばせる"))
        self.assertIn("飛ぶ", scan_input_string("飛ばせられる"))
        self.assertIn("飛ぶ", scan_input_string("飛ばされる"))
        # 飛び-たい/ます/そうだ/ながら/つつ
        self.assertIn("飛ぶ", scan_input_string("飛びたい"))
        self.assertIn("飛ぶ", scan_input_string("飛びます"))
        self.assertIn("飛ぶ", scan_input_string("飛びそうだ"))
        self.assertIn("飛ぶ", scan_input_string("飛びながら"))
        self.assertIn("飛ぶ", scan_input_string("飛びつつ"))
        # 飛べ・飛べ-ば/る
        self.assertIn("飛ぶ", scan_input_string("飛べ"))
        self.assertIn("飛ぶ", scan_input_string("飛べば"))
        self.assertIn("飛ぶ", scan_input_string("飛べる"))
        # 飛ぼう
        self.assertIn("飛ぶ", scan_input_string("飛ぼう"))
        # 飛ん-で/だ/だり/でも
        self.assertIn("飛ぶ", scan_input_string("飛んで"))
        self.assertIn("飛ぶ", scan_input_string("飛んだ"))
        self.assertIn("飛ぶ", scan_input_string("飛んだり"))
        self.assertIn("飛ぶ", scan_input_string("飛んでも"))

        # マ行
        # 読ま-ない/ず/ぬ/れる/せる/せられる/される
        self.assertIn("読む", scan_input_string("読まない"))
        self.assertIn("読む", scan_input_string("読まず"))
        self.assertIn("読む", scan_input_string("読まぬ"))
        self.assertIn("読む", scan_input_string("読まれる"))
        self.assertIn("読む", scan_input_string("読ませる"))
        self.assertIn("読む", scan_input_string("読ませられる"))
        self.assertIn("読む", scan_input_string("読まされる"))
        # 読み-たい/ます/そうだ/ながら/つつ
        self.assertIn("読む", scan_input_string("読みたい"))
        self.assertIn("読む", scan_input_string("読みます"))
        self.assertIn("読む", scan_input_string("読みそうだ"))
        self.assertIn("読む", scan_input_string("読みながら"))
        self.assertIn("読む", scan_input_string("読みつつ"))
        # 読め・読め-る/ば
        self.assertIn("読む", scan_input_string("読め"))
        self.assertIn("読む", scan_input_string("読める"))
        self.assertIn("読む", scan_input_string("読めば"))
        # 読もう
        self.assertIn("読む", scan_input_string("読もう"))
        # 読ん-で/だ/だり/でも
        self.assertIn("読む", scan_input_string("読んで"))
        self.assertIn("読む", scan_input_string("読んだ"))
        self.assertIn("読む", scan_input_string("読んだり"))
        self.assertIn("読む", scan_input_string("読んでも"))

        # ラ行
        # 帰ら-ない/ず/ぬ/れる/せる/せられる/される
        self.assertIn("帰る", scan_input_string("帰らない"))
        self.assertIn("帰る", scan_input_string("帰らず"))
        self.assertIn("帰る", scan_input_string("帰らぬ"))
        self.assertIn("帰る", scan_input_string("帰られる"))
        self.assertIn("帰る", scan_input_string("帰らせる"))
        self.assertIn("帰る", scan_input_string("帰らせられる"))
        self.assertIn("帰る", scan_input_string("帰らされる"))
        # 帰り-たい/ます/そうだ/ながら/つつ
        self.assertIn("帰る", scan_input_string("帰りたい"))
        self.assertIn("帰る", scan_input_string("帰ります"))
        self.assertIn("帰る", scan_input_string("帰りそうだ"))
        self.assertIn("帰る", scan_input_string("帰りながら"))
        self.assertIn("帰る", scan_input_string("帰りつつ"))
        # 帰れ-ば/る
        self.assertIn("帰る", scan_input_string("帰れば"))
        self.assertIn("帰る", scan_input_string("帰れる"))
        # 帰ろう
        self.assertIn("帰る", scan_input_string("帰ろう"))
        # 帰っ-て/た/たり/ても
        self.assertIn("帰る", scan_input_string("帰って"))
        self.assertIn("帰る", scan_input_string("帰った"))
        self.assertIn("帰る", scan_input_string("帰ったり"))
        self.assertIn("帰る", scan_input_string("帰っても"))

        # ワア行
        # 笑わ-ない/ず/ぬ/れる/せる/せられる/される
        self.assertIn("笑う", scan_input_string("笑わない"))
        self.assertIn("笑う", scan_input_string("笑わず"))
        self.assertIn("笑う", scan_input_string("笑わぬ"))
        self.assertIn("笑う", scan_input_string("笑われる"))
        self.assertIn("笑う", scan_input_string("笑わせる"))
        self.assertIn("笑う", scan_input_string("笑わせられる"))
        self.assertIn("笑う", scan_input_string("笑わされる"))
        # 笑い-たい/た/たり/ても
        self.assertIn("笑う", scan_input_string("笑いたい"))
        self.assertIn("笑う", scan_input_string("笑いた"))
        self.assertIn("笑う", scan_input_string("笑いたり"))
        self.assertIn("笑う", scan_input_string("笑いても"))
        # 笑え・笑え-る/ば
        self.assertIn("笑う", scan_input_string("笑え"))
        self.assertIn("笑う", scan_input_string("笑える"))
        self.assertIn("笑う", scan_input_string("笑えば"))
        # 問お
        # 「問おう。あなたがわたしのマスターか」
        self.assertIn("問う", scan_input_string("問おう"))


if __name__ == "__main__":
    unittest.main()

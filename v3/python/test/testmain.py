"""单元测试框架 """

import unittest
import main


class TestMain(unittest.TestCase):
    """
    单元测试，考虑到时间成本，部分测试的优先度不高，暂时用TODO进行标记，之后结合用户反馈进行修复。

    """

    def convert_repe_single_sign(self):
        """单字符重复符号"""
        # https://ja.wikipedia.org/wiki/%E8%B8%8A%E3%82%8A%E5%AD%97
        # 々
        self.assertEqual("正正堂堂", main.convert_repe_single_sign("正々堂々"))
        self.assertEqual("段段", main.convert_repe_single_sign("段々"))
        self.assertEqual("赤裸裸", main.convert_repe_single_sign("赤裸々"))
        self.assertEqual("告別式式場", main.convert_repe_single_sign("告別式々場"))

        # 非正常输入测试
        self.assertEqual("正正堂", main.convert_repe_single_sign("正々堂"))
        self.assertEqual("々段", main.convert_repe_single_sign("々段"))
        self.assertEqual("々堂堂", main.convert_repe_single_sign("々堂々"))
        # TODO 极少数特例
        # self.assertEqual("複複複線", main.convert_repe_single_sign("複々々線"))
        # self.assertEqual("部分部分", main.convert_repe_single_sign("部分々々"))
        # TODO 古く（奈良時代）は記法が異なり
        # self.assertEqual("部分部分", main.convert_repe_single_sign("部々分々"))

        # 〻 現代では「〻」は「々」と書き換えられ、主に縦書きの文章に用いる。
        self.assertEqual("屡屡", main.convert_repe_single_sign("屡〻"))

        # ゝ 平仮名繰返し記号
        self.assertEqual("ここ", main.convert_repe_single_sign("こゝ"))
        self.assertEqual("こころ", main.convert_repe_single_sign("こゝろ"))
        self.assertEqual("わななかした", main.convert_repe_single_sign("わなゝかした"))

        # ヽ 片仮名繰返し記号
        self.assertEqual("ハハヽヽ", main.convert_repe_single_sign("ハヽヽヽ"))
        # 曾ては、妣 （ ハヽ ） が国として、恋慕の思ひをよせた此国は、現実の悦楽に満ちた楽土として、見かはすばかりに変つて了うた。
        # https://www.aozora.gr.jp/cards/000933/files/13212_14465.html
        self.assertEqual("ハハ", main.convert_repe_single_sign("ハヽ"))

    def test_convert_repe_single_daku_sign(self):
        """单字符浊音重复符号"""
        # https://ja.wikipedia.org/wiki/%E8%B8%8A%E3%82%8A%E5%AD%97#%E3%82%9D%E3%81%A8%E3%83%BD%EF%BC%88%E4%B8%80%E3%81%AE%E5%AD%97%E7%82%B9%EF%BC%89
        self.assertEqual("ただ", main.convert_repe_single_daku_sign("たゞ"))
        self.assertEqual("みすず飴", main.convert_repe_single_daku_sign("みすゞ飴"))
        # FIXME 注意这个字符的定义：代表一个浊音假名，当前浊音符前的第一个假名就是浊音时，直接拼接返回即可
        # self.assertEqual("ぶぶ漬け", main.convert_repe_single_daku_sign("ぶゞ漬け"))

    def test_convert_repeated_double_sign(self):
        """多字符重复符号"""
        # ／＼
        # Unicodeのブロックでは、収録されているの〳〵だが、
        # https://ja.wikipedia.org/wiki/CJK%E3%81%AE%E8%A8%98%E5%8F%B7%E5%8F%8A%E3%81%B3%E5%8F%A5%E8%AA%AD%E7%82%B9
        # 青空文庫では「／＼」を使っている。
        # https://www.aozora.gr.jp/cards/001383/files/56641_59496.html
        # 時々両国で催される刺青会では参会者おの／＼肌を叩いて、互に奇抜な意匠を誇り合い、評しあった。
        self.assertEqual("おのおの", main.convert_repe_double_sign("おの／＼"))
        # 〳〵
        self.assertEqual("おのおの", main.convert_repe_double_sign("おの〳〵"))
        self.assertEqual(
            "くり返しくり返し", main.convert_repe_double_sign("くり返し〳〵")
        )
        # 〱
        self.assertEqual("見る見る", main.convert_repe_double_sign("見る〱"))
        # https://ja.wikipedia.org/wiki/%E8%B8%8A%E3%82%8A%E5%AD%97#%E3%80%B1%EF%BC%88%E3%81%8F%E3%81%AE%E5%AD%97%E7%82%B9%EF%BC%89
        self.assertEqual(
            "どうしてどうして", main.convert_repe_double_sign("どうして〱")
        )
        # 非正常输入测试
        self.assertEqual("おの／＼肌", main.convert_repe_double_sign("おの／＼肌"))

    def test_convert_repeated_double_daku_sign(self):
        """多字符浊音符号"""
        # https://ja.wikisource.org/wiki/%E3%81%8F%E3%82%8A%E3%81%8B%E3%81%B8%E3%81%97%E7%AC%A6%E5%8F%B7%E3%81%AE%E4%BD%BF%E3%81%B2%E6%96%B9
        self.assertEqual("散り散り", main.convert_repe_double_daku_sign("散り〴〵"))
        self.assertEqual(
            "代わる代わる", main.convert_repe_double_daku_sign("代わる〴〵")
        )
        # 请注意，这个样例并非来自真实的使用场景，仅用作测试
        self.assertEqual(
            "かわるがわる", main.convert_repe_double_daku_sign("かわる〴〵")
        )
        # https://www.aozora.gr.jp/cards/001383/files/56641_59496.html
        # 彼は今始めて女の妙相みょうそうをしみ／″＼味わう事が出来た。
        self.assertEqual("しみじみ", main.convert_repe_double_daku_sign("しみ／″＼"))
        # 其の瞳は夕月の光を増すように、だん／＼と輝いて男の顔に照った。
        # TODO　以下のURLでは、
        # https://ja.wikipedia.org/wiki/%E8%B8%8A%E3%82%8A%E5%AD%97#%E3%80%B1%EF%BC%88%E3%81%8F%E3%81%AE%E5%AD%97%E7%82%B9%EF%BC%89
        # 濁点の付く文字を繰り返す場合は、濁点の付いていない「くの字点」を用いる場合と、濁点の付いている「くの字点」を用いる場合がある。
        # 濁点の付く文字を繰り返すが、繰り返し箇所は濁点がつかない場合は、濁点の付いていない「くの字点」を用いる（擬音などでは少ないが児童向け文学などで漢字を仮名表記する場合に用いられる）。
        # self.assertEqual("だんだん", main.convert_repe_double_daku_sign("だん／＼"))
        # self.assertEqual("だんだん", main.convert_repe_double_daku_sign("だん／″＼"))

    def test_del_ocr_error(self):
        """注意空格往往不止一个"""
        self.assertEqual("食べた", main.del_ocr_error(" 食べた"))
        self.assertEqual("食べた", main.del_ocr_error("食 べた"))
        self.assertEqual("食べた", main.del_ocr_error("食べた "))
        self.assertEqual("食べた", main.del_ocr_error(" 食べた "))
        self.assertEqual("食べた", main.del_ocr_error(" 食 べ た "))
        self.assertEqual("", main.del_ocr_error(" "))


if __name__ == "__main__":
    unittest.main()

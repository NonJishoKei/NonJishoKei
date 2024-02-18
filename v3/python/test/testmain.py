"""单元测试框架 """

import unittest
import main


class TestMain(unittest.TestCase):
    """
    单元测试，考虑到时间成本，部分测试的优先度不高，暂时用TODO进行标记，之后结合用户反馈进行修复。

    """

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
        """注意空格往往不止一个
        """
        self.assertEqual("食べた", main.del_ocr_error(" 食べた"))
        self.assertEqual("食べた", main.del_ocr_error("食 べた"))
        self.assertEqual("食べた", main.del_ocr_error("食べた "))
        self.assertEqual("食べた", main.del_ocr_error(" 食べた "))
        self.assertEqual("食べた", main.del_ocr_error(" 食 べ た "))
        self.assertEqual("", main.del_ocr_error(" "))


if __name__ == "__main__":
    unittest.main()

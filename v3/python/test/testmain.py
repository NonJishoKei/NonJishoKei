"""单元测试框架 """

import unittest
import main


class TestMain(unittest.TestCase):
    """
    单元测试，考虑到时间成本，部分测试的优先度不高。

    """

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

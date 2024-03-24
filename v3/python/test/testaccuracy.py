""" 遍历"""

import logging
import os
import re
import sys
import time
from textwrap import dedent

from main import scan_input_string


def init_logging(logging_level: int = logging.DEBUG):
    """Initialize log configuration
        初始化日志配置

    Args:
        logging_level (str, optional): Set log level. Defaults to logging.DEBUG.
    """
    logging.basicConfig(
        handlers=[
            logging.FileHandler(
                f"{time.strftime('%Y-%m-%d', time.localtime()) }.log", encoding="utf-8"
            ),
            logging.StreamHandler(sys.stderr),
        ],
        level=logging.DEBUG,
        format="%(asctime)s %(filename)s %(levelname)s %(message)s",
        datefmt="%a %d %b %Y %H:%M:%S",
    )
    logging.disable(logging_level)


def test_convert_conjugate(test_file: str, converted_file: str):
    """Covers all collections of nonjishokei
        覆盖所有收集的非辞書型

    Args:
        test_file (str): Includes all nonjishokei file test paths.
        converted_file (str): Path where test results are saved.
    """
    with open(test_file, "r", encoding="utf-8") as f, open(
        converted_file, "w", encoding="utf-8"
    ) as s:
        done_line_count = 0
        all_line_count = len(f.readlines())
        f.seek(0)
        for line in f.readlines():
            line = line.replace("\n", "")
            input_text = line.partition(":")[0]
            result_text = ",".join(scan_input_string(input_text))
            s.write(result_text + " " + line + "\n")
            done_line_count += 1
            progress_percent = (done_line_count / all_line_count) * 100
            logging.info("progress percent: %s", progress_percent)


def cal_accuracy(converted_result_file: str, accuracy_result_file: str) -> str:
    """Calculate the ratio of derivation results to correct answers.
        计算推导结果与正确答案的比例

    Args:
        converted_result (str): Includes all converted result file test paths.
        accuracy_result (str): Path where calculate results are saved.

    Returns:
        str: The ratio of derivation results to correct answers.
    """
    reg = re.compile(
        r"(?P<converted_jishokei>.*?) (?P<nonjishokei>.*?)\:(?P<jishokei>.*?)\n"
    )
    true_count = 0
    false_count = 0
    with open(converted_result_file, "r", encoding="utf-8") as f, open(
        accuracy_result_file, "w", encoding="utf-8"
    ) as s:
        for line in f.readlines():
            match = re.search(reg, line)
            if not match:
                logging.debug("the line: %s is not match", line)
                s.write("False\n")
                false_count += 1
                continue
            converted_result_list = match.group("converted_jishokei").split(",")
            result_template = dedent(
                f"""converted_jishokei<{match.group('converted_jishokei')}>
                    nonjishokei<{match.group('nonjishokei')}>
                    jishokei<{match.group("jishokei")}>"""
            )
            if match.group("jishokei") not in converted_result_list:
                false_count += 1
                logging.debug("the converted jishokei: %s is false", line)
                s.write(f"False {result_template.strip()}\n")
            else:
                true_count += 1
                s.write(f"True {result_template.strip()}\n")
        return str(round((true_count / (true_count + false_count)) * 100, 3)) + "%"


init_logging()
CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))

STAR_TIME = time.perf_counter()
test_convert_conjugate(
    os.path.join(CURRENT_PATH, "temp.txt"), os.path.join(CURRENT_PATH, "save.txt")
)
END_TIME = time.perf_counter()
logging.info(
    "The time required for this test :%s millisecond",
    str(round((END_TIME - STAR_TIME) * 1000, 3)),
)

ACCURACY = cal_accuracy(
    os.path.join(CURRENT_PATH, "save.txt"), os.path.join(CURRENT_PATH, "review_v3.txt")
)
logging.info("Accuracy of this algorithm: %s ", ACCURACY)

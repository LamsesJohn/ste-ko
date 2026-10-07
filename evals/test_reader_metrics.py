import unittest

from reader_metrics import analyze, hard_violations, split_sentences, strip_code


class ReaderMetricsTest(unittest.TestCase):
    def test_code_blocks_are_ignored(self):
        text = "결론은 이렇다.\n```\nlong code line with ; and — inside\n```\n끝."
        self.assertNotIn("code", strip_code(text))
        m = analyze(text)
        self.assertEqual(m["semicolon"], 0)
        self.assertEqual(m["em_dash"], 0)

    def test_list_items_count_as_sentences(self):
        text = "1. 첫 단계를 실행한다.\n2. 둘째 단계를 실행한다.\n- 셋째 항목이다."
        self.assertEqual(len(split_sentences(text)), 3)

    def test_long_sentence_is_flagged(self):
        long_sentence = " ".join(["단어"] * 30) + "."
        m = analyze(long_sentence)
        self.assertEqual(m["sentences_over_limit"], 1)
        self.assertEqual(m["max_eojeol_in_sentence"], 30)
        self.assertGreater(hard_violations(m), 0)

    def test_a_list_does_not_hide_a_long_sentence(self):
        long_item = "- " + " ".join(["단어"] * 30)
        self.assertEqual(analyze(long_item)["sentences_over_limit"], 1)

    def test_form_markers_are_counted(self):
        text = "**결론**이다; 그렇다 — 맞다.\n# 제목\n| a | b |\n|---|---|\n| 1 | 2 |"
        m = analyze(text)
        self.assertEqual(m["bold_spans"], 1)
        self.assertEqual(m["semicolon"], 1)
        self.assertEqual(m["em_dash"], 1)
        self.assertEqual(m["headers"], 1)
        self.assertEqual(m["table_rows"], 3)

    def test_stock_phrases_and_nominalizations(self):
        text = "다양한 분야에서 분석을 수행하여 효율적으로 처리한다. 좋은 질문입니다."
        m = analyze(text)
        self.assertGreaterEqual(m["stock_phrases"], 2)
        self.assertEqual(m["nominalizations"], 1)
        self.assertEqual(m["openers"], 1)

    def test_clean_text_has_no_hard_violations(self):
        text = "원인은 포트 설정이다. 서버가 5432 포트를 열지 않았다.\n\n1. 설정 파일을 연다.\n2. 포트를 확인한다."
        self.assertEqual(hard_violations(analyze(text)), 0)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import mock_open, patch


from lab4 import calc_total_bytes, read_chunks, check_lines


class UnitTestCase(unittest.TestCase):
    def setUp(self):
        self.sample_log = (
            '213.109.238.193 - - [07/May/2017:00:08:35 +0300] "GET /login/index.php HTTP/1.0" 200 21351 "http://learn.topnode.if.ua/question/edit.php" "Mozilla/5.0"\n'
            '213.109.238.193 - - [07/May/2017:00:08:52 +0300] "POST /login/index.php HTTP/1.0" 303 - "http://learn.topnode.if.ua/login/index.php" "Mozilla/5.0"\n'
        )

    def test_log_lines(self):
        """Тестування парсингу рядків логу та розрахунку розміру запиту й переданих байтів"""
        lines = self.sample_log.strip().splitlines(True)
        results = list(check_lines(lines))

        self.assertEqual(len(results), 2)

        record1, sent1 = results[0]
        self.assertEqual(record1, len(lines[0].encode("utf-8")))
        self.assertEqual(sent1, 21351)

        record2, sent2 = results[1]
        self.assertEqual(record2, len(lines[1].encode("utf-8")))
        self.assertEqual(sent2, 0)

    def test_read_chunks(self):
        """Тестування зчитування файла шматками (chunks) за допомогою mock_open"""
        mk_open = mock_open(read_data="1234567890")
        with patch("builtins.open", mk_open):
            with open("dummy.log", "r") as f:
                chunk = list(read_chunks(f, chunk_size=3))
                self.assertEqual(chunk, ["123", "456", "789", "0"])

    def test_calc_log_traffic(self):
        """Тестування підрахунку сумарного трафіку"""
        mk_open = mock_open(read_data=self.sample_log)
        with patch("builtins.open", mk_open):
            total_bytes = calc_total_bytes("dummy.log")
            self.assertIsNotNone(total_bytes)


if __name__ == "__main__":
    unittest.main()
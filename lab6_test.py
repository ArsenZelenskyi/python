import unittest
import subprocess
import sys
from click.testing import CliRunner
from lab6 import HourlyWorker, FixedWorker, FopWorker, ContractWorker, sort_workers, cli


class TestLab6(unittest.TestCase):
    def test_workers_and_sort(self):
        w1 = HourlyWorker("1", "В", 100, 166.4)
        w2 = FixedWorker("2", "Б", 50000)
        w3 = FopWorker("3", "Г", 10, group=3, hours=100)
        w4 = ContractWorker("4", "А", 2.0, 1000)

        self.assertEqual((round(w1.get_salary(), 2), round(w1.get_tax(), 2)), (16640.0, 3244.8))
        self.assertEqual((w2.get_salary(), w2.get_tax()), (50000.0, 9750.0))
        self.assertEqual((round(w3.get_salary(), 2), round(w3.get_tax(), 2)), (1100.0, 1815.0))
        self.assertEqual((w4.get_salary(), w4.get_tax()), (2000.0, 2150.0))

        self.assertEqual(sort_workers([w1, w2, w3, w4]), [w2, w1, w4, w3])

    def test_cli(self):
        runner = CliRunner()
        for cmd in [['list'], ['filter-fop-group', '--group', '3'], ['filter-income', '--min-income', '1000'], ['filter-taxes', '--min-tax', '1000']]:
            self.assertEqual(runner.invoke(cli, cmd).exit_code, 0)

    def test_subprocess(self):
        self.assertEqual(subprocess.call([sys.executable, 'lab6.py', '--help']), 0)


if __name__ == '__main__':
    unittest.main()
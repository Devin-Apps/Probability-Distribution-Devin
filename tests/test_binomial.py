import unittest
from binomial import Binomial

class TestBinomial(unittest.TestCase):
    def setUp(self):
        self.binomial = Binomial(0.4, 20)

    def test_mean_calculation(self):
        self.assertEqual(self.binomial.calculate_mean(), 8)

    def test_stdev_calculation(self):
        self.assertEqual(round(self.binomial.calculate_stdev(), 2), 2.19)

    def test_pmf_calculation(self):
        self.assertAlmostEqual(self.binomial.pmf(5), 0.07465, places=5)
        self.assertAlmostEqual(self.binomial.pmf(10), 0.11714, places=5)

    def test_replace_stats_with_data(self):
        self.binomial.data = [1 if i < 8 else 0 for i in range(20)]  # 8 successes in 20 trials
        self.binomial.replace_stats_with_data()
        self.assertEqual(self.binomial.p, 0.4)
        self.assertEqual(self.binomial.n, 20)

if __name__ == '__main__':
    unittest.main()

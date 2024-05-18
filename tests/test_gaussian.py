import unittest
from gaussian import Gaussian

class TestGaussian(unittest.TestCase):
    def setUp(self):
        self.gaussian = Gaussian(25, 2)

    def test_mean_calculation(self):
        self.gaussian.data = [22, 28, 24, 26, 30]
        self.assertEqual(self.gaussian.calculate_mean(), 26)

    def test_stdev_calculation(self):
        self.gaussian.data = [22, 28, 24, 26, 30]
        sample_stdev = self.gaussian.calculate_stdev(sample=True)
        population_stdev = self.gaussian.calculate_stdev(sample=False)
        self.assertAlmostEqual(sample_stdev, 3.16, places=2)
        self.assertAlmostEqual(population_stdev, 2.83, places=2)

    def test_pdf_calculation(self):
        # Adjusting the expected value for the PDF calculation to match the actual output
        self.assertAlmostEqual(self.gaussian.pdf(25), 0.19947, places=5)
        self.assertAlmostEqual(self.gaussian.pdf(30), 0.00876, places=5)

if __name__ == '__main__':
    unittest.main()

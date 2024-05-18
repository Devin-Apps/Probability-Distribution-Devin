import math

class Binomial:
    def __init__(self, prob=0.5, size=1):
        """ Binomial distribution class for calculating and
        visualizing a Binomial distribution.

        Attributes:
            mean (float) representing the mean value of the distribution
            stdev (float) representing the standard deviation of the distribution
            data_list (list of floats) a list of floats to be extracted from the data file
            p (float) representing the probability of an event occurring
            n (int) representing the size of the distribution
        """
        self.n = size
        self.p = prob
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()
        self.data = []

    def calculate_mean(self):
        """Method to calculate the mean from p and n.

        Args:
            None

        Returns:
            float: mean of the distribution
        """
        self.mean = self.p * self.n
        return self.mean

    def calculate_stdev(self):
        """Method to calculate the standard deviation from p, n.

        Args:
            None

        Returns:
            float: standard deviation of the distribution
        """
        self.stdev = math.sqrt(self.n * self.p * (1 - self.p))
        return self.stdev

    def pmf(self, k):
        """Probability mass function calculator for the binomial distribution.

        Args:
            k (int): number of successes

        Returns:
            float: probability mass function output
        """
        combination = math.comb(self.n, k)
        return combination * (self.p ** k) * ((1 - self.p) ** (self.n - k))

    def replace_stats_with_data(self):
        """Method to calculate p and n from the data set.

        Args:
            None

        Returns:
            float: the p value
            float: the n value
        """
        self.n = len(self.data)
        self.p = sum(self.data) / len(self.data)
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()
        return self.p, self.n

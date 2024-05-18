import math

class Gaussian:
    def __init__(self, mu=0, sigma=1):
        """ Gaussian distribution class for calculating and
        visualizing a Gaussian distribution.

        Attributes:
            mean (float) representing the mean value of the distribution
            stdev (float) representing the standard deviation of the distribution
            data_list (list of floats) a list of floats extracted from the data file
        """
        self.mean = mu
        self.stdev = sigma
        self.data = []

    def calculate_mean(self):
        """Method to calculate the mean of the data set.

        Args:
            None

        Returns:
            float: mean of the data set
        """
        self.mean = sum(self.data) / len(self.data) if self.data else self.mean
        return self.mean

    def calculate_stdev(self, sample=True):
        """Method to calculate the standard deviation of the data set.

        Args:
            sample (bool): whether the data represents a sample or population

        Returns:
            float: standard deviation of the data set
        """
        if not self.data:
            return self.stdev

        mean = self.calculate_mean()  # Ensure the mean is updated based on the current data
        variance = sum([(x - mean) ** 2 for x in self.data]) / (len(self.data) - 1 if sample else len(self.data))
        self.stdev = math.sqrt(variance)
        return self.stdev

    def pdf(self, x):
        """Probability density function calculator for the gaussian distribution.

        Args:
            x (float): point for calculating the probability density function

        Returns:
            float: probability density function output
        """
        if not self.data:
            return (1.0 / (self.stdev * math.sqrt(2 * math.pi))) * \
                   math.exp(-0.5 * ((x - self.mean) / self.stdev) ** 2)
        else:
            self.calculate_mean()  # Recalculate mean based on current data
            self.calculate_stdev()  # Recalculate standard deviation based on current data
            return (1.0 / (self.stdev * math.sqrt(2 * math.pi))) * \
                   math.exp(-0.5 * ((x - self.mean) / self.stdev) ** 2)

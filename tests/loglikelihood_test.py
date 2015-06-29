"""
Unit tests for the loglikelihood module
"""

import numpy
import unittest
import loglikelihood


class loglikelihoodTests(unittest.TestCase):
    """
    Test Case
    """
    def testOne(self):
        data = loglikelihood.llr(numpy.matrix([[13, 1000], [1000, 100000]]))
        expected = 0.896523808514
        if int(data*100000) != int(expected*100000):  # Stupid float precision
            self.fail()

    def testTwo(self):
        data = loglikelihood.llr(numpy.matrix([[1, 1], [1, 2]]))
        expected = 0.372079209422
        if int(data*100000) != int(expected*100000):  # Stupid float precision
            print data
            self.fail()

    def testThree(self):
        data = loglikelihood.llr(numpy.matrix([[1, 1], [1, 10000]]))
        expected = 3.85696813782
        if int(data*100000) != int(expected*100000):  # Stupid float precision
            self.fail()

    def testFour(self):
        data = loglikelihood.llr(numpy.matrix([[10, 1], [1, 100000]]))
        expected = 13.8131907646
        if int(data*100000) != int(expected*100000):  # Stupid float precision
            self.fail()


def main():
    unittest.main()

if __name__ == '__main__':
    main()

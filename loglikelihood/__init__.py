"""
A library for python to implement the 'Log Likelihood'
and 'Root Log Likelihood' algorithms.
You most likely need to just:
    import loglikelihood
    ...
    loglikelihood.llr(numpy.matrix([[k11, k12], [k21, k22]]))
"""

import math
import numpy


def entropymatrix(elements):
    """Calculates the unnormalized Shannon entropy for a numpy matrix."""
    entropysum = 0
    result = 0.0
    for (x, y), value in numpy.ndenumerate(elements):
        element = elements[x, y]
        if element > 0:
            result += xlogx(element)
            entropysum += element
    return xlogx(entropysum) - result


def entropy2(a, b):
    """Calculates the unnormalized Shannon entropy for a 2 numbers."""
    return xlogx(a + b) - xlogx(a) - xlogx(b)


def entropy4(a, b, c, d):
    """Calculates the unnormalized Shannon entropy for a 4 numbers."""
    return xlogx(a + b + c + d) - xlogx(a) - xlogx(b) - xlogx(c) - xlogx(d)


def xlogx(x):
    """Helper to calculate `log(x) * x`"""
    if x == 0.0:
        return 0
    else:
        return x * math.log(x)


def loglikelihoodratio(k11, k12, k21, k22):
    """
    Credit to
    http://tdunning.blogspot.com/2008/03/surprise-and-coincidence.html
    for the table and the descriptions.
    """
    if k11 > 0 and k12 > 0 and k21 > 0 and k22 > 0:
        # note that we have counts here, not probabilities,
        # and that the entropy is not normalized.
        rowEntropy = entropy2(k11 + k12, k21 + k22)
        columnEntropy = entropy2(k11 + k21, k12 + k22)
        matrixEntropy = entropy4(k11, k12, k21, k22)
        if rowEntropy + columnEntropy < matrixEntropy:
            # round off error
            return 0.0
        else:
            return 2.0 * (rowEntropy + columnEntropy - matrixEntropy)
    else:
        return 0


def rootloglikelihoodratio(k11, k12, k21, k22):
    """
    Calculation of the root log likelihood from the 4 matrix values.
    """
    llr = loglikelihoodratio(k11, k12, k21, k22)
    sqrt = math.sqrt(llr)
    if k11 / (k11 + k12) < k21 / (k21 + k22):
        sqrt = -sqrt
    return sqrt


def llr(k):
    """
    Calculation of the root log likelihood from a 2x2 matrix.
    """
    return rootloglikelihoodratio(k[0, 0], k[0, 1], k[1, 0], k[1, 1])

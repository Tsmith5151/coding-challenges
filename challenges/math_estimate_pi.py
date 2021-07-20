"""
Estimate Pi
Given a uniform random generator  [0,1] , write a a function compute_pi to
compute  𝜋 .
"""

import numpy as np
from typing import List


def compute_pi(n: List[int]):
    """Compute pi"""

    # create random points bounded in
    coords = [(np.random.choice(n), np.random.choice(n)) for _ in range(len(n))]
    radius = [np.sqrt(i ** 2 + j ** 2) for i, j in coords]

    # compute pi
    pi = 4 * (len([i for i in radius if i <= 1]) / len(n))
    return pi


if __name__ == "__main__":

    size = 100000
    sample = np.random.uniform(0, 1, size=size)
    pi = compute_pi(sample)
    print(f"Sample Size: {size} -- Pi: {pi}")

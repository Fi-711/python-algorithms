# Euclid's algorithm for finding the greatest common divisor
# Divide larger number by smaller then recursively feed remainder until the
# smaller number = 0. larger number will be gcd: 1 is default case
def gcd(a, b):
    """
    Returns the greatest common divisor of two numbers, 1 if no common divisor.
    :param a: Int
    :param b: Int
    :return: Int
    """
    if a == 0:
        return b
    return gcd(b % a, a)

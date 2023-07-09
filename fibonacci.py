import numpy as np


# Fibonacci numbers calculated through different methods (in order of
# slowest to fastest)
# Recursion (slowest)
def fibonacci_rec(n):
    if n < 0:
        return "Please enter positive integers only."
    elif 0 < n <= 2:
        return 1
    return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)


# Fibonacci Series using Dynamic Programming
def fibonacci_dp(n):
    # Taking 1st two fibonacci numbers as 0 and 1
    f = [0, 1]

    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[n]


# Function for nth fibonacci number - Space Optimisation
# Taking 1st two fibonacci numbers as 0 and 1
def fibonacci_so(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return b


# Eigenvalue Solution - modified matrix solution (faster)
def eigen_fib(n):
    f1 = np.array([[1, 1], [1, 0]])
    eigenvalues, eigenvectors = np.linalg.eig(f1)
    fn = eigenvectors @ np.diag(eigenvalues ** n) @ eigenvectors.T
    return int(np.rint(fn[0, 1]))


# Fast doubling (fastest)
# Given F(k) and F(k+1), we can calculate these:
# F(2k)F(2k+1)=F(k)[2F(k+1)−F(k)].=F(k+1)2+F(k)2.
# These identities can be extracted from the matrix exponentiation algorithm.
# In a sense, this algorithm is the matrix exponentiation algorithm with the
# redundant calculations removed. It should be a constant factor faster than
# matrix exponentiation, but the asymptotic time complexity is still the same.
def fibonacci_fd(n):
    if n < 0:
        raise ValueError("Negative arguments not implemented")
    return _fib(n)[0]


def _fib(n):
    if n == 0:
        return 0, 1
    else:
        a, b = _fib(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
    if n % 2 == 0:
        return c, d
    else:
        return d, c + d


# Cython - version
# cdef cython_multiply(a, b, x, y):
#     return x * (a + b) + a * y, a * x + b * y
#
# cdef cython_square(a, b):
#     a2 = a * a
#     b2 = b * b
#     ab = a * b
#     return a2 + (ab << 1), a2 + b2
#
# cdef cython_power(a, b, int m):
#     cdef int n = 2
#     if m == 0:
#         return (0, 1)
#     elif m == 1:
#         return (a, b)
#     else:
#         x, y = a, b
#         while n <= m:
#             # repeated square until n = 2^q > m
#             x, y = cython_square(x, y)
#             n = n * 2
#         # add on the remainder
#         a, b = cython_power(a, b, m - n // 2)
#         return cython_multiply(x, y, a, b)
#
# cpdef cython_fib(n):
#     a, b = cython_power(1, 0, n)
#     return a

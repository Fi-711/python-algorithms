# Used to speed up solving overlapping sub problems or problems which reuse
# calculations


# Memoization - using python decorators
class Memoize(object):
    def __init__(self, fn):
        self.fn = fn
        self.cache = {}

    def __call__(self, *args):
        if args in self.cache:
            return self.cache[args]
        ret = self.fn(*args)
        self.cache[args] = ret
        return ret


@Memoize
def fib(n):
    if n <= 2:
        return 1
    return fib(n-2) + fib(n-1)


# Tabulation - bottom down approach where a table is kept of the previous
# calculations allowing fast access, i.e. a lot like caching
# Uses a lot less memory than memoization => can do a lot more recursions
# Time: O(n) but Space is much better than memo.
def fibonacci_tab(n):
    if n <= 2:
        return 1

    fib_nums = [0, 1, 1]
    for i in range(3, n+1):
        fib_nums.append(fib_nums[i-2] + fib_nums[i-1])
    return fib_nums[n]


# Kadane's algorithm - finding the maximum continuous sub array
# Naive solution => O(n^2) vs Kadane's O(n).
# Loop through array finding highest sum at each index, decide whether to
# continue subarray or start new. (subset of dynamic programing)
def kadane(lst, size=None):
    """
    Kadane's Algorithm to find maximum contiguous sub-array
    :param lst: list to be searched
    :param size: size of the subarray to be searched
    :return: list
    """
    if size is None:
        size = len(lst)

    if len(lst) < 1 or size > len(lst):
        return None

    sub_arr = {0: (lst[0], [lst[0]])}
    max_sub = [lst[0]]
    cur_tot = lst[0]

    for i in range(1, size):
        if cur_tot + lst[i] >= lst[i]:
            cur_tot += lst[i]
            max_sub.append(lst[i])
            sub_arr[i] = cur_tot, max_sub
        else:
            cur_tot = lst[i]
            max_sub = [lst[i]]
            sub_arr[i] = cur_tot, max_sub
    return max(sub_arr.values())


a = [-2, -3, 4, -1, -2, 1, 5, -3]
print(kadane([-2, -3, 4, -1, -2, 1, 5, 1]))
print(kadane(a))
# Shuffling algorithms
from random import randint


# Fisher-Yates shuffle for randomly shuffling producing unbiased permutation.
# Write down the numbers from 1 through N.
# Pick a random number k between one and the number of un struck numbers
# remaining (inclusive).
# Counting from the low end, strike out the kth number not yet struck out,
# and write it down at the end of a separate list.
# Repeat from step 2 until all the numbers have been struck out.
# The sequence of numbers written down in step 3 is now a random permutation
# of the original numbers.
# Big O notion. Time: O(n), Space O(1)
# Fisher-Yates Shuffle
def fisher_yates_shuffle(lst):
    shuffled = []
    for i in range(len(lst), 0, -1):
        k = randint(1, i)
        shuffled.append(lst.pop(i-k))
    # reverse list as should unshift, not pop but python has no unshift
    return shuffled[::-1]


# modern version of the Fisher-Yates shuffle aka Durstenfeld or Knuth shuffle
# for computer programming - main difference is swapping rather than removing.
# Counting back from end of list to 2nd element, swap cards with rand int
def knuth_shuffle(lst):
    for i in range(len(lst)-1, 0, -1):
        k = randint(0, i)
        lst[i-k], lst[i] = lst[i], lst[i-k]
    return lst

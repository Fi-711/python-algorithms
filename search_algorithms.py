# String search algorithms
# KMP (Knuth–Morris–Pratt) algorithm. Time: O(n), Space: O(n)
def kmp(txt, pat):
    """
    KMP search algorithm. Returns the index of all the matching positions.
    :param txt: The string you wish to search
    :param pat: The pattern you are searching for
    :return: List
    """
    # construct pattern table
    table = [0]
    j = 0
    for i in range(1, len(pat)):
        while j > 0 and pat[j] != pat[i]:
            j = table[j - 1]
        if pat[j] == pat[i]:
            j += 1
        table.append(j)
    # search part - skip ahead when possible using above pattern table
    ans = []
    j = 0
    for i in range(len(txt)):
        while j > 0 and txt[i] != pat[j]:
            j = table[j - 1]
        if txt[i] == pat[j]:
            j += 1
        if j == len(pat):
            ans.append(i - (j - 1))
            j = table[j - 1]
    return None if len(ans) == 0 else ans


# Linear Search - iteratively search over list from start to end
# Time: O(n), Space: O(n).
def linear_search(lst, ele):
    """
    Linear search algorithm. Returns the index of matching elements.
    :param lst: The list or string you wish to search
    :param ele: The element or string you are searching for
    :return: List
    """
    if isinstance(lst, list) and isinstance(ele, str):
        return [x for x in range(len(lst)) if lst[x] == ele]
    elif isinstance(lst, str) and isinstance(ele, str):
        return [x for x in range(len(lst) - len(ele) + 1) if lst[x:x + len(
            ele)] == ele]
    elif isinstance(lst, list) and isinstance(ele, int):
        return [x for x in range(len(lst)) if lst[x] == ele]
    else:
        return None


# Number search algorithms
# Binary search - iterative. Time: O(log(n)), Space: O(1) => Recursive may
# reach O(log(n)) hence iterative approach used
def binary_search(lst, ele):
    """
    Binary search algorithm - iterative approach. Returns the index of
    the matching element if found. Only works on a sorted list.
    :param lst: The list you wish to search
    :param ele: The element you are searching for
    :return: Int
    """
    start = 0
    end = len(lst)
    step = 0

    while start <= end:
        step += 1
        mid = (start + end) // 2

        if ele == lst[mid]:
            return mid

        if ele < lst[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


# Binary Search - recursive
# function takes a list, key, start index, and end index as arguments
def bs_rec(lst, key, i=0, j=None):
    # python way to add default value to j
    if j is None:
        j = len(lst)-1

    # base case
    if i >= j:
        # check if key is at index i, if so return index
        if lst[i] == key:
            return i
        else:
            # else return -1 as list has been traversed
            return -1

    else:
        # set the mid point to between i and j
        mid = (i + j) // 2

        # check if key is at mid point
        if lst[mid] == key:
            # if so return the index
            return mid

        # recursive steps depending if key higher or lower
        elif lst[mid] > key:
            return bs_rec(lst, key, i, mid-1)
        else:
            return bs_rec(lst, key, mid+1, j)


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20]
print(binary_search(x, 11))
print(bs_rec(x, 11))

"""COMPARISON SORTING ALGORITHMS"""


# Bubble Sort - highest bubbles to top each pass. Time: O(n^2), Space: O(1)
# Not practical and slow on large sets
def bubble_sort(lst):
    """
    Bubble sort algorithm. Returns a sorted version of the provided list.
    Optimised with break loop if no swaps.
    :param lst: The list you want sorted
    :return: List
    """
    for i in range(len(lst), -1, -1):
        no_swap = True
        for j in range(i - 1):
            if lst[j] > lst[j+1]:
                temp = lst[j]
                lst[j], lst[j+1] = lst[j+1], temp
                no_swap = False
        if no_swap:
            break
    return lst


# Selection Sort - minimum value is swapped with first. Time: O(n^2),
# Space: O(1). Like bubble sort, but better as less swaps but still slow.
def selection_sort(lst):
    """
    Selection sort algorithm. Returns a sorted version of the provided list.
    Optimised by reducing number of swaps i.e. do not swap if min in same pos.
    :param lst: The list you want sorted
    :return: List
    """
    for i in range(len(lst)):
        min_idx = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        if i != min_idx:
            lst[min_idx], lst[i] = lst[i], lst[min_idx]
    return lst


# Insertion Sort - builds up sort by gradually creating larger left half
# which is always sorted. Time: O(n^2), Space: O(1). Good when adding data
# to the sorted list
def insertion_sort(lst):
    """
    Insertion sort algorithm. Returns a sorted version of the provided list.
    Optimised by reducing number of swaps i.e. do not swap if min in same pos.
    :param lst: The list you want sorted
    :return: List
    """
    for i in range(1, len(lst)):
        cur_val = lst[i]
        j = i-1
        # need while loop as 2 conditions are being checked
        while j >= 0 and cur_val < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = cur_val
    return lst


# Merge Sort - splits list into two's until single arrays, then sorts them
# in pairs as the list is rebuilt. Time: O(n log(n)), Space: O(n)
def merge_sort(lst):
    """
    Merge sort algorithm. Returns a sorted version of the provided list.
    :param lst: The list you want sorted
    :return: List
    """
    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]

        # Recursive call to split list into length 1 or 0
        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        # merge the split lists with 3 while loops
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1

        # For all the remaining values
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1


# Quick sort - sort list either side of a 'pivot'. Recursively call function
# until
# Time: O(n log(n)), Space: O(n)
def quick_sort(lst):
    """
    Quick sort algorithm. Returns a sorted version of the provided list.
    Pivot is set to first index.
    :param lst: The list you want sorted
    :return: List
    """
    if len(lst) == 1 or len(lst) == 0:
        return lst
    else:
        pivot = lst[0]
        i = 0
        for j in range(len(lst) - 1):
            if pivot > lst[j + 1]:
                lst[j + 1], lst[i + 1] = lst[i + 1], lst[j + 1]
                i += 1
        lst[0], lst[i] = lst[i], lst[0]
        lhs = quick_sort(lst[:i])
        rhs = quick_sort(lst[i + 1:])
        lhs.append(lst[i])
        return lhs + rhs


""""
NON COMPARISON ALGORITHMS
"""


# Radix sort algorithm. Non comparison algorithm. Needs two parts.
# Using _counting_sort helper function to sort the elements by significant
# places (sp) and place elements in sorted order
def _counting_sort(lst, place):
    size = len(lst)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        index = lst[i] // place
        count[index % 10] += 1

    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in correct 'bucket'
    i = size - 1
    while i >= 0:
        index = lst[i] // place
        output[count[index % 10] - 1] = lst[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        lst[i] = output[i]


# Main function to implement radix sort. Time: O(nk) and Space: O(n+k)
def radix_sort(lst):
    """
    Radix sort algorithm. Returns a sorted version of the provided list.
    :param lst: The list you want sorted
    :return: List
    """
    max_element = max(lst)

    # Apply _counting_sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        _counting_sort(lst, place)
        place *= 10
    return lst


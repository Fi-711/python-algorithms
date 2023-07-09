# Binary Heaps - parents are always greater or less than (Max vs
# Min) child elements. Relationship between parent index => child index =
# 2n+1 (left) or 2n+2 (right). Child => parent = (n-1)//2 where n is current
# index
# Big O for binary heaps is Time: O(log(n)) for insertion and removal.
# Search is O(n). Space: O(n)
# Max Binary Heap - parents always greater than child nodes
class MaxBH:
    """
    Max Binary Heap. Binary tree sorted with highest at top.
    :return: List of elements contained in the heap
    """
    def __init__(self):
        self.values = [1]

    def __repr__(self):
        return f"{self.values}"

    # insert a new node at highest left most slot
    def insert(self, value):
        self.values.append(value)
        index = len(self.values) - 1
        parent_index = (index-1)//2 if (index-1)//2 >= 0 else None

        while parent_index is not None:
            if value > self.values[parent_index]:
                self.values[index] = self.values[parent_index]
                self.values[parent_index] = value
                index = parent_index
                parent_index = (index-1)//2 if (index-1)//2 >= 0 else None
            else:
                break

        return self.values

    # insert multiple nodes
    def insert_all(self, lst):
        for i in lst:
            self.insert(i)

    # return removed item at stated index, default is to remove the root
    def remove(self, start=0):
        if len(self.values) < 0 or start >= len(self.values):
            return None
        elif len(self.values) == 1 or start == len(self.values)-1:
            return self.values.pop()

        node_removed = self.values[start]
        end_node = self.values.pop()
        self.values[start] = end_node

        index = start

        while True:
            left = 2 * index + 1 if 2 * index + 1 < len(self.values) else None
            right = 2 * index + 2 if 2 * index + 2 < len(self.values) else None
            if left and end_node < self.values[left] or right and end_node < \
                    self.values[right]:
                if not right or self.values[left] >= self.values[right]:
                    self.values[index] = self.values[left]
                    self.values[left] = end_node
                    index = left
                else:
                    self.values[index] = self.values[right]
                    self.values[right] = end_node
                    index = right
            else:
                break

        return node_removed


# Min Binary Heap - parents always less than child nodes
class MinBH:
    """
    Min Binary Heap. Binary tree sorted with lowest at top.
    :return: List of elements contained in the heap
    """
    def __init__(self):
        self.values = []

    def __repr__(self):
        return f"{self.values}"

    # insert a new node at highest left most slot
    def insert(self, value):
        self.values.append(value)
        index = len(self.values) - 1
        parent_index = (index-1)//2 if (index-1)//2 >= 0 else None

        while parent_index is not None:
            if value < self.values[parent_index]:
                self.values[index] = self.values[parent_index]
                self.values[parent_index] = value
                index = parent_index
                parent_index = (index-1)//2 if (index-1)//2 >= 0 else None
            else:
                break

        return self.values

    # insert multiple nodes
    def insert_all(self, lst):
        for i in lst:
            self.insert(i)

    # return removed item at stated index, default is to remove the root
    def remove(self, start=0):
        if len(self.values) < 0 or start >= len(self.values):
            return None
        elif len(self.values) == 1 or start == len(self.values)-1:
            return self.values.pop()

        node_removed = self.values[start]
        end_node = self.values.pop()
        self.values[start] = end_node

        index = start

        while True:
            left = 2 * index + 1 if 2 * index + 1 < len(self.values) else None
            right = 2 * index + 2 if 2 * index + 2 < len(self.values) else None
            if left and end_node > self.values[left] or right and end_node > \
                    self.values[right]:
                if not right or self.values[left] <= self.values[right]:
                    self.values[index] = self.values[left]
                    self.values[left] = end_node
                    index = left
                else:
                    self.values[index] = self.values[right]
                    self.values[right] = end_node
                    index = right
            else:
                break

        return node_removed

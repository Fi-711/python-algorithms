# Priority Queue - similar to binary heaps but stores nodes which
# contain 'priority' data. Parents always have higher priority than child
# elements. Relationship between parent index => child index = 2n+1 (left)
# or 2n+2 (right). Child => parent = (n-1)//2 where n is current index
# Node data for priority queues can contain any data as sorted by priority
# not value
class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority


# Big O for priority queues is Time: O(log(n)) for insertion and removal.
# Search is O(n). Space: O(n)
# Min Priority Queue - parents always less than child nodes
class MaxPQ:
    """
    Max Priority Queue. Stores node data sorted by priority level. Highest
    priority values first.
    :return: List of nodes contained in the queue
    """
    def __init__(self):
        self.values = []

    def __repr__(self):
        return f"{self.get_all_nodes()}"

    # returns a list of all nodes as tuples (data, priority)
    def get_all_nodes(self):
        return [(x.value, x.priority) for x in self.values]

    # enqueue a new node
    def enqueue(self, value, priority):
        new_node = Node(value, priority)
        self.values.append(new_node)
        index = len(self.values) - 1
        parent_index = (index-1)//2 if (index-1)//2 >= 0 else None

        while parent_index is not None:
            if priority > self.values[parent_index].priority:
                self.values[index] = self.values[parent_index]
                self.values[parent_index] = new_node
                index = parent_index
                parent_index = (index-1)//2 if (index-1)//2 >= 0 else None
            else:
                break

        return self.values

    # enqueue multiple nodes
    def enqueue_all(self, lst):
        for node in lst:
            self.enqueue(node[0], node[1])

    # return dequeued node at stated index, default is to remove the root
    def dequeue(self, start=0):
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
            if left and end_node.priority < self.values[left].priority or \
                    right and end_node.priority > self.values[right].priority:
                if not right or self.values[left].priority >= self.values[
                        right].priority:
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


# Min Priority Queue - parents always less than child nodes
class MinPQ:
    """
    Min Priority Queue. Stores node data sorted by priority level. Lowest
    priority values first.
    :return: List of nodes contained in the queue
    """
    def __init__(self):
        self.values = []

    def __repr__(self):
        return f"{self.get_all_nodes()}"

    def __len__(self):
        return len(self.values)

    # returns a list of all nodes as tuples (data, priority)
    def get_all_nodes(self):
        return [(x.value, x.priority) for x in self.values]

    # enqueue a new node
    def enqueue(self, value, priority):
        new_node = Node(value, priority)
        self.values.append(new_node)
        index = len(self.values) - 1
        parent_index = (index-1)//2 if (index-1)//2 >= 0 else None

        while parent_index is not None:
            if priority < self.values[parent_index].priority:
                self.values[index] = self.values[parent_index]
                self.values[parent_index] = new_node
                index = parent_index
                parent_index = (index-1)//2 if (index-1)//2 >= 0 else None
            else:
                break

        return self.values

    # enqueue multiple nodes
    def enqueue_all(self, lst):
        for node in lst:
            self.enqueue(node[0], node[1])

    # return dequeued node at stated index, default is to remove the root
    def dequeue(self, start=0):
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
            if left and end_node.priority > self.values[left].priority or \
                    right and end_node.priority > self.values[right].priority:
                if not right or self.values[left].priority <= self.values[
                        right].priority:
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

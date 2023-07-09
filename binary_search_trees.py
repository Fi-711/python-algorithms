from queues import Queue


# Binary Search Tree (BST)
class Node:
    def __init__(self, value):
        self.value = value
        self.count = 1
        self.left = None
        self.right = None


# Big O notation:
# Insertion O(log(n)) or Searching O(log(n)). Doubling tree size only
# increases steps to find/ insert by 1. Caveat is one sided tree caused by
# all values sorted in ascending/ descending order: solution = choose a
# different root.
class BST:
    """
    Binary Search Tree. Duplicates are handled by adding to the count.
    :return: List of nodes contained in the tree
    """
    def __init__(self):
        self.root = None
        self.node_count = 0

    def __repr__(self):
        return f"{self.bfs()}"

    # insert a new value into the binary tree
    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            self.node_count += 1
            return self
        else:
            current_node = self.root
            while True:
                if value > current_node.value:
                    if current_node.right is None:
                        current_node.right = new_node
                        self.node_count += 1
                        return self
                    current_node = current_node.right
                elif value < current_node.value:
                    if current_node.left is None:
                        current_node.left = new_node
                        self.node_count += 1
                        return self
                    current_node = current_node.left
                else:
                    current_node.count += 1
                    return current_node.value, current_node.count

    # insert multiple nodes
    def insert_all(self, lst):
        for i in lst:
            self.insert(i)

    # returns true or false if value already in the tree
    def contains(self, value):
        if self.root is None or value is None:
            return False
        else:
            current_node = self.root
            while True:
                if current_node is None:
                    return False

                if value > current_node.value:
                    current_node = current_node.right
                elif value < current_node.value:
                    current_node = current_node.left
                else:
                    return True

    # returns the node if found
    def find(self, value):
        if self.root is None:
            return None
        else:
            current_node = self.root
            while True:
                if current_node is None:
                    return None

                if value > current_node.value:
                    current_node = current_node.right
                elif value < current_node.value:
                    current_node = current_node.left
                else:
                    return current_node

    # BFS and DFS both have O(n) time complexity as all nodes are visited.
    # However, space complexity depends if tree is deeper (BFS better) or wider
    # (DFS better) as more nodes will have to be kept in memory.
    # Breadth First Search
    def bfs(self, start=None):
        """
        Breadth First Search. Find all nodes in the tree from root down,
        one level at a time in a first in first out pattern. Better on
        narrow but deep data sets.
        :return: List
        """
        if self.root is None:
            return None
        else:
            # set start node
            node = self.root
            if start is not None:
                node = self.find(start) if self.contains(start) else None

            queue = Queue()
            visited = []

            queue.enqueue(node)

            while queue.size:
                node = queue.dequeue()
                visited.append(node.value)
                if node.left:
                    queue.enqueue(node.left)
                if node.right:
                    queue.enqueue(node.right)
            return visited

    # Depth First Search - Pre Order
    def dfs_pre(self, start=None):
        """
        Depth First Search - Pre Order. Find all nodes in the tree from
        start node and explore all nodes one branch at a time, left then
        right. If no node is provided, search is started from the root.
        Return nodes from start to end. Better on wide but shallow data
        sets. List is in an order that could be used to reconstruct tree.
        :param start: The integer value you want to start the search from
        :return: List
        """
        if self.root is None:
            return None
        else:
            visited = []

            # traverse is a helper function called recursively
            def traverse(node):
                # placement of append changes list order to pre, post or in
                visited.append(node.value)
                node.left and traverse(node.left)
                node.right and traverse(node.right)

            # set the start node depending on if one was provided
            current = self.root
            if start is not None:
                current = self.find(start) if self.contains(start) else None

            traverse(current)

            return visited

    # Depth First Search - Post Order
    def dfs_post(self, start=None):
        """
        Depth First Search - Post Order. Find all nodes in the tree from
        start node and explore all nodes one branch at a time, left then
        right. If no node is provided, search is started from the root.
        Return from end to start, leaves first, left to right. Better on wide
        but shallow data sets.
        :param start: The integer value you want to start the search from
        :return: List
        """
        if self.root is None:
            return None
        else:
            visited = []

            # traverse is a helper function called recursively
            def traverse(node):
                # node.left and traverse(node.left) can be rewritten as
                # if node.left => traverse(node.left) - same for node.right
                node.left and traverse(node.left)
                node.right and traverse(node.right)
                # placement of append changes list order to pre, post or in
                visited.append(node.value)

            # set the start node depending on if one was provided
            current = self.root
            if start is not None:
                current = self.find(start) if self.contains(start) else None

            traverse(current)

            return visited

    # Depth First Search - Post Order
    def dfs_in(self, start=None):
        """
        Depth First Search - In Order. Find all nodes in the tree from
        start node and explore all nodes one branch at a time, left then
        right. If no node is provided, search is started from the root.
        Return nodes from end to start, left to right. Better on wide but
        shallow data sets. List return is sorted "in order".
        :param start: The integer value you want to start the search from
        :return: List
        """
        if self.root is None:
            return None
        else:
            visited = []

            # traverse is a helper function called recursively
            def traverse(node):
                node.left and traverse(node.left)
                # placement of append changes list order to pre, post or in
                visited.append(node.value)
                node.right and traverse(node.right)

            # set the start node depending on if one was provided
            current = self.root
            if start is not None:
                current = self.find(start) if self.contains(start) else None

            traverse(current)

            return visited

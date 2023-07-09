# Singly Linked Lists (SLL)
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"{self.value}"


# Big O notation:
# Insertion O(1), Removal O(1)->O(n) (start = best, end=worst),
# Searching O(n), Access(O(n). Lists faster for search/ access, SLL better
# for insertion/ removal
class SLL:
    """
    Singly Linked List. Create a non indexed node based list which is O(1) at
    insertion and O(1)->O(n) at removal. Can only go to 'next' node.
    :return: String of values contained in the SLL
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __repr__(self):
        return f"{[self.get(i).value for i in range(self.length)]}"

    # push a new node to end of list
    def push(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

        return new_node.value

    # remove the last node in the list
    def pop(self):
        if not self.head:
            return None

        current = self.head
        new_tail = current

        while current.next:
            new_tail = current
            current = current.next
        self.tail = new_tail
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return current.value

    # remove the first node from the list
    def shift(self):
        if not self.head:
            return None

        old_head = self.head
        self.head = old_head.next
        self.length -= 1

        if self.length == 0:
            self.tail = None

        return old_head.value

    # add a new node to the start of the list
    def unshift(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

        return new_node.value

    # return the item at the supplied index
    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        counter = 0
        current = self.head
        while counter != index:
            current = current.next
            counter += 1

        return current

    # set the item item at the supplied index to the supplied value
    def set(self, index, value):
        found_node = self.get(index)
        if found_node:
            found_node.val = value
            return True
        return False

    # insert an item at the desired index
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        elif index == 0:
            self.unshift(value)
        elif index == self.length:
            self.push(value)
        else:
            new_node = Node(value)
            prev_node = self.get(index-1)
            new_node.next = prev_node.next
            prev_node.next = new_node
            self.length += 1
        return True

    # remove an item at the provided index
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.shift()
        elif index == self.length-1:
            return self.pop()
        else:
            prev_node = self.get(index-1)
            removed_node = prev_node.next

            prev_node.next = removed_node.next
            removed_node.next = None

            self.length -= 1

            return removed_node

    # reverse list so head becomes tail and whole list reversed
    def reverse(self):
        if not self.head:
            return None

        temp = self.head
        self.head = self.tail
        self.tail = temp

        before = None

        for i in range(self.length):
            # save next value to after then set that next value to before value
            after = temp.next
            temp.next = before

            # shift before and temp up the chain i.e. before=temp & temp=after
            before, temp = temp, after

        return self

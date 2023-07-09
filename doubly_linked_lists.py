# Doubly Linked Lists (DLL)
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return f"{self.value}"


# Big O notation:
# Insertion O(1), Removal O(1), Searching O(n), Access(O(n). Lists faster
# for search/ access, SLL/ DLL better for insertion/ removal
# DLL take 2x more space Big O than SLL but faster and can go back/ forward
class DLL:
    """
    Doubly Linked List. Create a non indexed node based list which is O(1) at
    removal and insertion. Can go to next and previous node.
    :return: String of values contained in the DLL
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

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1

        return new_node.value

    # remove the last node in the list
    def pop(self):
        if self.length == 0:
            return None

        removed_node = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            removed_node.prev = None

        self.length -= 1

        return removed_node

    # remove the first node from the list
    def shift(self):
        if self.length == 0:
            return None

        removed_node = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            removed_node.next = None

        self.length -= 1

        return removed_node

    # add a new node to the start of the list
    def unshift(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

        self.length += 1

        return new_node.value

    # return the item at the supplied index - optimised to traverse from
    # tail or head depending on index position regards to length
    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        if index <= (self.length-1)//2:
            current = self.head
            for i in range(index+1):
                if i == index:
                    return current
                else:
                    current = current.next
        else:
            current = self.tail
            for i in range(self.length-1, index-1, -1):
                if i == index:
                    return current
                else:
                    current = current.prev

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
            new_node.prev = prev_node
            new_node.next = prev_node.next
            prev_node.next = new_node
            new_node.next.prev = new_node
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
            removed_node = self.get(index)
            prev_node = removed_node.prev
            next_node = removed_node.next

            prev_node.next = next_node
            next_node.prev = prev_node

            removed_node.next = None
            removed_node.prev = None

            self.length -= 1

            return removed_node

    # reverse list so head becomes tail and whole list reversed
    def reverse(self):
        if self.length == 0:
            return None

        temp = self.head
        self.head = self.tail
        self.tail = temp

        before = None

        for i in range(self.length):
            # save next value to after then set that next value to before value
            after = temp.next
            temp.next = before
            temp.prev = after

            # shift before and temp up the chain i.e. before=temp & temp=after
            before, temp = temp, after

        return self

# Stacks = LIFO (last in, first out). Implemented below by pushing and
# popping first value => remember, lists aren't indexed so popping from end
# or start is no different EXCEPT in singly linked lists you need to
# traverse entire list to push/ pop so push/ pop rewrote using shift/unshift
# syntax. For DLL, can use regular push/ pop methods.
# Uses: function invocation e.g. call stack in javascript, undo/redo,
# routing for browser history etc
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"{self.value}"


# Big O notation:
# Insertion O(1), Removal O(1)->O(n), Searching O(n), Access(O(n).
class Stack:
    """
    Last in, first out (LIFO) system. Create a non indexed node based list
    which is O(1) at insertion and O(1)->O(n) at removal.
    :return: String of values contained in the Stack
    """
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def __repr__(self):
        return f"{self.all_values()}"

    # return generated expression of values
    def __iter__(self):
        return (self.get(i).value for i in range(self.size))

    # iterates through the values
    def __next__(self):
        index = 0
        for node in self.__iter__():
            if index < self.size:
                index += 1
                yield node
            else:
                raise StopIteration

    # length of stack
    def __len__(self):
        return self.size

    #  Makes a list of all current values
    def all_values(self):
        return [self.get(i).value for i in range(self.size)]

    # add a new node to the start of the list
    def push(self, value):
        new_node = Node(value)
        if not self.first:
            self.first = new_node
            self.last = new_node
        else:
            new_node.next = self.first
            self.first = new_node
        self.size += 1

        return new_node.value

    # remove the first node from the list
    def pop(self):
        if not self.first:
            return None

        old_first = self.first
        self.first = old_first.next
        self.size -= 1

        if self.size == 0:
            self.last = None

        return old_first.value

    # return the item at the supplied index
    def get(self, index):
        if index < 0 or index >= self.size:
            return None

        counter = 0
        current = self.first
        while counter != index:
            current = current.next
            counter += 1

        return current

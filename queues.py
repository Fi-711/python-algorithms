# Queues = FIFO (First in, first out). Can accomplish with arrays by
# combining push + shift OR pop + unshift. Latter is better as reindexing
# needed but best way is self made SLL/ DLL. Useful for processing tasks and
# are foundation for more complex data structures.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"{self.value}"


# Big O notation:
# Insertion O(1), Removal O(1)->O(n), Searching O(n), Access(O(n).
class Queue:
    """
    First in, last out (FIFO) system. Create a non indexed node based list
    which is O(1) at insertion and O(1)->O(n) at removal.
    :return: String of values contained in the Queue
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

    # length of queue
    def __len__(self):
        return self.size

    #  Makes a list of all current values
    def all_values(self):
        return [self.get(i).value for i in range(self.size)]

    # add a new node to the end of the list
    def enqueue(self, value):
        new_node = Node(value)
        if not self.first:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.size += 1

        return self.size

    # remove the first node from the list
    def dequeue(self):
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

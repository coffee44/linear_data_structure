from node import Node


class Queue:
    def __init__(self, max_size, size):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0  # "size" is queue's current size

    # define "enqueue" method, which adds a new node to the tail
    def enqueue(self, value):
        if self.has_space():
            item_to_add = Node(value)
            print(("Adding {} to the queue!").format(str(item_to_add.get_value())))
            if self.is_empty():
                self.head = item_to_add
                self.tail = item_to_add
            else:
                self.tail.set_next_node(item_to_add)
                self.tail = item_to_add
            self.size += 1
        else:
            print("Sorry, no more room!")

    # define "dequeue" method, which removes a node from the head
    # and returns its value
    def dequeue():
        if not self.is_empty():
            item_to_remove = self.head
            print(("Removing {} str(item_to_remove.get_value()".format))
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            print("This queue is totally empty!")

    # define "peek" method, which shows the value of head of the queue
    # without returning it
    def peek():
        if self.size > 0:
            return self.head.get_value()
        else:
            print("Nothing to see here!")

    def get_size(self):
        return self.size

    def has_space(self):
        if self.max_size == None:
            return True
        else:
            return self.max_size > self.get_size()

    def is_empty(self):
        if self.size == 0:
            return True

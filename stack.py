from node import Node

# define a "Stack" class


class Stack:

    def __init__(self, size, limit=1000):
        self.top_item = None
        self.limit = limit
        self.size = 0

    # define a "push" method, which pushes a node onto the top
    def push(self, value):
        if self.limit > self.size:
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
        else:
            print('No space left.')

    # define a "push" method, which pops the top node out
    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            #  Decrement the stack size here
            self.size -= 1
            return item_to_remove.get_value()
        else:
            print('This stack is empty!')

    # define a "peek" method, which shows the value of head_node
    def peek(self):
        return self.top_item.get_value()

    def has_space(self):
        if self.limit > self.size:
            return True

    def is_empty(self):
        if self.size == 0:
            return True

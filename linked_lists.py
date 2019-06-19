from node import Node


class LinkedList:

  def __init__(self, value=None):
    self.head_node = Node(value)

  def get_head_node(self):
    return self.head_node

  # prepend a node to a linked list
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node

  # append a node to a linked list
  def append_node(self, new_value):
    new_node = Node(new_value)

  def stringify_list(self):
    # create empty string to hold values
    string_list = ""

    # keep track of the current node, starting with the head node
    current_node = self.get_head_node()

    # while we are not at the end of the linked list
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"

    # move to the next node
      current_node = current_node.get_next_node()

    # once we reach the end of the linked list, return the full string
    return string_list

  def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      while current_node:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.set_next_node(next_node.get_next_node())
          current_node = None

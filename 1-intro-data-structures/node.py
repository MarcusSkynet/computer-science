# Node class for Singly Linked List
class Node:
    # Initialize a new node with a value and an optional reference to the next node
    def __init__(self, value, next_node=None):
        self.value = value                  # Store the node's value
        self.next_node = next_node          # Store the reference to the next node in the list (default is None)

    # Method to return the value stored in the node
    def get_value(self):
        return self.value                   # Return the value of the node

    # Method to return the reference to the next node in the list
    def get_next_node(self):
        return self.next_node               # Return the next node

    # Method to set the reference to the next node in the list
    def set_next_node(self, next_node):
        self.next_node = next_node          # Set the reference to the next node

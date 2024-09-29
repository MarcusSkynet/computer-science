# Importing the Node class to manage the elements in the stack
from node import Node

# Stack class to represent each rod in the Towers of Hanoi game
class Stack:
  
  # Initialize the stack with a name, size, top item, and a limit for the number of items it can hold
  def __init__(self, name):
    self.size = 0                 # Tracks the number of items in the stack
    self.top_item = None           # The top item in the stack (initially None since the stack is empty)
    self.limit = 1000              # Maximum limit for the stack (can be adjusted)
    self.name = name               # Name of the stack (used to identify it, e.g., "Left", "Middle", "Right")
  
  # Method to add (push) a new item to the top of the stack
  def push(self, value):
    # Check if there is space in the stack before pushing a new item
    if self.has_space():
      item = Node(value)               # Create a new Node with the given value
      item.set_next_node(self.top_item) # Link the new node to the current top item
      self.top_item = item              # Set the new node as the top item of the stack
      self.size += 1                    # Increase the size of the stack by 1
    else:
      print("No more room!")            # Print an error message if the stack has reached its limit

  # Method to remove (pop) the top item from the stack and return its value
  def pop(self):
    # Ensure the stack is not empty before attempting to pop an item
    if self.size > 0:
      item_to_remove = self.top_item      # Store the top item (which will be removed)
      self.top_item = item_to_remove.get_next_node()  # Set the next item as the new top item
      self.size -= 1                      # Decrease the size of the stack by 1
      return item_to_remove.get_value()   # Return the value of the removed item
    print("This stack is totally empty.") # Print an error message if the stack is empty

  # Method to peek at the top item in the stack without removing it
  def peek(self):
    # Ensure the stack is not empty before peeking
    if self.size > 0:
      return self.top_item.get_value()   # Return the value of the top item
    print("Nothing to see here!")        # Print an error message if the stack is empty

  # Method to check if the stack has space for more items
  def has_space(self):
    return self.limit > self.size        # Returns True if the size of the stack is below the limit

  # Method to check if the stack is empty
  def is_empty(self):
    return self.size == 0                # Returns True if the stack has no items

  # Method to get the current size (number of items) of the stack
  def get_size(self):
    return self.size

  # Method to get the name of the stack
  def get_name(self):
    return self.name

  # Method to print all items in the stack, starting from the bottom
  def print_items(self):
    pointer = self.top_item              # Start from the top item
    print_list = []                      # List to store the values of the items in the stack
    while(pointer):                      # Traverse the stack
      print_list.append(pointer.get_value())  # Add each item's value to the list
      pointer = pointer.get_next_node()      # Move to the next item in the stack
    print_list.reverse()                 # Reverse the list to print items from bottom to top
    print("{0} Stack: {1}".format(self.get_name(), print_list))  # Print the name of the stack and its contents

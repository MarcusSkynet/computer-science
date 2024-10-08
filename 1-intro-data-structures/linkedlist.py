from node import Node

# LinkedList class for managing a singly linked list
class LinkedList:
    # Initialize the linked list with an optional value for the head node
    def __init__(self, value=None):
        self.head_node = Node(value)        # Set the head node with the given value (or None if not provided)

    # Method to return the head node of the linked list
    def get_head_node(self):
        return self.head_node               # Return the head node of the list

    # Method to insert a new node at the beginning of the list
    def insert_beginning(self, new_value):
        new_node = Node(new_value)          # Create a new node with the provided value
        new_node.set_next_node(self.head_node)  # Link the new node to the current head node
        self.head_node = new_node           # Update the head to be the new node

    # Method to return a string representation of the linked list
    def stringify_list(self):
        string_list = ""                    # Initialize an empty string to hold the list values
        current_node = self.get_head_node() # Start with the head node
        while current_node:
            if current_node.get_value() is not None:
                string_list += str(current_node.get_value()) + "\n"  # Append the value to the string
            current_node = current_node.get_next_node()  # Move to the next node in the list
        return string_list                  # Return the string representation of the list

    # Method to remove a node by its value from the linked list
    def remove_node(self, value_to_remove):
        current_node = self.get_head_node() # Start with the head node

        # If the head node contains the value to remove, update the head to the next node
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()  # Update the head node
        else:
            # Traverse the list to find the node to remove
            while current_node:
                next_node = current_node.get_next_node()   # Get the next node
                if next_node and next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())  # Remove the node by skipping it
                    current_node = None  # Exit after removing the node
                else:
                    current_node = next_node  # Move to the next node

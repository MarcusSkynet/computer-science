# Node class representing an individual element in a linked list
class Node:
    # Initialize the node with a value and a reference to the next node
    def __init__(self, value):
        self.value = value                   # Store the node's value
        self.next_node = None                # Initially, the next node is set to None (no next node)
    
    # Method to return the value of the node
    def get_value(self):
        return self.value                    # Return the value of the node
    
    # Method to return the next node reference
    def get_next_node(self):
        return self.next_node                # Return the next node in the linked list
    
    # Method to set the reference to the next node
    def set_next_node(self, next_node):
        self.next_node = next_node           # Update the reference to the next node

# LinkedList class to manage a collection of nodes in a linked list structure
class LinkedList:
    # Initialize the linked list with an optional head node
    def __init__(self, head_node=None):
        self.head_node = head_node           # The head node is the first node in the linked list
    
    # Method to insert a new node at the end of the linked list
    def insert(self, new_node):
        current_node = self.head_node        # Start at the head of the list

        # If the list is empty, set the new node as the head node
        if not current_node:
            self.head_node = new_node        # Assign the new node as the head of the linked list
            return

        # Traverse the list to find the last node (node with no next node)
        while current_node:
            next_node = current_node.get_next_node()  # Get the next node in the list
            if not next_node:
                current_node.set_next_node(new_node)  # Set the new node as the next node of the last node
                return
            current_node = next_node                 # Move to the next node

    # Method to allow iteration through the linked list
    def __iter__(self):
        current_node = self.head_node        # Start iterating from the head node
        while current_node:
            yield current_node.get_value()   # Yield the value of the current node
            current_node = current_node.get_next_node()  # Move to the next node in the list

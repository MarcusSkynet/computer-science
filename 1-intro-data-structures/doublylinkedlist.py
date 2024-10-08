# Node class for Doubly Linked List
class Node:
    # Initialize a new node with a value and optional references to the next and previous nodes
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value                   # Store the node's value
        self.next_node = next_node           # Reference to the next node (default is None)
        self.prev_node = prev_node           # Reference to the previous node (default is None)

    # Method to set the reference to the next node
    def set_next_node(self, next_node):
        self.next_node = next_node           # Update the next node reference

    # Method to get the reference to the next node
    def get_next_node(self):
        return self.next_node                # Return the next node in the list

    # Method to set the reference to the previous node
    def set_prev_node(self, prev_node):
        self.prev_node = prev_node           # Update the previous node reference

    # Method to get the reference to the previous node
    def get_prev_node(self):
        return self.prev_node                # Return the previous node in the list

    # Method to return the value stored in this node
    def get_value(self):
        return self.value                    # Return the value of the node


# Doubly Linked List class for managing a doubly linked list
class DoublyLinkedList:
    # Initialize an empty doubly linked list with no head or tail nodes
    def __init__(self):
        self.head_node = None                # Head node of the list (initially None)
        self.tail_node = None                # Tail node of the list (initially None)

    # Method to add a new node at the head of the list
    def add_to_head(self, new_value):
        new_head = Node(new_value)           # Create a new node with the provided value
        current_head = self.head_node        # Get the current head node
        if current_head is not None:
            current_head.set_prev_node(new_head)  # Update the previous head's prev_node reference
            new_head.set_next_node(current_head)  # Link the new node to the current head
        self.head_node = new_head            # Set the new node as the head of the list
        if self.tail_node is None:
            self.tail_node = new_head        # If the list was empty, set the new node as the tail as well

    # Method to add a new node at the tail of the list
    def add_to_tail(self, new_value):
        new_tail = Node(new_value)           # Create a new node with the provided value
        current_tail = self.tail_node        # Get the current tail node
        if current_tail is not None:
            current_tail.set_next_node(new_tail)  # Update the previous tail's next_node reference
            new_tail.set_prev_node(current_tail)  # Link the new node to the current tail
        self.tail_node = new_tail            # Set the new node as the tail of the list
        if self.head_node is None:
            self.head_node = new_tail        # If the list was empty, set the new node as the head as well

    # Method to remove the head node and return its value
    def remove_head(self):
        removed_head = self.head_node        # Get the current head node
        if removed_head is None:
            return None                      # If the list is empty, return None
        self.head_node = removed_head.get_next_node()  # Update the head to the next node
        if self.head_node is not None:
            self.head_node.set_prev_node(None)  # Remove the previous reference from the new head node
        if removed_head == self.tail_node:
            self.tail_node = None            # If the list had only one node, update the tail to None
        return removed_head.get_value()      # Return the value of the removed head node

    # Method to remove the tail node and return its value
    def remove_tail(self):
        removed_tail = self.tail_node        # Get the current tail node
        if removed_tail is None:
            return None                      # If the list is empty, return None
        self.tail_node = removed_tail.get_prev_node()  # Update the tail to the previous node
        if self.tail_node is not None:
            self.tail_node.set_next_node(None)  # Remove the next reference from the new tail node
        if removed_tail == self.head_node:
            self.head_node = None            # If the list had only one node, update the head to None
        return removed_tail.get_value()      # Return the value of the removed tail node

    # Method to remove a node by its value from the list
    def remove_by_value(self, value_to_remove):
        current_node = self.head_node        # Start with the head node
        while current_node:
            if current_node.get_value() == value_to_remove:
                if current_node == self.head_node:
                    self.remove_head()       # If it's the head node, remove the head
                elif current_node == self.tail_node:
                    self.remove_tail()       # If it's the tail node, remove the tail
                else:
                    next_node = current_node.get_next_node()  # Get the next node
                    prev_node = current_node.get_prev_node()  # Get the previous node
                    next_node.set_prev_node(prev_node)        # Update the next node's prev reference
                    prev_node.set_next_node(next_node)        # Update the prev node's next reference
                return current_node
            current_node = current_node.get_next_node()  # Move to the next node
        return None                      # Return None if the node is not found

    # Method to return a string representation of the list
    def stringify_list(self):
        string_list = ""                    # Initialize an empty string to hold the list values
        current_node = self.head_node       # Start with the head node
        while current_node:
            if current_node.get_value() is not None:
                string_list += str(current_node.get_value()) + "\n"  # Append each value to the string
            current_node = current_node.get_next_node()  # Move to the next node in the list
        return string_list                  # Return the string representation of the list

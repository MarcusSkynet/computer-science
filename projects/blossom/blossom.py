# Importing the Node and LinkedList classes to manage data in the hash map using linked lists
from linked_list import Node, LinkedList

# Importing flower definitions to be used in the HashMap
from blossom_lib import flower_definitions

# HashMap class implementing a hash table using linked lists to handle collisions
class HashMap:

    # Initialize the hash map with a specified size
    def __init__(self, size):
        self.array_size = size                               # Set the size of the hash map
        self.array = [LinkedList() for number in range(size)] # Create an array of empty linked lists
    
    # Hash function to generate a hash code from a given key
    def hash(self, key):
        return sum(key.encode())                            # Convert the key to bytes and sum the byte values
    
    # Compressor function to ensure the hash code maps within the array size
    def compress(self, hash_code):
        return hash_code % self.array_size                  # Use modulus operation to map the hash code to an array index
    
    # Method to assign a key-value pair to the hash map
    def assign(self, key, value):
        array_index = self.compress(self.hash(key))         # Get the index in the array using hash and compress functions
        payload = Node([key, value])                        # Create a new node to store the key-value pair
        list_at_array = self.array[array_index]             # Retrieve the linked list at the computed index

        # Iterate through the linked list to check if the key already exists
        for item in list_at_array:
            if key == item[0]:                              # If the key is found, update its value
                item[1] = value
                return

        # If the key is not found, insert the new node (key-value pair) into the linked list
        list_at_array.insert(payload)
    
    # Method to retrieve the value associated with a given key
    def retrieve(self, key):
        array_index = self.compress(self.hash(key))         # Compute the array index for the given key
        list_at_index = self.array[array_index]             # Retrieve the linked list at the computed index

        # Iterate through the linked list to find the key
        for item in list_at_index:
            if key == item[0]:                              # If the key is found, return its value
                return item[1]
        
        return None                                         # Return None if the key is not found

# Create an instance of the HashMap using the length of the flower definitions as the size
blossom = HashMap(len(flower_definitions))

# Assign each flower and its meaning to the HashMap
for flower in flower_definitions:
    blossom.assign(flower[0], flower[1])

# Retrieve and print the meaning of 'daisy'
print(blossom.retrieve('daisy'))                           # Output: innocence

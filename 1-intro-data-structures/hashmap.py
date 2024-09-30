# HashMap class implementing a basic hash map (or hash table) with collision handling
class HashMap:
  
  # Initialize the hash map with a specified array size
  def __init__(self, array_size):
    self.array_size = array_size               # Set the size of the array (hash map storage)
    self.array = [None for item in range(array_size)]  # Initialize an empty array with all values set to None

  # Hash function to generate a hash code for the given key
  # Uses the sum of the byte values of the characters in the key
  def hash(self, key, count_collisions=0):
    key_bytes = key.encode()                   # Convert the key to bytes
    hash_code = sum(key_bytes)                 # Sum the byte values of the key to generate the hash code
    return hash_code + count_collisions        # Return the hash code, adjusted for collisions (if any)

  # Compressor function to ensure the hash code fits within the array size
  def compressor(self, hash_code):
    return hash_code % self.array_size         # Use modulus operation to map the hash code to a valid array index

  # Method to assign a key-value pair to the hash map
  def assign(self, key, value):
    # Compute the initial array index using the hash and compressor functions
    array_index = self.compressor(self.hash(key))
    current_array_value = self.array[array_index]  # Check the current value at the computed index

    # If the index is empty, assign the key-value pair here
    if current_array_value is None:
      self.array[array_index] = [key, value]       # Store the key-value pair in the array at the index
      return

    # If the key already exists at this index, update the value
    if current_array_value[0] == key:
      self.array[array_index] = [key, value]       # Overwrite the existing value with the new value
      return

    # Collision handling using linear probing (finding the next available slot)
    number_collisions = 1

    # Continue to search for the key or an empty slot in case of collision
    while(current_array_value[0] != key):
      new_hash_code = self.hash(key, number_collisions)  # Recompute the hash code with the collision count
      new_array_index = self.compressor(new_hash_code)   # Map the new hash code to an array index
      current_array_value = self.array[new_array_index]  # Get the value at the new index

      # If the new index is empty, assign the key-value pair there
      if current_array_value is None:
        self.array[new_array_index] = [key, value]       # Store the key-value pair
        return

      # If the key is found at the new index, update the value
      if current_array_value[0] == key:
        self.array[new_array_index] = [key, value]       # Overwrite the existing value with the new value
        return

      # Increment the collision counter and continue searching
      number_collisions += 1

    return

  # Method to retrieve the value associated with a given key
  def retrieve(self, key):
    # Compute the initial array index using the hash and compressor functions
    array_index = self.compressor(self.hash(key))
    possible_return_value = self.array[array_index]  # Get the value at the computed index

    # If the index is empty, return None (key not found)
    if possible_return_value is None:
      return None

    # If the key is found at this index, return its value
    if possible_return_value[0] == key:
      return possible_return_value[1]            # Return the value associated with the key

    # Collision handling for retrieval: use linear probing to search for the key
    retrieval_collisions = 1

    # Continue searching for the key in case of collisions
    while (possible_return_value != key):
      new_hash_code = self.hash(key, retrieval_collisions)  # Recompute the hash code with the collision count
      retrieving_array_index = self.compressor(new_hash_code)  # Map the new hash code to an array index
      possible_return_value = self.array[retrieving_array_index]  # Get the value at the new index

      # If the new index is empty, return None (key not found)
      if possible_return_value is None:
        return None

      # If the key is found at the new index, return its value
      if possible_return_value[0] == key:
        return possible_return_value[1]              # Return the value associated with the key

      # Increment the collision counter and continue searching
      retrieval_collisions += 1

    return

# Example usage of the HashMap class
hash_map = HashMap(15)   # Create a new HashMap with an array size of 15
hash_map.assign('gabbro', 'igneous')     # Assign key-value pair ('gabbro', 'igneous') to the hash map
hash_map.assign('sandstone', 'sedimentary')  # Assign key-value pair ('sandstone', 'sedimentary') to the hash map
hash_map.assign('gneiss', 'metamorphic')     # Assign key-value pair ('gneiss', 'metamorphic') to the hash map

# Retrieve and print the values associated with the keys 'gabbro', 'sandstone', and 'gneiss'
print(hash_map.retrieve('gabbro'))          # Output: igneous
print(hash_map.retrieve('sandstone'))       # Output: sedimentary
print(hash_map.retrieve('gneiss'))          # Output: metamorphic

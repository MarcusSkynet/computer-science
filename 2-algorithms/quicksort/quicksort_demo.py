from random import randrange, shuffle

def quicksort(list, start, end):
  """
  Sorts a list in-place using the Quicksort algorithm.

  Parameters:
  list (List[int]): The list of integers to be sorted.
  start (int): The starting index of the portion of the list to be sorted.
  end (int): The ending index of the portion of the list to be sorted.

  Returns:
  None
  """
  # Base case: sublist is of length 0 or 1
  if start >= end:
    return

  # Print current state of list segment being sorted
  print("Running quicksort on {0}".format(list[start: end + 1]))

  # Select a random pivot element
  pivot_idx = randrange(start, end + 1)
  pivot_element = list[pivot_idx]
  print("Selected pivot {0}".format(pivot_element))

  # Move the pivot to the end for ease of partitioning
  list[end], list[pivot_idx] = list[pivot_idx], list[end]

  # Track index for values less than the pivot
  less_than_pointer = start

  for i in range(start, end):
    if list[i] < pivot_element:
      # Log and perform swap of out-of-place element
      print("Swapping {0} with {1}".format(list[i], list[less_than_pointer]))
      list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
      less_than_pointer += 1

  # Move pivot to its final place in the sorted list
  list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
  print("{0} successfully partitioned".format(list[start: end + 1]))

  # Recursively sort left and right partitions
  quicksort(list, start, less_than_pointer - 1)
  quicksort(list, less_than_pointer + 1, end)

# Generate and shuffle the list
list = [5, 3, 1, 7, 4, 6, 2, 8]
shuffle(list)
print("PRE SORT: ", list)

# Run quicksort with detailed output
print(quicksort(list, 0, len(list) - 1))
print("POST SORT: ", list)

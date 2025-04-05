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
  # If the portion of the list is one or zero elements, it's already sorted
  if start >= end:
    return

  # Select a random index to use as pivot to ensure good average performance
  pivot_idx = randrange(start, end + 1)
  pivot_element = list[pivot_idx]

  # Move pivot to the end temporarily for easier partitioning
  list[end], list[pivot_idx] = list[pivot_idx], list[end]

  # Initialize pointer for elements smaller than the pivot
  less_than_pointer = start

  # Partition the list: all elements less than pivot go before it
  for i in range(start, end):
    if list[i] < pivot_element:
      list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
      less_than_pointer += 1

  # Place the pivot in its correct sorted position
  list[end], list[less_than_pointer] = list[less_than_pointer], list[end]

  # Recursively apply quicksort to the partitions
  quicksort(list, start, less_than_pointer - 1)
  quicksort(list, less_than_pointer + 1, end)

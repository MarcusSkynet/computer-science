def bubble_sort(arr):
    """
    Performs an optimized version of bubble sort.
    
    Args:
    arr (list): The list to be sorted.
    
    Returns:
    list: The sorted list.
    """
    
    for i in range(len(arr)):
        # Inner loop only iterates through unsorted elements
        for idx in range(len(arr) - i - 1):
            if arr[idx] > arr[idx + 1]:
                # Swap elements in place without using a temporary variable
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
    
    return arr  # Return the sorted list

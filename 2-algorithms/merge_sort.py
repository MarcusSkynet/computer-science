def merge_sort(items):
    """
    Recursively sorts a list using the merge sort algorithm.
    
    Args:
    items (list): The list of elements to be sorted.
    
    Returns:
    list: A new sorted list.
    """
    
    # Base case: A list with 0 or 1 elements is already sorted
    if len(items) <= 1:
        return items

    # Find the middle index to split the list into two halves
    middle_index = len(items) // 2
    
    # Divide the list into two smaller sublists
    left_split = items[:middle_index]  # Left half
    right_split = items[middle_index:]  # Right half

    # Recursively apply merge sort to both halves
    left_sorted = merge_sort(left_split)
    right_sorted = merge_sort(right_split)

    # Merge the sorted halves back together
    return merge(left_sorted, right_sorted)

def merge(left, right):
    """
    Merges two sorted lists into a single sorted list.
    
    Args:
    left (list): The first sorted list.
    right (list): The second sorted list.
    
    Returns:
    list: A merged and sorted list containing all elements from left and right.
    """
    
    result = []  # This will store the merged sorted elements
    
    # Compare elements from both lists and add the smallest one to the result
    while left and right:  # Continue until one of the lists is empty
        if left[0] < right[0]:  # If the first element of left is smaller
            result.append(left[0])  # Add it to the result
            left.pop(0)  # Remove the used element from the left list
        else:
            result.append(right[0])  # Add the first element of right to result
            right.pop(0)  # Remove the used element from the right list
    
    # If there are remaining elements in either list, append them
    # Since both lists are already sorted, we can simply concatenate them
    if left:
        result += left
    if right:
        result += right
    
    return result  # Return the merged and sorted list

def linear_search(search_list, target_value):
    """
    Performs a linear search to find the index of a target value in a list.
    
    Args:
    search_list (list): The list to search through.
    target_value (any): The value to find in the list.
    
    Returns:
    int: The index of the target value if found.
    
    Raises:
    ValueError: If the target value is not in the list.
    """
    
    # Iterate through the list to find the target value
    for idx in range(len(search_list)):
        if search_list[idx] == target_value:  # Check if the current element matches the target
            return idx  # Return the index where the value is found
    
    # If the target value is not found, raise an error
    raise ValueError("{0} not in list".format(target_value))

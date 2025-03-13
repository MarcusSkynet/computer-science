def pattern_search(text, pattern):
    """
    Naive pattern search algorithm that looks for occurrences of a pattern in a given text.
    
    Args:
    text (str): The string in which to search for the pattern.
    pattern (str): The substring pattern to search for in the text.
    
    Returns:
    None: Prints the indices where the pattern is found.
    """
    
    print("Input Text:", text, "Input Pattern:", pattern)
    
    # Loop through each character in the text where the pattern can fit
    for index in range(len(text) - len(pattern) + 1):
        print("Text Index:", index)
        match_count = 0  # Counter to track matched characters
        
        # Check each character of the pattern against the corresponding text character
        for char in range(len(pattern)):
            print("Pattern Index:", char)
            if pattern[char] == text[index + char]:
                match_count += 1
            else:
                break  # If a mismatch occurs, break out of the inner loop
        
        # If all characters in the pattern matched, print the occurrence index
        if match_count == len(pattern):
            print(pattern, "found at index", index)

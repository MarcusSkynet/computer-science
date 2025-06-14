"""sorts.py

Classic comparison-based sorting routines plus swap-count instrumentation.
The caller supplies a *comparison_function* of the form:

    comparison_function(a, b)  ⇨  True  ⇔  a should appear **after** b

Using this single convention allows us to describe many orderings
(alphabetical, length-based, descending, …) with tiny predicate helpers.
"""

import random                     # needed for random pivot selection

# ----------------------------- Bubble Sort ---------------------------- #
def bubble_sort(arr, comparison_function):
    """
    In-place, stable \$\\mathcal{O}(n^2)\$ bubble sort.

    A full pass bubbles the ‘largest’ element (per *comparison_function*)
    to the right.  Passes repeat until no swaps are required.
    """
    swaps  = 0                    # instrumentation only
    sorted = False
    while not sorted:             # keep sweeping until no swap happens
        sorted = True
        for idx in range(len(arr) - 1):
            if comparison_function(arr[idx], arr[idx + 1]):
                # Elements are in the wrong order – exchange them
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
                swaps  += 1
                sorted = False
    print(f"Bubble sort: There were {swaps} swaps")
    return arr                    # method sorts *and* returns same list

# ------------------------------ Quicksort ----------------------------- #
def quicksort(list, start, end, comparison_function):
    """
    In-place quicksort with a random pivot to avoid pathological inputs.

    Parameters
    ----------
    list  : list   – sequence to sort
    start : int    – inclusive start index of current sub-array
    end   : int    – inclusive end index of current sub-array
    comparison_function : callable – defines ordering
    """
    if start >= end:              # base case: 0- or 1-element slice
        return

    # --- 1. choose random pivot & move it to the end ------------------ #
    pivot_idx      = random.randrange(start, end + 1)
    pivot_element  = list[pivot_idx]
    list[end], list[pivot_idx] = list[pivot_idx], list[end]

    # --- 2. partition: ≤ pivot  |  pivot  |  ≥ pivot ------------------ #
    less_than_ptr = start
    for i in range(start, end):
        if comparison_function(pivot_element, list[i]):
            # current item belongs in the ‘less than pivot’ zone
            list[i], list[less_than_ptr] = list[less_than_ptr], list[i]
            less_than_ptr += 1

    # place pivot between partitions
    list[end], list[less_than_ptr] = list[less_than_ptr], list[end]

    # --- 3. recurse on both partitions -------------------------------- #
    quicksort(list, start,               less_than_ptr - 1,
              comparison_function)
    quicksort(list, less_than_ptr + 1,   end,
              comparison_function)

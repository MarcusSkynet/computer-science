"""utils.py

Utility functions for loading book data from CSV into a list of
dictionaries suitable for the sorting algorithms in `sorts.py`.

Each row from the CSV is augmented with two extra keys:
    • 'author_lower' – the author’s name in lowercase
    • 'title_lower'  – the book title in lowercase

Storing the lowercase versions once up-front is faster than calling
`.lower()` repeatedly inside every comparison function.
"""
import csv

# --------------------------------------------------------------------- #
# Public API                                                            #
# --------------------------------------------------------------------- #
def load_books(filename):
    """
    Read *filename* (a CSV file) and return a list of book dictionaries
    with additional lowercase keys for case-insensitive sorting.

    Parameters
    ----------
    filename : str
        Path to the CSV file (relative or absolute).

    Returns
    -------
    list[dict]
        The bookshelf, ready for downstream processing.
    """
    bookshelf = []                       # ← will hold every row
    # `with` guarantees the file is closed even if an error occurs
    with open(filename) as file:
        # DictReader turns each CSV row into a dict keyed by column name
        shelf = csv.DictReader(file)
        for book in shelf:
            # -------- augmentation ------------------------------------ #
            # Create cheap, case-folded copies so comparison functions
            # never worry about upper/lower case.
            book['author_lower'] = book['author'].lower()
            book['title_lower']  = book['title'].lower()
            # ----------------------------------------------------------- #
            bookshelf.append(book)
    return bookshelf

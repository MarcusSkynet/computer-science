"""
The Sorted Tale

Demonstration harness:

1. Load two CSV datasets (small & large).
2. Define three comparison predicates:
       • by_title_ascending
       • by_author_ascending
       • by_total_length             (author + title length)
3. Run bubble-sort on several copies and watch swap counts.
4. Run quicksort on the large dataset.
5. Print the length metric post-sort as a sanity check.
"""

import utils
import sorts

# --------------------------------------------------------------------- #
# 1. Load data                                                          #
# --------------------------------------------------------------------- #
bookshelf      = utils.load_books('books_small.csv')
long_bookshelf = utils.load_books('books_large.csv')

# independent copies so each experiment starts unsorted
bookshelf_v1 = bookshelf.copy()
bookshelf_v2 = bookshelf.copy()

# --------------------------------------------------------------------- #
# 2. Comparison functions                                               #
# --------------------------------------------------------------------- #
def by_title_ascending(book_a, book_b):
    # Alphabetical on *title*
    return book_a['title_lower'] > book_b['title_lower']

def by_author_ascending(book_a, book_b):
    # Alphabetical on *author*
    return book_a['author_lower'] > book_b['author_lower']

def by_total_length(book_a, book_b):
    # Longer (author + title) goes later
    return (len(book_a['author_lower']) + len(book_a['title_lower'])
            > len(book_b['author_lower']) + len(book_b['title_lower']))

# --------------------------------------------------------------------- #
# 3. Bubble-sort experiments                                            #
# --------------------------------------------------------------------- #
sort_1 = sorts.bubble_sort(bookshelf,      by_title_ascending)
sort_2 = sorts.bubble_sort(bookshelf_v1,   by_author_ascending)
sort_3 = sorts.bubble_sort(long_bookshelf, by_total_length)

# --------------------------------------------------------------------- #
# 4. Quicksort experiment                                               #
# --------------------------------------------------------------------- #
# Note: quicksort sorts in place and returns None
sorts.quicksort(long_bookshelf, 0,
                len(long_bookshelf) - 1,
                by_total_length)

# --------------------------------------------------------------------- #
# 5. Verify order                                                       #
# --------------------------------------------------------------------- #
for book in long_bookshelf:
    # Each printed number should be ≥ the previous one
    print(len(book['author_lower']) + len(book['title_lower']))

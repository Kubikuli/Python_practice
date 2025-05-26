#!/usr/bin/env python3

from collections import Counter

# Custom exception
class ValidationError(Exception):
    pass

def upd_word_counts(sentence: str, word_counts: Counter=None, *, to_upper=False) -> Counter:
    """Returns Counter in 'word_counts' with updated values with number of words from 'sentence'.
    up_upper declares if all the words in 'sentence' should be transformed to uppercase.

    >>> upd_word_counts('That that exists exists in that that that that exists exists in', to_upper = True) 
    Counter({'THAT': 6, 'EXISTS': 4, 'IN': 2})

    >>> upd_word_counts('du du du du po le du do pre du du i do za du du', Counter(['po','le'])) 
    Counter({'du': 9, 'po': 2, 'le': 2, 'do': 2, 'pre': 1, 'i': 1, 'za': 1})

    >>> upd_word_counts('du du du du po le du do pre du du i do za du du', Counter(['po','le']), True) 
    Traceback (most recent call last):
    ...
    TypeError: upd_word_counts() takes from 1 to 2 positional arguments but 3 were given

    >>> upd_word_counts('du du du du po le du do pre du du i do za du du', Counter(['PO','LE']), to_upper = True) 
    Counter({'DU': 9, 'PO': 2, 'LE': 2, 'DO': 2, 'PRE': 1, 'I': 1, 'ZA': 1})

    >>> all_words = Counter(('a','b','c','a')); upd_word_counts('du du du du po le du do pre du du i do za du du', all_words, to_upper = True) 
    Traceback (most recent call last):
    ...
    ValidationError

    >>> all_words = Counter(('A','B','C','A')); upd_word_counts('du du du du po le du do pre du du i do za du du', all_words, to_upper = True) 
    Counter({'DU': 9, 'DO': 2, 'A': 2, 'PO': 1, 'LE': 1, 'PRE': 1, 'I': 1, 'ZA': 1, 'B': 1, 'C': 1})

    >>> print(all_words)
    Counter({'A': 2, 'B': 1, 'C': 1})
    """

    # If no counter was provided, create a new one
    if word_counts is None:
        word_counts = Counter()

    # Check if every key in words_count is uppercase letter
    # If not, throws an exception
    if to_upper:
        for key in word_counts:
            if not isinstance(key, str) or not key.isupper():
                raise ValidationError()

        sentence = sentence.upper()

    words = sentence.split()

    return Counter(words) + word_counts


if __name__ == "__main__":
    import doctest
    doctest.testmod()

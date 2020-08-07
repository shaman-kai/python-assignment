# python-assignment

This repository contains two modules that achieve the same goal in two different ways.
Module 1 'scrambled_words.py' is longer, but easier to understandand and modify, because it requires no knowledge of regular expressions operations (re).
Module 2 're_scrambled_words' is more efficient, but requires knowledge of re to understand and modify.

_______________________________

MODULE 1 'SCRAMBLED_WORDS.PY'

This program is a module that contains 4 functions to "scramble" a piece of text:

    • shuffle_middles: to randomly reorder all but the first and last letters of each word.
    • shuffle_words: to randomly reorder all the letters in each word.    
    • shuffle_short_words: to randomly reorder all letters in words shorter than n letters.    
    • random_upper: to randomly make some letters lowercase and some uppercase.

In addition, it contains 2 helper functions:

    • full_split: to split a piece of text into a list of words and groups of punctuation 
    (to make sure punctuation is not "scrambled" and stays in its place).
    • spaced_text: to assemble a list of words and punctuation back into text 
    (after each word has been "scrambled") with spaces in appropriate positions 
    (e.g. before an opening bracket but after a closing bracket).
    
Main and helper functions:

    • The helper function 1 splits text into segments, then main functions 1-4 shuffle letters within them, 
    then helper function 2 assembles scrambled segments back into a single text string.
    • To use main fuctions, helper functions should also be imported, 
    so it is recommended to import the module as a whole.    
    • However, helper functions can also be used independently.

_______________________________

MODULE 2 'RE_SCRAMBLED_WORDS.PY'

This module contains 4 functions to "scramble" a piece of text:

    • shuffle_middles: to randomly reorder all but the first and last letters of each word.
    • shuffle_words: to randomly reorder all the letters in each word.
    • shuffle_short_words: to randomly reorder all letters in words shorter than n letters.
    • random_upper: to randomly make some letters lowercase and some uppercase.

In addition, it contains 2 helper functions:

    • shuffled_middle_word: takes a result of patterning consisting of groups (re.Match type) 
    and returns string with shuffled middle.
    • shuffled_word: takes a result of patterning consisting of groups (re.Match type) and shuffleseach of them.
   
Main and helper functions:

    • The helper functions only work on re.Match variables,but can be used independently.
    • To use main functions, helper functions need to be imported, so it is recommended to import this module as a whole.

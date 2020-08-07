# python-assignment

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


The helper function 1 splits text into segments, then main functions 1-4 shuffle letters within them,
    then helper function 2 assembles scrambled segments back into a single text string.
    
To use main fuctions, helper functions should also be imported,
    so it is recommended to import the module as a whole.
    
However, helper functions can also be used independently.

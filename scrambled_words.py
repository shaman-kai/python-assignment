"""
This module contains 4 functions to "scramble" a piece of text:
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
"""

#%% HELPER FUNCTION 1

def full_split(text):
    """
    This function takes a piece of text and splits it into words and punctuation so that hyphens and apostrophs do not split the word, and groups of punctuation marks like "?!" are treated as one entity.
        
    INPUT AND OUTPUT:
        In: Takes a single string of any length as an input argument called text.
        Out: Returns a list containing words and (groups of) punctuation marks.
    EXAMPLE:
        In : full_split("... Didn't you buy the e-tickets (and even 2)?!")
        Out: ['...', "Didn't", 'you', 'buy', 'the', 'e-tickets', '(', 'and', 'even', '2', ')?!']
    ERROR: 
        If input argument is not a string, raises a TypeError("The input argument should be a piece of text as a string").
    """
    
    if not type(text) is str:
        raise TypeError("The input argument should be a piece of text as a string")
    
    # Split text into segments consisting of words+punctuation (e.g. '...X-men-2?!.'):
    words_punctuated = text.split()
    
    # Separate punctuation at the end of each segment (e.g. '...X-men-2', '?!.'):
    words_clean_ended = []
    for word in words_punctuated:
        ending = word[-1]
        if ending.isalpha() == True or ending.isdigit() == True:
        # (if necessary, word endings other than letters and numbers can be allowed by adding another 'or')
            word = word
            words_clean_ended.append(word)
        elif any(x.isdigit() for x in word) == False and any(x.isalpha() for x in word) == False:
            word = word
            words_clean_ended.append(word)
        else:
            positions = [(x) for x, y in enumerate(word) if y.isalpha() or y.isdigit()]
            last_letter = positions[-1]+1
            word1 = word[0:last_letter]
            words_clean_ended.append(word1)
            word2 = word[last_letter:]
            words_clean_ended.append(word2)
    while '' in words_clean_ended: words_clean_ended.remove('')
    
    # Separate punctuation at the beginning of each segment (e.g. '...', 'X-men-2', '?!.'):
    words_clean = []
    for word in words_clean_ended:
        beginning = word[0]
        if beginning.isalpha() == True or beginning.isdigit() == True:
        # (if necessary, word beginnings other than letters and numbers can be allowed by adding another 'or')
            word = word
            words_clean.append(word)
        elif any(x.isdigit() for x in word) == False and any(x.isalpha() for x in word) == False:
            word = word
            words_clean.append(word)
        else:
            positions = [(x) for x, y in enumerate(word) if y.isalpha() or y.isdigit()]
            first_letter = positions[0]
            word1 = word[0:first_letter]
            words_clean.append(word1)
            word2 = word[first_letter:]
            words_clean.append(word2)
    while '' in words_clean: words_clean.remove('')
    
    return words_clean

    
#%% HELPER FUNCTION 2

def spaced_text(word_list):
    """
    This function takes a list of strings that can contain e.g. words, numbers and (groups of) punctuation marks and assembles it into a text (as a single string) with spaces in appropriate positions (e.g. before an opening bracket but after a closing bracket).
    
    INPUT AND OUTPUT:
        In: Takes a list of strings as an input argument called word_list.
        Out: Returns a text as a single string.
    EXAMPLE:
        In : spaced_text(['...', "Didn't", 'you', 'buy', 'the', 'e-tickets', '(', 'and', 'even', '2', ')?!'])
        Out: "... Didn't you buy the e-tickets (and even 2)?!"
    ERRORS: 
        If input argument is not a list, raises a TypeError("The input argument should be a list containing strings").
        If the input list contains something else than strings, raises a TypeError("All items in the input argument list should be strings")
    """
    
    if not type(word_list) is list:
        raise TypeError("The input argument should be a list containing strings")
    if all(isinstance(item, str) for item in word_list) == False:
        raise TypeError("All items in the input argument list should be strings")
    
    words_spaced = [word_list[0]]
    for word in word_list[1:]:
        beginning = word[0]
        # Add spaces before words and numbers:
        if beginning.isalpha() == True or beginning.isdigit() == True:
        # (if necessary, word beginnings other than letters and numbers can be allowed by adding another 'or')
            word1 = ' '+ word
            words_spaced.append(word1)
        # Do not add spaces before punctuation:
        else:
            word2 = word
            words_spaced.append(word2)
    # Join the word list into a single string of text:
    part_spaced_text = ''.join(words_spaced)
    # For some exceptional punctuation signs that go before a word, such as (<[“, put a space before, not after them:
    spaced_text = part_spaced_text.replace("( ", " (").replace("< ", " <").replace("[ ", " [").replace("“ ", " “")
    # (if necessary, other exceptional punctuation marks can be added by adding another 'replace')
    return spaced_text

#%% MAIN FUNCTION 1

def shuffle_middles(text):
    """
    This function takes a piece of text and randomly reorders all but the first and last letters of each word.
    
    INPUT AND OUTPUT:
        In: Takes a single string containing a piece of text as the input argument called text.
        Out: Returns a text as a single string.
    EXAMPLE:
        In : shuffle_middles("... Didn't you purchase the e-tickets (and actually 2)?!")
        Out: "... Dnid't you pruchsae the etiekt-cs (and acuallty 2)?!"
    ERROR: 
        If input argument is not a string, raises a TypeError("The input argument should be a piece of text as a string").
    """
    
    import random
    # Split text into fragments separating words and punctuation:
    words_clean = full_split(text)
    
    # For every word, shuffle all letters except first and last, punctuation stays the same:
    randomized_words = []
    for word in words_clean:
        beginning = word[0]
        if  beginning.isalpha() == False and beginning.isdigit() == False:
        # (if one also wishes to shuffle groups of punctuation, this condition can be omitted)
            end_result = word
            randomized_words.append(end_result)
        elif len(word) < 4: # because in makes no sence to shuffle middles for words of 3 letters or less
            end_result = word
            randomized_words.append(end_result)
        else:
            middle = word[1:-1]
            rand_middle = random.sample(middle,len(middle))
            result = ''.join(rand_middle)
            end_result = word[0]+result+word[-1]
            randomized_words.append(end_result)
            # (if necessary, this function can be mofified to shuffle any part of word (e.g. from 3rd to second-to-last letter, or the first/second half of word) by changing numbers in variables 'middle' and 'end_result')
    
    # Join scrambled words back into text with punctuation and spaces:
    new_text = spaced_text(randomized_words)
    return new_text

#%% MAIN FUNCTION 2

def shuffle_words(text):
    """
    This function takes a piece of text and randomly reorders all letters of each word.
    
    INPUT AND OUTPUT:
        In: Takes a single string containing a piece of text as the input argument called text.
        Out: Returns a text as a single string.
    EXAMPLE:
        In : shuffle_words("... Didn't you purchase the e-tickets (and actually 2)?!")
        Out: "... idtD'n uyo scpuaher eht stei-kcte (and tulclyaa 2)?!"
    ERROR: 
        If input argument is not a string, raises a TypeError("The input argument should be a piece of text as a string").
    """ 
    
    import random
    # Split text into fragments separating words and punctuation:
    words_clean = full_split(text)
    
    # Shuffle all letters in each word, punctuation stays the same:
    randomized_words = []
    for word in words_clean:
        beginning = word[0]
        if  beginning.isalpha() == False and beginning.isdigit() == False:
        # (if one also wishes to shuffle groups of punctuation, this condition can be omitted)
            end_result = word
            randomized_words.append(end_result)
        else:
            shuffled_letters = random.sample(word,len(word))
            word = ''.join(shuffled_letters)
            randomized_words.append(word)
    
    # Join scrambled words back into text with punctuation and spaces:
    new_text = spaced_text(randomized_words)
    return new_text

#%% MAIN FUNCTION 3

def shuffle_short_words(text, n):
    """
    This function takes a piece of text and randomly reorders all letters in words that are shorter than a given number of letters.
    
    INPUT AND OUTPUT:
        In: Takes a single string containing a piece of text as the first input argument called text. Takes a single integer that determines the number of letters as the second input argument n.
        Out: Returns a text as a single string.
    EXAMPLE:
        In : shuffle_short_words("... Didn't you purchase the e-tickets (and actually 2)?!", 7)
        Out: "... dDt'ni oyu purchase the e-tickets (nda actually 2?!)"
    ERROR: 
        If the first input argument is not a string, raises a TypeError("The input argument should be a piece of text as a string").
    """ 
       
    import random
    # Split text into fragments separating words and punctuation:
    words_clean = full_split(text)
    
    # Shuffle all letters in words shorter than n, punctuation stays the same:
    randomized_words = []
    for word in words_clean:
        beginning = word[0]
        if  beginning.isalpha() == False and beginning.isdigit() == False:
        # (if one also wishes to shuffle groups of punctuation, this condition can be omitted)
            end_result = word
            randomized_words.append(end_result)
        elif len(word) < n:
        # (if necessary, this condition can be modified to shuffle words longer or equal to certain length by changing the '<' operator)
            shuffled_letters = random.sample(word,len(word))
            result = ''.join(shuffled_letters)
            randomized_words.append(result)
        else:
            result = word
            randomized_words.append(result)    
    
    # Join scrambled words back into text with punctuation and spaces:
    new_text = spaced_text(randomized_words)
    return new_text

#%% MAIN FUNCTION 4

def random_upper(text):
    """
    This function takes a piece of text and randomly  makes some letters lowercase and some uppercase.
    
    INPUT AND OUTPUT:
        In: Takes a single string containing a piece of text as the input argument called text.
        Out: Returns a text as a single string.
    EXAMPLE:
        In : shuffle_words("... Didn't you purchase the e-tickets (and actually 2)?!")
        Out: "... dIDn'T yOu PuRchasE tHe E-tIcKEtS (AND ACTUaLLy 2)?!"
    ERROR: 
        If input argument is not a string, raises a TypeError("The input argument should be a piece of text as a string").
    """
    
    if not type(text) is str:
        raise TypeError("The input argument should be a piece of text as a string")
    
    import random
    new_text = ''.join(random.choice([x.upper(), x.lower()]) for x in text)
    return new_text


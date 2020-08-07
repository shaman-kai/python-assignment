#%%

import re
import random

#%% Helper functions

def shuffled_middle_word(m):
    """
    This function takes a result of string patterning consisting of groups (e.g. beginning of string + middle + end), shuffles the second group and returns a string joining 1 group + shuffled 2nd group + 3rd group. Intended use: to get a string with shuffled middle.
        INPUT AND OUTPUT:
        In: Takes a single input argument of type re.Match.
        Out: Returns a single string.
    EXAMPLE:
        In : m = p.match('abcdf')
        Out: 'abcdfbcdc'
    ERROR: 
        If input argument is not a re.Match, raises a TypeError("The input argument should be a piece of text as a string").
    """
    # raising an error:
    if not type(m) is re.Match:
        raise TypeError("The input argument should be of type re.Match")
        
    inner_word = list(m.group(2))
    random.shuffle(inner_word)
    return m.group(1) + "".join(inner_word) + m.group(3)
    #(if necessary, the segmentation of a word can be changed to any number of segments (not necessarily 3); in that case, the pattern in shuffle_middles_re should be changed accordingly)
 
    
def shuffled_word(m):
    """
    This function takes a result of string patterning consisting of groups and shuffles each group.
        INPUT AND OUTPUT:
        In: Takes a single input argument of type re.Match.
        Out: Returns a single string.
    EXAMPLE:
        In : m = p.match('abcdf')
        Out: 'dafcb'
    ERROR: 
        If input argument is not a re.Match, raises a TypeError("The input argument should be a piece of text as a string").
    """
        # raising an error:
    if not type(m) is re.Match:
        raise TypeError("The input argument should be of type re.Match")
    
    word = list(m.group(0))
    random.shuffle(word)
    return "".join(word)
    #(if necessary, this function can be changed to perform other operations instead of shuffling by writing something else instead of random.shuffle(word). Results of main functions shuffle_words_re and shuffle_short_words_re will change accordingly)

#%% Main functions
     
def shuffle_middles_re(text):
    """
    This function takes a piece of text and randomly reorders all but the first and last letters of each word.
    
    INPUT AND OUTPUT:
        In: Takes a single string containing a piece of text as the input argument called text.
        Out: Returns a text as a single string.
    EXAMPLE:
        In : shuffle_middles("... Didn't you purchase the e-tickets (and actually 2)?!")
        Out: "... Ddin't you phucrase the e-ttcikes (and acltluay 2)?!"
    ERROR: 
        If input argument is not a string, raises a TypeError("The input argument should be a piece of text as a string").
    """
    # raising an error:
    if not type(text) is str:
        raise TypeError("The input argument should be a piece of text as a string")
        
    return re.sub(r"(\w)(\w+)(\w)", shuffled_middle_word, text)
    # (if necessary, the pattern first letter + middle + last letter (\w)(\w+)(\w) can be substituted by any other pattern: with a different number of initial and/or end letters, different word segmentation (e.g.in half) or a different sentence segmentation)


def shuffle_words_re(text):
    """
    This function takes a piece of text and randomly reorders all letters of each word.
    
    INPUT AND OUTPUT:
        In: Takes a single string containing a piece of text as the input argument called text.
        Out: Returns a text as a single string.
    EXAMPLE:
        In : shuffle_words("... Didn't you purchase the e-tickets (and actually 2)?!")
        Out: "... ndDi't yuo spuaechr eht e-ekisctt (nda luyalcta 2)?!"
    ERROR: 
        If input argument is not a string, raises a TypeError("The input argument should be a piece of text as a string").
    """ 
    # raising an error:
    if not type(text) is str:
        raise TypeError("The input argument should be a piece of text as a string")
        
    return re.sub(r"(\w+)", shuffled_word, text)
    # (if necessary, the specified pattern (\w+) can be changed, if one wants to shuffle not words, but bigger|smaller segments of text (e.g.sentences))


def shuffle_short_words_re(text, n):
    """
    This function takes a piece of text and randomly reorders all letters in words that are shorter than or equal to a given number of letters (<=n).
    
    INPUT AND OUTPUT:
        In: Takes a single string containing a piece of text as the first input argument called text. Takes a single integer that determines the number of letters as the second input argument n.
        Out: Returns a text as a single string.
    EXAMPLE:
        In : shuffle_short_words("... Didn't you purchase the e-tickets (and actually 2)?!", 7)
        Out: "... niDd't uyo purchase het e-tickets (nad actually 2)?!"
    ERROR: 
        If the first input argument is not a string, raises a TypeError("The input argument should be a piece of text as a string").
        If the second input argument is not a number, raises a TypeError("The second input argument should be a number")
    """ 
    # raising an error:
    if not type(text) is str:
        raise TypeError("The first input argument should be a piece of text as a string")
    if not type(n) is int:
        raise TypeError("The second input argument should be a number")
        
    return re.sub(r"\b\w{,%s}\b" % n, shuffled_word, text)
    # (if necessary, instead of an upper limit %s in {,%s} one can set a lower limit {%s,} to scramble words longer than n, or both limits to scramble words between certain lengths)


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
    # raising an error:
    if not type(text) is str:
        raise TypeError("The input argument should be a piece of text as a string")
        
    new_text = ''.join(random.choice([x.upper(), x.lower()]) for x in text)
    return new_text

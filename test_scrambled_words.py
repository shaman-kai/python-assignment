"""
Tests the scrambled_words module
"""

import pytest
import scrambled_words

#%% Testing results and exceptions of the helper function full_split

def test_full_split():
    result = scrambled_words.full_split("... Didn't you buy “e-tickets” (and even 2)?!")
    assert result == ['...', "Didn't", 'you', 'buy', '“', 'e-tickets', '”', '(', 'and', 'even', '2', ')?!']
    
def test_full_split_exception_not_string():
    with pytest.raises(TypeError):
        scrambled_words.full_split(4)
        
#%% Testing results and exceptions of the helper function spaced_text

def test_spaced_text():
    result = scrambled_words.spaced_text(['...', "Didn't", 'you', 'buy', '“', 'e-tickets', '”', '(', 'and', 'even', '2', ')?!'])
    assert result == "... Didn't you buy “e-tickets” (and even 2)?!"
    
def test_spaced_text_exception_not_list():
    with pytest.raises(TypeError):
        scrambled_words.spaced_text(4)

def test_spaced_text_exception_not_strings_in_list():
    with pytest.raises(TypeError):
        scrambled_words.spaced_text(["Mary", "John", 4, "Paul"])

#%% Testing exceptions of the main function suffle_middles

def test_shuffle_middles_exception_not_string():
    with pytest.raises(TypeError):
        scrambled_words.shuffle_middles(4)

#%% Testing exceptions of the main function shuffle_words

def test_shuffle_words_exception_not_string():
    with pytest.raises(TypeError):
        scrambled_words.shuffle_words(4)
        
#%% Testing exceptions of the main function shuffle_short_words
        
def test_shuffle_short_words_exception_not_string():
    with pytest.raises(TypeError):
        scrambled_words.shuffle_short_words(2,5)
        
#%% Testing exceptions of the main function random_upper

def test_random_upper_exception_not_string():
    with pytest.raises(TypeError):
        scrambled_words.random_upper(4)
        

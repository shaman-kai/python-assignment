# -*- coding: utf-8 -*-
"""
Tests the re_scrambled_words module
"""

import pytest
import re_scrambled_words

#%% Testing exceptions of the helper function shuffled_middle_word:

def test_shuffled_middle_word_exception_wrong_type():
    with pytest.raises(TypeError):
        re_scrambled_words.shuffled_middle_word(4)

#%% Testing exceptions of the main function shuffle_middles_re:

def test_shuffled_word_exception_wrong_type():
    with pytest.raises(TypeError):
        re_scrambled_words.shuffled_word(4)
        
#%% Testing exceptions of the main function shuffle_middles_re:

def test_shuffle_middles_re_exception_not_string():
    with pytest.raises(TypeError):
        re_scrambled_words.shuffle_middles_re(4)

#%% Testing exceptions of the main function shuffle_words_re:

def test_shuffle_words_re_exception_not_string():
    with pytest.raises(TypeError):
        re_scrambled_words.shuffle_words_re(4)
        
#%% Testing exceptions of the main function shuffle_short_words_re:
        
def test_shuffle_short_words_re_exception_not_string():
    with pytest.raises(TypeError):
        re_scrambled_words.shuffle_short_words_re(2,5)
        
#%% Testing exceptions of the main function random_upper:

def test_random_upper_exception_not_string():
    with pytest.raises(TypeError):
        re_scrambled_words.random_upper(4)
        

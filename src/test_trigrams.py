# -*- coding: utf-8 -*-
import pytest

TEST_STRING = 'I wish I may I wish I might'
TEST_FILE = '../test.txt'
TEST_DICT = {('I', 'wish'): ["I", "I"],
    ('wish', 'I'): ["may", "might"],
    ('may', 'I'): ["wish"],
    ('I', 'may'): ["I"]}
TEST_TUPLE = ('may', 'I')


def test_get_input():
    """Test to see if import corectly reads from a known file."""
    from trigrams import get_input
    assert get_input(TEST_FILE) == TEST_STRING


def test_has_dictionary():
    """Test to see if read_imput will return a dictionary."""
    from trigrams import read_input
    assert read_input("") == {}


def test_dictionary_values():
    """Test to see if read_input will currectly form a dictionary."""
    from trigrams import read_input
    assert read_input(TEST_STRING) == TEST_DICT


def test_select_word():
    """Test to see if pselect_word returns correct value."""
    from trigrams import select_word
    assert select_word(TEST_DICT, TEST_TUPLE) == 'wish'

def test_start_of_story():
    from trigrams import start_of_story
    assert start_of_story(TEST_TUPLE) == 'may I'

def test_add_to_story():
    from trigrams import add_to_story
    assert add_to_story(TEST_STRING, 'add') == 'I wish I may I wish I might add'


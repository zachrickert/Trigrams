# -*- coding: utf-8 -*-
import pytest

TEST_STRING = 'I wish I may I wish I might'
TEST_FILE = '../test.txt'
TEST_DICT = {('I', 'wish'): ["I", "I"],
    ('wish', 'I'): ["may", "might"],
    ('may', 'I'): ["wish"],
    ('I', 'may'): ["I"]}


def test_get_input():
    from trigrams import get_input
    assert get_input(TEST_FILE) == TEST_STRING


def test_has_dictionary():
    from trigrams import read_input
    assert read_input("") == {}

def test_dictionary_values():
    from trigrams import read_input
    assert read_input(TEST_STRING) == TEST_DICT

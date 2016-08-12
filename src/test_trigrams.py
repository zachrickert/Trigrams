# -*- coding: utf-8 -*-


TEST_STRING = "I wish I may I wish I might"
TEST_FILE = 'sample.txt'
TEST_DICT = {('I', 'wish'): ["I", "I"],
             ('wish', 'I'): ["may", "might"],
             ('may', 'I'): ["wish"],
             ('I', 'may'): ["I"]}
TEST_TUPLE = ('may', 'I')
TEST_LIST = ['I', 'wish', 'I', 'may', 'I', 'wish', 'I', 'might']
TEST_STRING2 = 'first second third first second'
TEST_LENGTH = 30


def test_file_length():
    """Test to check trigram file length."""
    from trigrams import main
    assert len(main(TEST_STRING2, TEST_LENGTH).split()) == TEST_LENGTH


def test_get_input():
    """Test to see if import corectly reads from a known file."""
    from trigrams import get_input
    assert get_input(TEST_FILE) == TEST_STRING


def test_has_dictionary():
    """Test to see if read_imput will return a dictionary."""
    from trigrams import create_trigram_dict
    assert create_trigram_dict("") == {}


def test_dictionary_values():
    """Test to see if create_trigram_dict will currectly form a dictionary."""
    from trigrams import create_trigram_dict
    assert create_trigram_dict(TEST_STRING) == TEST_DICT


def test_select_word():
    """Test to see if pselect_word returns correct value."""
    from trigrams import select_word
    assert select_word(TEST_DICT, TEST_TUPLE) == 'wish'


def test_select_random_start():
    """Test to see if random start returns a key in the dictionary."""
    from trigrams import select_random_start
    assert tuple(select_random_start(TEST_DICT)) in TEST_DICT.keys()


def test_formatting():
    """Test to see if story is correctly formatted."""
    from trigrams import formatting
    assert formatting(TEST_LIST) == TEST_STRING

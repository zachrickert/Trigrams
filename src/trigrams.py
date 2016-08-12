# -*- coding: utf-8 -*-
"""Trigrams can be used to mutate text into new, surreal, forms."""
import io
from random import choice
import sys


def main(file_source, output_amt=200):
    """Main takes user input source file & integer for output size, returns a trigram."""
    file_data = get_input(file_source)
    trigram_dict = create_trigram_dict(file_data)
    story = select_random_start(trigram_dict)
    while True:
        current_phrase = (story[-2], story[-1])
        if len(story) >= output_amt or current_phrase not in trigram_dict:
            break

        next_word = select_word(trigram_dict, current_phrase)
        story.append(next_word)

    print(formatting(story))


def get_input(file_source):
    """Read data from a file."""
    f = io.open(file_source, encoding='utf-8')
    data = f.read().rstrip('\n')
    f.close()
    return data


def create_trigram_dict(raw_data):
    """Take raw data from a file and create a dictionary."""
    data = raw_data.split()
    trigram_dict = {}

    for idx, word in enumerate(data):
        if idx <= len(data) - 3:
            dict_key = data[idx], data[idx + 1]
            dict_value = data[idx + 2]

            trigram_dict.setdefault(dict_key, []).append(dict_value)

    return trigram_dict


def select_random_start(my_dict):
    """Return a random key from a dictionary."""
    return list(choice(list(my_dict.keys())))


def select_word(my_dict, my_key):
    """Return a radom value from a dictionary."""
    return choice(my_dict[my_key])


def formatting(my_list):
    """Format story by joining the list together with spaces."""
    return(' '.join(my_list))


if __name__ == '__main__':
        main(sys.argv[1], int(sys.argv[2]))

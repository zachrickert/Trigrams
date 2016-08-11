# -*- coding: utf-8 -*-
import io

from random import choice

"""Trigrams can be used to mutate text into new, surreal, forms."""

def main(file_source, output_amt=200):
    file_data = get_input(file_source)
    trigram_dict = read_input(file_data)
    current_key = choice(trigram_dict)
    story = start_of_story(current_key)
    story_count = 0
    while True:
        if story_count > output_amt or current_key not in trigram_dict:
            break
        next_word = select_word(trigram_dict, current_key)
        add_to_story(story, next_word)
        story_count += 1
        current_key = (current_key[1], next_word)
    print(story)


def get_input(file_source):
    """Reads the data from a file."""
    f = io.open(file_source, encoding='utf-8')
    data = f.read()
    f.close()
    return data


def read_input(raw_data):
    """Take raw data from a file and create a dictionary."""
    data = raw_data.split()
    trigram_dict = {}

    for idx, word in enumerate(data):
        if idx <= len(data) - 3:
            dict_key = data[idx], data[idx + 1]
            dict_value = data[idx + 2]

            if dict_key not in trigram_dict:
                trigram_dict[dict_key] = []

            trigram_dict[dict_key].append(dict_value)

    return trigram_dict


def select_word(my_dict, my_key):
    """Return a value from a dictionary."""
    return choice(my_dict[my_key])


def start_of_story(my_tuple):
    return "{0} {1}".format(my_tuple[0], my_tuple[1])


def add_to_story(story, new_word):
    return "{} {}".format(story, new_word)

if __name__ == '__main__':
    main('../test.txt')

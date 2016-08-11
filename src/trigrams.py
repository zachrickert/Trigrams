# -*- coding: utf-8 -*-
"""Trigrams can be used to mutate text into new, surreal, forms."""
import io

from random import choice


def main(file_source, output_amt=200):
    file_data = get_input(file_source)
    trigram_dict = create_trigram_dict(file_data)
    current_phrase = select_random_start(trigram_dict)
    story = start_of_story(current_phrase)
    story_count = 2
    while True:
        if story_count > output_amt or current_phrase not in trigram_dict:
            break
        next_word = select_word(trigram_dict, current_phrase)
        add_to_story(story, next_word)
        story_count += 1
        current_phrase = (current_phrase[1], next_word)
    print(story)


def get_input(file_source):
    """Read data from a text file."""
    f = io.open(file_source, encoding='utf-8')
    data = f.read()
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

            if dict_key not in trigram_dict:
                trigram_dict[dict_key] = []

            trigram_dict[dict_key].append(dict_value)

    return trigram_dict


def select_random_start(my_dict):
    """Return a random key from a dictionary."""
    for key in my_dict:
        return key


def select_word(my_dict, my_key):
    """Return a value from a dictionary."""
    return choice(my_dict[my_key])


def start_of_story(my_tuple):
    """Change one tuple into a phrase."""
    return "{0} {1}".format(my_tuple[0], my_tuple[1])


def add_to_story(story, new_word):
    """Add a single word onto the end of the story."""
    return "{} {}".format(story, new_word)

if __name__ == '__main__':
    main('../test.txt')

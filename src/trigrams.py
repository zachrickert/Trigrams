# -*- coding: utf-8 -*-
import io

"""Trigrams can be used to mutate text into new, surreal, forms."""

def main():
    pass

def get_input(file_source):
    """Reads the data from a file."""
    f = io.open(file_source, encoding='utf-8')
    data = f.read()
    f.close()
    print(data)
    return data


def read_input(raw_data):
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

# def select_word():
#     pass



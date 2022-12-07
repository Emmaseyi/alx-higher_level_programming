#!/usr/bin/python3

def complex_delete(a_dictionary, value):
        test_dict = dict(a_dictionary)
        for k, v in test_dict.items():
            if v == value:
                del a_dictionary[k]
        return a_dictionary

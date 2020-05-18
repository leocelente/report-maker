#!/usr/bin/python3
'''
    Given an dict that represents the line structure of a log file.
    Generates a group-named Regular Expression matches and extracts
    the parameters according to the dict

    RegEx Named Grouping Reference:
    https://docs.python.org/3.8/howto/regex.html#non-capturing-and-named-groups
'''

import re


def make_regex(structure, separator):
    '''
        Generates the RegEx given structure and separator
    '''
    regex = r""
    for key in structure:
        # uses Python Named Group RegEx Extension: ?P<group name>
        regex = regex + \
            (r"(?P<" + key + ">{" + structure[key]+"})") + separator
    date_re = r"[\d]{1,2}\-[\d]{1,2}\-[\d]{4}"      # DD-MM-YYYY format date
    integer_re = r"[\-]?[\d]+"                      # signed integer
    float_re = r"[\-][\d]+\.[\d]+"                  # signed float
    str_re = r"[\w]+"
    regex = regex.replace(r"{date}", date_re)
    regex = regex.replace(r"{integer}", integer_re)
    regex = regex.replace(r"{float}", float_re)
    regex = regex.replace(r"{str}", str_re)
    # replaces last separator with EOL
    return regex[0:-1] + r'$'


def extract_as_dict(line, structure, separator):
    '''
        Does the matching and returns the parameters dict
    '''
    my_re = make_regex(structure, separator)
    match = re.match(my_re, line)
    if match:
        return match.groupdict()
    else:
        return None


def parse_file():
    # construct structure with menu?
    # read file
    # populate lists for each data type
    # generate statistics & graphs...
    # ?? profit
    pass


if __name__ == "__main__":
    filename = "test.log"
    structure = {
        "my_date": "date",
        "my_int": "integer",
        "my_float": "float",
        "my_str": "str"
    }
    separator = ";"
    line = "1-12-2021;123;-123.456;xa"

    parameters = extract_as_dict(line, structure, separator)
    if parameters:
            print("Extracted Data:")
            print(parameters)
        else:
            print("Failed to parse")

#!/usr/bin/python3
'''
    Given an dict that represents the line structure of a log file.
    Generates a group-named Regular Expression matches and extracts
    the parameters according to the dict

    RegEx Named Grouping Reference:
    https://docs.python.org/3.8/howto/regex.html#non-capturing-and-named-groups
'''

import re
import sys
import json
import getopt

HELP_MSG = """
File Parser:
    USAGE: ./main.py [OPTIONS] <log_file>
    
    OPTIONS:
        -f  <filename>  :    File containing the line structure in json format
    
    EXAMPLE:
        ./main.py -f my_line_structure.json my_log.log
            """

def make_regex(structure, separator):
    '''
        Generates the RegEx given structure and separator
    '''
    regex = r""
    for key in structure:
        if key =="separator":
            continue
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
    s_file = ""
    args  = sys.argv[1:]
    opts, args = getopt.getopt(args, "hf:i:")
    for opt, arg in opts:
        if opt in ("-f"):
            s_file = arg
        elif opt in ("-i"):
            print("inline structures not implemented yet")
            exit()
        elif opt in ("-h"):
            print(HELP_MSG)
            exit()
    if len(args) != 1:
        print("No file to parse")
        exit()
    p_file = args[0]
    print("Parsing: " + p_file)
    print("Using: " + s_file)

    with open(s_file, 'r') as myfile:
        data=myfile.read()
    structure = json.loads(data)

    try:
        separator = structure["separator"]
    except KeyError as _:
        print("No separator field found")
        exit()
        
    with open(p_file, 'r') as myfile:
        print("Extracted Data:")
        for line in myfile:
            parameters = extract_as_dict(line, structure, separator)
            if parameters:
                print(parameters)
                # store data in a array to pass to matplotlib
            else:
                print("Failed to parse")

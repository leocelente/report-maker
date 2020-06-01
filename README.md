# Report Maker
## Introduction
Report Maker is a program to generate mission reports based on system logs. 
It is intended tobe applicable to the various kinds of activities performed by the Zenith Aerospace group.

## This Repository
This repository contains the data parsing submodule of the program. 
It is resposible to parse the text log file using the specification 
described by an JSON file containing the name and type of each field.
As well as the field separator token.

It currently uses a feature of the Python specific extension of RegEx, [Named Group Capturing](  https://docs.python.org/3.8/howto/regex.html#non-capturing-and-named-groups).

From the example file you can see that the primary output is a dictionary containg the field names as keys and the values as either a single value or a list as long as the lines of the log file.

## Future
In the future there is the possibility of adding:
- A more generic parsing method
- A user provided data treatment function
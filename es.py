# es.py
# Author: Robert O'Brien-Monk
# reads in a text file and returns how many letter e's it contains
# takes the filename from an argument on the command line
# https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/
# https://stackoverflow.com/questions/7033987/get-a-file-from-cli-input

# to access the commandline
import sys

# FILENAME is the file entered on the commandline
# it's taking the second argument which is the file to search for e in
FILENAME = sys.argv[1]

# count the occurrence of e
with open(FILENAME, 'rt') as f:
    text = f.read()
    count_e= text.count("e")
    print(count_e)
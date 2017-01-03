#!/usr/bin/env python3
# This script reads a file and extracts all of the todo comments

import os
import argparse

"""
Each todo comment will have it's own entry in the todo file. An entry will follow the format
    [line number] text

"""

def read_file(path):
    """
    read_file will read each line of the file at the specified path for all instances of "#TODO". If found the line will be added to a list which
    will then be passed to the write_file function.

    :param path: file path to read from
    """
    file_obj = open(path)
    todo_list = [] 

    todo_list = read_file_looper("#TODO", todo_list, file_obj)
 
    dir_name, file_name = os.path.split(file_obj.name)
    file_obj.close()

    if len(todo_list) != 0:
        write_file(dir_name, todo_list)

def read_multiple_files(lst):
    """
    read_multiple_files will loop through a list of files and call read_file on each one
    
    :param lst: list of file paths
    """

    for path in lst:
        read_file(path)

def read_file_looper(search, lst, source):
    """
    read_file_looper loops through the source and tries to find lines containin search. If found it will add them to the list provided

    Returns lst

    :param search: primary search term to find
    :type search: string
    :type subsearch: string
    :param lst: list to add the matching lines to
    :param source: the source document to loop through
    :type source: any object that can be enumerated
    """
    for num, line in enumerate(source, 1):
        if search in line:
            lst.append(str(num) + " " +  _remove_whitespace(line))

    return lst

def write_file(path, ls):
    """
    write_file will create a new todo file in the target directory if one doesn't already exist and then add the passed list
    to the file
    
    :param path: path to check for file
    :param ls: list of strings to add to the file
    """
    filepath = os.path.join(path, "todo.txt")   
    # check whether file exists
    if os.path.exists(filepath):
        append_write = 'a'
    else:
        append_write = 'w'

    file_obj = open(filepath, append_write)
    for line in ls:
        file_obj.write(line)        

    file_obj.close()

def _remove_whitespace(string):
    """
    Removes white space from a string and then returns it. This function should be called before strings are added to the list.
    """

    return string.lstrip()

def main():
    # get the file path from the args
    parser = argparse.ArgumentParser()
    parser.add_argument("-p","--path", nargs='+', help="File path")
    args = parser.parse_args()

    read_multiple_files(args.path)

if __name__ == '__main__':
    main()

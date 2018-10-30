"""
Implement a recursive function with signature `find(path, filename)` that reports all entries of the file system rooted
at the given path having the given file name. """

import os


def find(path, filename):

    file = os.listdir(path)

    for i in file:

        if os.path.isdir(path + '\\' + i):

            find(path + '\\' + i, filename)

        else:

            if i == filename:
                print(os.path.basename(path))


find("C:\\Users\\Toshiba\\Andric\\", "task1.py")

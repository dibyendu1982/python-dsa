#!/usr/bin/env python3

import threading


def add(x, y):
    return x + y


def main():
    """
    1. Assuming the we know the file path
    2. Open the file in a text stream
    3. Read the file

    Threading
    1. Split it based on number of rows, shard of data, shard1, shard 2, shard3
    2. Start writing to individual file, initiating 1 thread with shard1

    """


def file_open(file_path):
    content_stream = open(file_path, "r")
    content = content_stream.read(content_stream)

    return content


if __name__ == "__main__":
    main()

"""
Write a script that will open and read a .csv file, instantiate a number of threads, 
and write data to a single output file.  
Python is preferred, but please use any language you're comfortable with.
"""


class Human:
    def __init__(self, name, age, health):
        self.name = name
        self.age = age
        self.__health = health

    def __str__(self):
        return f""

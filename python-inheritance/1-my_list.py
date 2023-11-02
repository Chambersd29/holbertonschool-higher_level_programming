#!/usr/bin/python3
"""
MyList class that inherits from the list class.

This class has an addition method to print sorted list.

"""

class MyList(list):

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 15:32:15 2023

@author: Brandon
"""


def encode(sequence):       # Brandon
    return ''.join(list(map(lambda x: str((int(x) + 3) % 10), sequence)))


def menu():
    print("""Menu
-------------
1. Encode
2. Decode
3. Quit
""")


def decode(sequence):
    return "[no decode available]"
    
    



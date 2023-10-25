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
    decoded_pass = ""
    for i in sequence:
        decreased_digit = str(((int(i) - 3) % 10))
        decoded_pass += decreased_digit
    return decoded_pass
    
    

if __name__ == '__main__':
    option = 0
    while option != 3:
        menu()
        option = int(input("Please enter an option: "))
        code = ''
        encoded = ''
        
        if option == 1:
            code = input("Please enter your password to encode: ")
            try:
                test = int(code)
                encoded = encode(code)
                print("Your password has been encoded and stored!\n")
            except:
                print("Error: Only enter integers\n")
        
        if option == 2:
            decoded = decode(encoded)
            if str(decoded) != code:
                print("Error: Decoded value does not match original code")
            output = "The encoded password is {}, and the original password is {}.".format(encoded, decoded)
            print(output)

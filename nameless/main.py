#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
main.py

@author ejnp
"""

def main():
    """Begins an interactive lambda calculus interpreter"""
    print "nameless!\nType 'quit' to exit."
    while True:
        read = raw_input('> ').decode('utf-8')
        if read == 'quit':
            break
        if read != '':
            print read

if __name__ == '__main__':
    main()

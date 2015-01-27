#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
lexer.py

@author ejnp
"""

import string

class Lexer(object):

    def __init__(self, source):
        self.source = source
        self.size = len(source)
        self.position = 0

    def __iter__(self):
        return self

    def next(self):
        self.clear_whitespace()
        if self.position < self.size:
            current = self.source[self.position]
            if Lexer.terminal_char(current):
                self.position += 1
                return current
            else:
                return self.symbol()
        else:
            raise StopIteration()

    def symbol(self):
        contents = ''
        for i in range(self.position, self.size):
            current = self.source[self.position]
            if Lexer.terminal_char(current) or current.isspace():
                break
            contents += current
            self.position += 1
        return contents

    def clear_whitespace(self):
        while self.position < self.size and self.source[self.position].isspace():
            self.position += 1

    @staticmethod
    def terminal_char(char):
        return char in [u'λ', '.', '(', ')']

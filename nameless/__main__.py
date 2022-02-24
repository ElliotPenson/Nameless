#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
main.py

@author ejnp
"""

import sys

from nameless.lexer import Lexer
from nameless.parser import Parser, ParserError
from nameless.visitors import BetaReduction


def interpret(input_string, print_reductions=False, lazy=False):
    """Performs normal order reduction on the given string lambda calculus
    expression. Returns the expression's normal form if it exists.
    """
    lexer = Lexer(input_string)
    try:
        ast = Parser(lexer).parse()
    except ParserError as discrepancy:
        # TODO Add position of error
        print(f'ParseError: {discrepancy}')
        return
    normal_form = False
    while not normal_form:
        reducer = BetaReduction(lazy)
        reduced_ast = reducer.visit(ast)
        normal_form = not reducer.reduced
        if print_reductions:
            print(ast)
        ast = reduced_ast
    return str(ast)


def main():
    """Begins an interactive lambda calculus interpreter"""
    print("nameless!\nType 'quit' to exit.")
    while True:
        read = input('> ').strip()
        if read == 'quit':
            break
        if read != '':
            interpret(read, print_reductions=True, lazy='-l' in sys.argv or '--lazy' in sys.argv)


if __name__ == '__main__':
    main()

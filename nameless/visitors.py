#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
visitors.py

@author ejnp
"""

import ast
import itertools
import lambda_calculus_ast


class FreeVariables(ast.NodeVisitor):
    """Visits each node of a lambda calculus abstract syntax tree and
    determines which variables (if any) are unbound. Ultimately provides a set
    of string variable names.
    """

    def visit_Variable(self, node):
        """FV(x) = {x}"""
        return {node.name}

    def visit_Application(self, node):
        """FV((e1 e2)) = FV(e1) U FV(e2)"""
        return (self.visit(node.left_expression) |
                self.visit(node.right_expression))

    def visit_Abstraction(self, node):
        """FV(λx.e) = FV(e) - {x}"""
        return self.visit(node.body) - self.visit(node.parameter)


class BoundVariables(ast.NodeVisitor):
    """A variable is bound when a surrounding abstraction defines its scope.
    This visitor traverses a lambda calculus abstract syntax tree and provides
    a set of all bound variable names.
    """

    def visit_Variable(self, node):
        """BV(x) = {}"""
        return set()

    def visit_Application(self, node):
        """BV((e1 e2)) = BV(e1) U BV(e2)"""
        return (self.visit(node.left_expression) |
                self.visit(node.right_expression))

    def visit_Abstraction(self, node):
        """BV(λx.e) = BV(e) U {x}"""
        return self.visit(node.body) | {node.parameter.name}


class AlphaConversion(ast.NodeVisitor):
    """Nondestructively substitutes all free occurances of a particular
    variable for an arbitrary expression.

    Attributes:
        to_return (Variable): Instance whose name attribute must match the
            variable that's being replaced
        replacement (Expression): Object inserted into the visited AST
    """

    def __init__(self, to_replace, replacement):
        self.to_replace = to_replace
        self.replacement = replacement

    def visit_Variable(self, node):
        """If the appropriate variable name is found, replace it."""
        if node.name == self.to_replace.name:
            return self.replacement
        else:
            return Variable(node.name)

    def visit_Application(self, node):
        """Returns a new Application after visiting both application
        expressions.
        """
        return Application(self.visit(node.left_expression),
                           self.visit(node.right_expression))

    def visit_Abstraction(self, node):
        """Returns a new Abstraction after visiting both the parameter and
        body. Renames the parameter if the replacement would be incorrectly
        bound by the abstraction.
        """
        if node.parameter.name in FreeVariables().visit(self.replacement):
            # name conflict with bound variable
            unavailable_names = (FreeVariables().visit(node) |
                                 {node.parameter.name})
            new_name = next(s for s in lexicographical()
                            if s not in unavailable_names)
            new_parameter = Variable(new_name)
            converter = AlphaConversion(node.parameter, new_parameter)
            new_body = converter.visit(node.body)
            return Abstraction(new_parameter, self.visit(new_body))
        else:
            return Abstraction(self.visit(node.parameter),
                               self.visit(node.body))


def lexicographical():
    """All alphabetic strings in lexicographical order."""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for size in itertools.count(1):
        for string in itertools.product(alphabet, repeat=size):
            yield ''.join(string)


class Printer(ast.NodeVisitor):
    """Constructs the unicode string representation of a lambda calculus
    abstract syntax tree.
    """

    def visit_Variable(self, node):
        return node.name

    def visit_Application(self, node):
        return u'({} {})'.format(self.visit(node.left_expression),
                                 self.visit(node.right_expression))

    def visit_Abstraction(self, node):
        return u'λ{}.{}'.format(self.visit(node.parameter),
                                self.visit(node.body))

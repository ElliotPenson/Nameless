#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
visitors.py

@author ejnp
"""

import ast
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
        return self.visit(node.expression) - self.visit(node.parameter)

class AlphaConversion(ast.NodeVisitor):
    """Nondestructively substitutes all occurances of a particular variable
    for an arbitrary expression.

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
        body.
        """
        return Abstraction(self.visit(node.parameter),
                           self.visit(node.body))

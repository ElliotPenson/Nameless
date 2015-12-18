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

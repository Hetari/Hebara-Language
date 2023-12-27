import sys
import os
import Tokens


class Interpreter:
    def __init__(self, tree):
        self.tree = tree

    def compute(self, left, op, right):
        left_type = left.type
        right_type = right.type

        left_value = getattr(self, f"read_{left_type}")(left.value)
        right_value = getattr(self, f"read_{right_type}")(right.value)

        if op.value == "+":
            output = left_value + right_value
        elif op.value == "-":
            output = left_value - right_value
        elif op.value == "*":
            output = left_value * right_value
        elif op == "/":
            output = left_value / right_value

        return Tokens.Integer(output) if (left.type == "INTEGER" and right.type == "INTEGER") else Tokens.Float(output)

    def interpret(self, tree=None):
        if tree is None:
            tree = self.tree

        left_node = tree[0]
        if isinstance(left_node, list):
            left_node = self.interpret(left_node)

        right_node = tree[2]
        if isinstance(right_node, list):
            right_node = self.interpret(right_node)

        operator = tree[1]
        return self.compute(left_node, operator, right_node)

    def read_INTEGER(self, value):
        return int(value)

    def read_FLOAT(self, value):
        return float(value)

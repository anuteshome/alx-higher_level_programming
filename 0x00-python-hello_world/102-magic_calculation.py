#!/usr/bin/python3

"""
Python bytecode given:

  3           0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE
"""


def magic_calculation(a, b):
    """
    LOAD_CONST (opcode 0): It loads a constant value onto the stack.
    In this case, it loads the constant 98 onto the stack: [98].

    LOAD_FAST (opcode 3 and 6): It loads a local variable onto the stack.
    The argument specifies the index of the local variable to be loaded.
    Loads the values of the local variables a and b onto the stack: [a, b, 98].

    BINARY_POWER (opcode 9): It performs the exponentiation operation on the
    top two values on the stack. It pops the two values from the stack, raises
    the second value to the power of the first value, and pushes the result
                back onto the stack: [a**b, 98].

    BINARY_ADD (opcode 10): It performs the addition operation on the top two
    values on the stack. It pops the two values from the stack, adds them
    together, and pushes the result back onto the stack: [(a**b) + 98].

    RETURN_VALUE (opcode 11): It returns the value on the top of the stack as
    the result of the function. It pops the value from the stack and returns
    it as the function's output. stack: [(a**b) + 98]
    """
    return a ** b + 98

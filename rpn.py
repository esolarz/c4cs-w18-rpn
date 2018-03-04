#!/usr/bin/python
"""RPN."""

import operator
import logging


logging.basicConfig(filename="rpn.log", level=logging.DEBUG)

operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
        "^": operator.pow,
        "%": operator.mod
}

def calculate(arg):
    """Calculate."""
    stack = list()
    for token in arg.split():
        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2) 
            stack.append(result)
        logging.info(stack)
    if len(stack) is not 1:
        logging.error("YOU FUCKED UP")
        logging.error("YOU FUCKED UP")
        logging.error("YOU FUCKED UP")
        logging.error("YOU FUCKED UP")
        logging.error("YOU FUCKED UP")
        logging.error("YOU FUCKED UP")
        logging.error("YOU FUCKED UP")
        raise TypeError("Too many parameters")
    return stack.pop()


def main():
    """Run main function."""
    while True:
        result = calculate(input('rpn calc> '))
        print("Result: ", result)


if __name__ == "__main__":
    main()

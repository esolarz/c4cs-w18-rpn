#!/usr/bin/python
"""RPN."""


def calculate(arg):
    """Calculate."""
    stack = list()
    for token in arg.split():
        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            arg1 = stack.pop()
            arg2 = stack.pop()
            return arg1 + arg2


def main():
    """Run main function."""
    while True:
        calculate(input('rpn calc> '))


if __name__ == "__main__":
    main()

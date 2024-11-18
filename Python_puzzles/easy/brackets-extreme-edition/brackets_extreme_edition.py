import sys
import math
import re


def has_valid_brackets(expression: str) -> bool:
    """brackets are pushed to a new string,
    then adjacent pairs of brackets of the same kind
    are deleted with re.sub, ideally resulting in an empty string
    if all brackets are matching : returns True  
    """
    brackets = ''
    for c in expression:
        if c in '([{}])':
            brackets += c
    nb_brackets = len(brackets)
    while nb_brackets > 0:
        brackets = re.sub(r'\(\)|\[\]|\{\}', '', brackets)
        if len(brackets) == nb_brackets:
            print(brackets, file=sys.stderr, flush=True)
            break
        nb_brackets = len(brackets)
    return nb_brackets == 0


def main():
    expression = input()
    print(expression, file=sys.stderr, flush=True)
    answer = has_valid_brackets(expression)
    print("true" * answer  + "false" * (not answer))

if __name__== '__main__':
    sys.exit(main())
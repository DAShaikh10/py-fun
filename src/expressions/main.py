from . import Expressions  # import from package (__init__.py)


def main():
    #
    # create 'Expressions' instance using Expressions.numbers[] as default
    expressions = Expressions()
    expressions.print_results()
    #
    # create 2nd 'Expressions' instance using numbers[] passed to constructor
    expressions_2 = Expressions([3, 1, 2, 4, 2, 3])
    expressions_2.print_results()

from .expressions import Expressions


def main():
    #
    e1 = Expressions()  # use default list
    #
    # 2nd object with different list
    e2 = Expressions(
        [1, 4, 6, 67, 6, 8, 23, 8, 34, 49, 67, 6, 8, 23, 37, 67, 6, 34, 19, 67, 6, 8]
    )
    #
    e1.print_results()
    e2.print_results()  # try also other list

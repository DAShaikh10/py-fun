from . import Stream
import random

def main():
    run_choice = 51
    #
    run_choices = {
        1:  "Challenge 1, Data streams in Python, run the first example",
        2:  "Challenge 2, complete map() function",
        3:  "Challenge 3, complete reduce() function",
        31: "Challenge 3.1, example RAYCOX",
        4:  "Challenge 4, complete sort() function",
        41: "Challenge 4.1, len-alpha comperator",
        42: "Challenge 4.2, tuple output: ('Cox', 'Xoc', 3)",
        5:  "Challenge 5, Pipeline for product codes",
        51: "Challenge 5.1, even digit codes"
    }

    names = ['Gonzalez', 'Gill', 'Hardin', 'Richardson', 'Buckner', 'Marquez',
        'Howe', 'Ray', 'Navarro', 'Talley', 'Bernard', 'Gomez', 'Hamilton',
        'Case', 'Petty', 'Lott', 'Casey', 'Hall', 'Pena', 'Witt', 'Joyner',
        'Raymond', 'Crane', 'Hendricks', 'Vance', 'Cleveland', 'Duncan', 'Soto',
        'Brock', 'Graham', 'Nielsen', 'Rutledge', 'Strong', 'Cox']


    if run_choice == 1:
        # Challenge 1, Data streams in Python, run the first example
        result = Stream(names).source() \
            .filter(lambda n : len(n) == 4) \
            .print() \
            .count()
        #
        print(f'found {result} names with 4 letters.')

    if run_choice == 2:
        # Challenge 2, complete map() function
        # to map names to name lengths for the first 8 names
        Stream(names).source() \
            .slice(8) \
            .print() \
            .map(lambda n : len(n)) \
            .print()

    if run_choice == 3:
        # Challenge 3, complete reduce() function
        # to compound all name lengths to a single result
        result = Stream(names).source() \
            .slice(8) \
            .print() \
            .map(lambda n : len(n)) \
            .print() \
            .reduce(lambda x, y : x + y)
        #
        print(f'compound number of letters in names is: {result}.')

    if run_choice == 31:
        # Challenge 3.1, example RAYCOX
        # compound single string of all n-letter names
        n = 3
        result = Stream(names).source() \
            .filter(lambda name : len(name) == n) \
            .print() \
            .map(lambda n : n.upper()) \
            .reduce(lambda x, y : str(x) + str(y), '')
        #
        print(f'compounded {n}-letter names: {result}.')

    if run_choice == 4:
        # Challenge 4, complete sort() function
        Stream(names).source() \
            .slice(8) \
            .print('unsorted: ') \
            .sort() \
            .print('  sorted: ')

    alpha_comperator = lambda n1, n2 : -1 if n1 < n2 else 1
    len_alpha_comperator = lambda n1, n2 : -1 if len(n1) < len(n2) else 1 if len(n1) > len(n2) else alpha_comperator(n1, n2)
    #
    if run_choice == 41:
        # Challenge 4.1, len-alpha comperator
        Stream(names).source() \
            .sort(len_alpha_comperator) \
            .print('sorted: ')

    if run_choice == 42:
        # Challenge 4.2, tuple output: ('Cox', 'Xoc', 3)
        result = Stream(names).source() \
            .sort(len_alpha_comperator) \
            .map(lambda n : (n, n[::-1].capitalize(), len(n))) \
            .filter(lambda n1 : n1[2] % 2 == 1) \
            .print('sorted: ') \
            .count()
        #
        print(f'\\\\\n{result} odd-length names found.')

    # rand_numbers = [random.randint(100000,999999) for i in range(30)]
    # print(f'random numbers: {rand_numbers}')
    #
    if run_choice == 5 or run_choice == 51:
        # Challenge 5, Pipeline for product codes
        # Challenge 5.1, even digit codes
        #
        for i in range(1, 5):
            # Stream of 5 random numbers from integer range, feel free to change
            codes = Stream([random.randint(100000,999999) for j in range(1000)]).source() \
                .filter(lambda n : n % 2 == 0) \
                .cond( run_choice == 51, \
                    # use only numbers with even digits, test by split up number in sequence of digits
                    lambda op : op.filter(lambda n : len(set(map(int, str(n))).intersection([1, 3, 5, 7, 9])) == 0) \
                ) \
                .slice(5) \
                .sort() \
                .map(lambda n : f'X{n}-{sum(list(map(int, str(n)))) % 10}') \
                .get()
            #
            print(f'batch {i}: {codes}')

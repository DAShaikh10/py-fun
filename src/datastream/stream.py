"""
Class of a data stream allowing a sequence of stream operations:
    - slice(i1, i2, i3)    # slice stream in analogy to python slicing
    - filter(filter_func)  # pass only elements for which filter_func yields True
    - map(map_func)        # pass stream where each element is mapped by map_func
    - sort(comperator_func) # pass stream sorted by comperator_func
    - cond(cond, cond_func) # pass stream or apply conditional function
    - print()              # pass unchanged stream and print as side effect

with terminal functions:
    - reduce(reduce_func, start)   # compound stream to single value with reduce_func
    - count()              # return number of elements in terminal stream
    - get()                # return final stream data
"""

"""
Which objects are actually passed downstream?
- We are always passing instances of inner class __Stream_op downstream.

How is method chaining achieved?
- Each method (except terminal functions) returns a new instance of __Stream_op,
  which allows further method calls on that new instance.
"""


class Stream:

    def __init__(self, _data=[]):
        # constructor to initialize instance member variables
        #
        self.__streamSource = self.__new_op(_data)

    class __Stream_op:
        """
        Inner class of objects passed down-stream with chainable functions.

        Results are collected at a stream stage and passed down-stream to the
        next stage where a new object is created and passed further.
        """

        def __init__(self, _new_op_func, _data):
            self.__data = _data
            self.__new = _new_op_func  # __new_op() function injected from outer context

        def slice(self, i1, i2=None, i3=1):
            # function that returns new __Stream_op instance that slices stream
            if i2 == None:
                # flip i1, i2 for single arg, e.g. slice(0, 8), slice(8)
                i2, i1 = i1, 0
            #
            # return new __Stream_op instance with sliced __data
            return self.__new(self.__data[i1:i2:i3])

        def filter(self, filter_func=lambda d: True):
            # return new __Stream_op instance that passes only elements for
            # which filter_func yields True
            #
            return self.__new([d for d in self.__data if filter_func(d)])

        def map(self, map_func=lambda d: d):
            # return new __Stream_op instance that passes elements resulting
            # from map_func of corresponding elements in the inbound stream
            #
            # input data is list of current instance: self.__data
            # mapping means a new list needs to be created with same number of
            # elements, each obtained by applying map_func

            # create new data for next __Stream_op instance from current instance
            # data: self.__data
            new_data = [
                map_func(data) for data in self.__data
            ]  # <-- compute new data here

            # create new __Stream_op instance with new stream data
            new_stream_op_instance = self.__new(new_data)
            return new_stream_op_instance

        def reduce(self, reduce_func=lambda compound, d: compound + d, start=0) -> any:
            # terminal function that returns single value compounded by reduce_func
            #
            compound = start  # <-- compute compound result here
            for data in self.__data:
                compound = reduce_func(compound, data)

            return compound

        def sort(self, comperator_func=lambda n1, n2: -1 if n1 < n2 else 1):
            # return new __Stream_op instance that passes stream sorted by
            # comperator_func
            #
            # create new data for next __Stream_op instance from current instance
            # data: self.__data
            # new_data = sorted(self.__data)  # <-- compute new data here

            new_data = self.__data.copy()

            # Implement bubble sort algorithm.
            total_length = len(new_data)
            for i in range(total_length):
                for j in range(0, total_length - i - 1):
                    if comperator_func(new_data[j], new_data[j + 1]) > 0:
                        new_data[j], new_data[j + 1] = new_data[j + 1], new_data[j]

            # create new __Stream_op instance with new stream data
            new_stream_op_instance = self.__new(new_data)
            return new_stream_op_instance

        def cond(self, cond: bool, conditional):
            # return same __Stream_op instance or apply conditional function
            # on __Stream_op instance if condition yields True
            #
            return conditional(self) if cond else self

        def print(self, prefix=""):
            # return same, unchanged __Stream_op instance and print as side effect
            #
            print(f"{prefix}{self.__data}")
            return self

        def count(self) -> int:
            # terminal function that returns number of elements in terminal stream
            #
            return len(self.__data)

        def get(self) -> any:
            # terminal function that returns final stream __data
            #
            return self.__data

    def source(self):
        # return first __Stream_op instance of stream as source
        #
        return self.__streamSource

    def __new_op(self, *argv):
        # private method to create new __Stream_op instance
        return Stream.__Stream_op(self.__new_op, *argv)

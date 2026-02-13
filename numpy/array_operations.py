import numpy as np

"""
Operations to be performed in this module
1. Sorting of np array
2. Searching (where) in np array
3.Filtering in np array

"""


class OneArray:
    def __init__(self, n):
        self.__nd = np.arange(1, n + 1)

    def sort_array(self):
        print(f"before sorting :{self.__nd}")
        self.__nd = np.sort(self.__nd)
        print(f"after sort :{self.__nd}")

        print(f"before sorting :{self.__nd}")
        self.__nd = np.sort(self.__nd)[::-1]
        print(f"after sort :{self.__nd}")

    def search_equal(self, k):
        x = np.where(self.__nd == k)
        print(f"Searchig for the elemenet {k}")
        try:
            print(x)
            print(self.__nd[x[0]])
        except Exception as e:
            print(f"Error : {e}")

    def filter_even(self):
        print(f"Array which I am going to use {self.__nd}")
        result = self.__nd % 2 == 0
        print(f"This are indexes where element are even :{result}")
        print(self.__nd[result])


def main():
    array = OneArray(9)
    array.sort_array()

    array.search_equal(4)
    array.search_equal(10)
    array.filter_even()


if __name__ == "__main__":
    main()

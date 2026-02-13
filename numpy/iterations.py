import numpy as np


class OneArray:
    def __init__(self, n):
        self.__nd = np.arange(1, n + 1)

    def iterate_loops(self):
        try:
            for x in self.__nd:
                print(x)
            print("-" * self.__nd.shape[0] * 2)
        except Exception as e:
            print(f"Error :{e}")

    def iterate_by_iterator(self):
        try:
            for x in np.nditer(self.__nd):
                print(x)
            print("-" * self.__nd.shape[0] * 2)
        except Exception as e:
            print(f"Error :{e}")


def main():
    array = OneArray(9)
    array.iterate_loops()
    array.iterate_by_iterator()


if __name__ == "__main__":
    main()

import numpy as np


class OneArray:
    def __init__(self, start, end):
        self.__nd = np.arange(start, end + 1)

    def show_universal_functions(self):
        """
        This is link to official documentation you can get all functions/methods from this link :https://numpy.org/doc/2.3/reference/ufuncs.html
        """

        print(f"This is our array :{self.__nd}")

        print(f"Square  of elements {np.square(self.__nd)}")
        print(f"Absoulte of element {np.abs(self.__nd)}")
        print(
            f"minimum element from the array id {np.min(self.__nd)} while \nmax element is {np.max(self.__nd)}"
        )
        print(
            f"Here are all the sign in the arrays wheere -1 =neg,1=pos \n{np.sign(self.__nd)}"
        )


def main():
    np_array = OneArray(-5, 5)
    np_array.show_universal_functions()


if __name__ == "__main__":
    main()

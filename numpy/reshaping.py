import numpy as np


class OneArray:
    def __init__(self, n):
        self.__nd = np.arange(1, n + 1)

    def reshape_2d(self, n, m):
        try:
            print(f"before reshpaing :{self.__nd}")
            self.__nd = self.__nd.reshape(n, m)
            print(self.__nd)
        except Exception as e:
            print(f"error in reshaping 1D in {n} & {m} \n This was error: {e}")

    def faltten_1d(self):
        try:
            print(f"before reshpaing :{self.__nd}")
            self.__nd = self.__nd.reshape(-1)
            print(f"After reshaping {self.__nd}")
        except Exception as e:
            print(f"Error in reshaping :{e}")


def main():
    print("hello")
    array = OneArray(12)
    array.reshape_2d(3, 4)
    array.faltten_1d()


if __name__ == "__main__":
    main()

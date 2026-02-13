import numpy as np


class oneArray:
    def __init__(self, n):
        self.nd = np.arange(0, n + 1)

    def show_various_slicings(self):
        print(f"start from 3 till end on 5th index {self.nd[3:6]}")
        print(f"start from 3 till end {self.nd[3:]}")
        print(f"start from beginign till second last {self.nd[:-1]}")
        print(f"move with steps of 2 elements {self.nd[::2]}")
        print(f"move with steps of 3 elements {self.nd[::3]}")


class multiArray:
    def __init__(self, n=None, m=None):
        self.nd = np.full((n, m), np.arange(1, m + 1))

    def show_various_slicings(self):
        print(f"{self.nd[:, :]}")
        print(f"this will print all rows but from second index\n{self.nd[:, 2:]}")


def main():
    array_one_dimensional = oneArray(7)
    array_one_dimensional.show_various_slicings()

    array_multi_dimensional = multiArray(n=3, m=4)
    array_multi_dimensional.show_various_slicings()


if __name__ == "__main__":
    main()

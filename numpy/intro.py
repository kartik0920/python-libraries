import numpy as np


def main():
    """
    list --> >can contain multiple datatypes  vs np.array contains only single data like array,float etc
    """
    list1 = ["kartik", 1, 3]

    try:
        nd1 = np.array(list1)
        print(nd1)
    except Exception as e:
        print(f"Error : {e}")

    nd2 = np.array([1, 2, 3, 4, 5])
    print(nd2)

    nd3 = np.array([[1, 2, 3], [4, 5, 6]])
    print(nd3)

    # shape return shape of numopy array
    print(f"Size of nd2 is {nd2.shape}")
    print(f"Size of nd3 is {nd3.shape}")

    # arange function is use to fill the array by the range
    nd4 = np.arange(5)
    print(nd4)

    nd5 = np.arange(
        1, 10, 2
    )  # this uses step of 2 and start from 1 and end till 10-1=9
    print(nd5)

    # if all element should be zero we use zeroes function
    nd6 = np.zeros(5)
    print(f"Element with 5 zeroes{nd6}")
    nd7 = np.zeros((3, 5))
    print(f"Element with 3X5 zeroes\n{nd7}")

    nd8 = np.full(10, 1)
    print(f"array with 10 element start from 1 {nd8}")
    nd8 = np.full((2, 2), 10)
    print(f"array with 2X2 element start from 1 \n {nd8}")


if __name__ == "__main__":
    main()

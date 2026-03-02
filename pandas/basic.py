import pandas as pd


def main():
    df = pd.DataFrame(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        columns=["a", "b", "c"],
    )
    print(df)

    print("Basic operations in Pandas")
    print(f"printing first rows :\n {df.head()}")
    print(f"printing last rows :\n {df.tail()}")
    print(f"printing info in dataframe :\n {df.info()}")
    print(f"printing description :\n {df.describe()}")


if __name__ == "__main__":
    main()

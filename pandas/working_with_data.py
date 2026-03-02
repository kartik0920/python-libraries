import pandas as pd
import os

data_path = os.path.join(os.getcwd(), "data")

bios_df = pd.read_csv(os.path.join(data_path, "bios.csv"))
bios_df.head()


bios_df.info()


# filetering the data
bios_df.loc[bios_df["height_cm"] > 123, ["name"]]  # specific columns
bios_df.loc[bios_df["height_cm"] > 123]


bios_df[(bios_df["height_cm"] > 123)]["name"]

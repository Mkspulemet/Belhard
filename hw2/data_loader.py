import pandas as pd
import os

def load_csv(filepath):
    return pd.read_csv(filepath)

path = "dataset/titanic.csv"


df = load_csv(path)
# print(df.head())
import pandas as pd
import matplotlib.pyplot as plt

# load data
data = pd.read_csv("investments_VC.csv", encoding='unicode_escape')

# select only data which name is not null
data = data[~data["name"].isna()]



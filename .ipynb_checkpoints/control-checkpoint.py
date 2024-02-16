import matplotlib
import pandas as pd
from matplotlib import pyplot as plt

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

df = pd.read_csv("input.csv")

print("Contents in csv file:", df)

plt.plot(df['run'], df['time'])  # Ensure correct column names here
plt.show()
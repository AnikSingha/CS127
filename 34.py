#Name: Anik Singha
#Email: anik.singha68@myhunter.cuny.edu
#Date: September 11, 2021
#Use Superbowl_Finals dataset

import pandas as pd
import matplotlib.pyplot as plt

file = input("Enter name of input file: ")
output = input("Enter name of outfile file: ")

df = pd.read_csv(file)

df["Date"] = pd.to_datetime(df["Date"].apply(str))

df["% Points"] = 100 * df["Winner Pts"] / (df["Winner Pts"] + df["Loser Pts"])

df.plot(x = "Date", y = "% Points")

fig = plt.gcf()
fig.savefig(output)

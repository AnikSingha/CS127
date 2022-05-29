#Name: Anik Singha
#Email: anik.singha68@myhunter.cuny.edu
#Date: September 11, 2021
#Manipulate the UFO dataset

import pandas as pd
import matplotlib.pyplot as plt

file = input("Enter name of input file: ")
output = input("Enter name of outfile file: ")

df = pd.read_csv(file)

groupedData = df.groupby("state")
averageStates = groupedData["duration (seconds)"].mean()
topTen = averageStates.sort_values(ascending=False)[:10]
print(topTen.head())

topTen.plot.bar("state","seconds")
plt.xlabel("State")
plt.ylabel("Seconds")

fig = plt.gcf()
fig.savefig(output)

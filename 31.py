#Name: Anik Singha
#Email: anik.singha68@myhunter.cuny.edu
#Date: September 10, 2021
#Modify program from Lab 7

import pandas as pd
import matplotlib.pyplot as plt

file = input("Enter name of input file: ")
output = input("Enter name of outfile file: ")

df = pd.read_csv(file)

df["Fraction Single Adults"] = df["Total Single Adults in Shelter"] / df["Total Individuals in Shelter"]


df.plot(x = "Date of Census", y = "Fraction Single Adults")

fig = plt.gcf()
fig.savefig(output)

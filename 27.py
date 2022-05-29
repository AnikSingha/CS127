#Name: Anik Singha
#Email: anik.singha68@myhunter.cuny.edu
#Date: September 10, 2021
#Modify program from Lab 6


import matplotlib.pyplot as plt
import pandas as pd

pop = pd.read_csv('covidCases.csv')

borough = input("Enter borough name: ")
output = input("Enter output name: ")

pop["Fraction"] = pop[borough]/pop["Case Count"]
pop.plot(x= "Date of Interest", y="Fraction")


print("Min:",pop[borough].min())
print("Max:",pop[borough].max())
print("Mean:",pop[borough].mean())
print("Median:",pop[borough].median())
print("Standard Deviation:",pop[borough].std())

fig = plt.gc()
fig.savefig(output)


#Name: Anik Singha
#Email: anik.singha68@myhunter.cuny.edu
#Date: September 11, 2021
#Write a program that asks the user for a CSV of a Video games Dataset

import pandas as pd

file = input("Enter file name: ")

df = pd.read_csv(file)

print("There are",df["Name"].size,"total games")

print("The number of games in each genre are")

print(df.Genre.value_counts())

print("The top 3 game publishers are")

print(df.Publisher.value_counts()[:3])


#Name: Anik Singha
#Email: anik.singha68@myhunter.cuny.edu
#Date: September 5, 2021
#organize a list of books

books = input("Enter a list of book and theirs authors: ")

books_split = books.split(";")

for x in range(len(books_split)):
    books_split[x] = books_split[x].split("-")

for x in range(len(books_split)):
    books_split[x][1] = books_split[x][1].split()[0][0] + "." + books_split[x][1].split()[1][0]

for x in books_split:
    print(x[0].lstrip() + "by " + x[1] + ".")

print("\nThank you for using my book organizer!")

#Name: Anik Singha
#Email: anik.singha68@myhunter.cuny.edu
#Date: September 5, 2021
#Remove the blue from an image

import matplotlib.pyplot as plt
import numpy as np


image = input("Enter name of the input file: ")
output = input("Enter name of the outfile file: ")

img = plt.imread(image)

img2 = img.copy()
img2[:,:,2] = 0

plt.imsave(output,img2)


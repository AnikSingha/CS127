#Name: Anik Singha
#Email: anik.singha68@myhunter.cuny.edu
#Date: September 17, 2021
#Create an image with khaki and rosy horizontal and vertical stripes


import matplotlib.pyplot as plt
import numpy as np


img = np.ones((10,10,3))

img[5:,:5,:]= 0

plt.imshow(img)
plt.show()
    

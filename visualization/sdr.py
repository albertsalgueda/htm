from matplotlib import pyplot, colors
import numpy as np  
# next, i will set up a 8 x 8 2d matrix, with random bits as elements (0 or 1); 
# for randomization of integers (0 or 1) I use the random module in Python;
# for building each row in the 2d matrix I use list comprehension in Python
import random

data = np.zeros((64,64))
sparcity = 0.02 
active = len(data)**2*sparcity
# add 2% sparcity into the distribution
while active>0:
    print(active)
    i = random.randint(0,len(data)-1)
    j = random.randint(0,len(data)-1)
    data[i][j] = 1
    active -= 1

# display the 2d data matrix
colormap = colors.ListedColormap(["white","red"])
pyplot.figure(figsize=(5,5))
pyplot.imshow(data,cmap=colormap)
pyplot.show()
from matplotlib import colors,pyplot
import numpy as np  
import random

def overlap(sdr1,sdr2):
    """
    Return the overlapping SDR || AND operation between 2 SDR
    """
    active = []
    for i in range(len(sdr1)):
        for j in range(len(sdr2)):
            if sdr1[i][j] == sdr2[i][j]:
                if sdr1[i][j] == 1:
                    active.append((i,j))
    size = len(sdr1)
    overlap = np.zeros((size,size))
    for bit in active:
        overlap[bit[0],bit[1]] = 1
    return overlap

def overlap_score(sdr1,sdr2):
    """
    Compute overlap score given 2 sdr 
    """
    score = 0
    for i in range(len(sdr1)):
        for j in range(len(sdr2)):
            if sdr1[i][j] == sdr2[i][j]:
                if sdr1[i][j] == 1:
                    score += 1
    return score

def viz(sdr):
    """
    Turn SDR into grid-like representation. We accept 2d numpy array
    """
    colormap = colors.ListedColormap(["black","red"])
    pyplot.figure(figsize=(5,5))
    pyplot.imshow(sdr,cmap=colormap)
    pyplot.show()

def vizComplete(sdr):
    """
    Turn SDR into grid-like representation. We accept 2d numpy array
    """
    colormap = colors.ListedColormap(["black","red","yellow"])
    pyplot.figure(figsize=(5,5))
    pyplot.imshow(sdr,cmap=colormap)
    pyplot.show()

def generate_sdr(size,sparsity):
    """
    Randomly generate an SDR of size and sparsity
    """
    data = np.zeros((size,size))
    active = len(data)**2*sparsity
    while active>0:
        i = random.randint(0,len(data)-1)
        j = random.randint(0,len(data)-1)
        data[i][j] = 1
        active -= 1
    return data

from matplotlib import pyplot, colors
import numpy as np  
import math

"""
--- THE RULES ---
1.- Semantically similar data should result with SDRs with overlapping active bits
2.- The same input should produce the same output ( deterministic ) 
3.- Output should have the same dimensionality all the time
4.- The output should have similar sparsity for all inputs and have enough one-bits to handle noise and sub-sampling
"""

class TimeEncoder():
    def __init__(self,size):
        self.size = size
        
    def current_time(self):
        import time
        current_time = time.time()
        return 'TODO'

class WordEncoder():
    def __init__(self):
        self.words = self.word2vec()
    def word2vec(self):
        #read word2vec file and save it as a dictionary
        with open("components/assets/words.txt") as f:
            words = dict()
            for i in range(50000):
                row = next(f).split()
                word = row[0]
                vector = np.array([float(x) for x in row[1:]])
                words[word] = vector
        return words

    def encode(self,word):
        w = self.words[word] # np array of len = 100
        return self.transform(w)
    
    def indexToSDR(self,index):
        step = 0.02
        sdr = np.zeros(100)
        if index > 0:
            #we look at the next 50 positions
            position = int(index//step + 50)
            if position >= 100: 
                position = 98
            sdr[position] = 1
            if (index/step)%1>0.5:
                #next bit
                sdr[position+1] = 1
            else:
                #previous bit
                sdr[position-1] = 1

        elif index < 0:
            index = abs(index)
            #we look at the first 50 positions
            position = int(index//step)
            if position >= 100: 
                position = 98
            sdr[position] = 1
            if (index/step)%1>0.5:
                #next bit
                sdr[position+1] = 1
            else:
                #previous bit
                sdr[position-1] = 1
        elif sdr == 0:
            sdr[50] = 1
            sdr[49] = 1
        return sdr

    def transform(self,word):
        #takes a word vector and turns into a SDR 
        encoded = []
        for index in word:
            raw = self.indexToSDR(index)
            encoded.append(raw)
        return encoded



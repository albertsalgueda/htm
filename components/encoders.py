from matplotlib import pyplot, colors
import numpy as np  
import math
#encoders turn input data into SDR with meaning

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
        with open("assets/words.txt") as f:
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

    @classmethod
    def transform(word):
        #takes a word vector and turns into a SDR
        pass



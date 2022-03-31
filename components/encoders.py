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
        #TODO
        """
        array([ 0.120765,  0.066397,  0.173003, -0.457878,  0.268186, -0.023906,
        0.02199 , -0.301028,  0.124743,  0.175319,  0.291662,  0.195042,
        0.143212,  0.081552, -0.338574,  0.122004,  0.176914,  0.276049,
        0.27135 ,  0.24526 ,  0.326964, -0.331824, -0.198997, -0.376592,
        0.013871, -0.255913,  0.12515 , -0.056746,  0.023215,  0.08028 ,
       -0.284722,  0.259277, -0.344066,  0.487042, -0.35944 , -0.205751,
        0.06215 , -0.132164,  0.354941, -0.280353, -0.330452,  0.162196,
       -0.21753 ,  0.246602,  0.301957,  0.067994,  0.096733,  0.270965,
       -0.215523, -0.280555,  0.213391, -0.323243,  0.335155, -0.093879,
       -0.124442,  0.209568,  0.077779, -0.126617,  0.043174, -0.193544,
       -0.562716,  0.053404, -0.345899, -0.005032,  0.073646,  0.10661 ,
        0.287481,  0.10057 ,  0.023196, -0.177859,  0.052546,  0.051572,
       -0.048939, -0.311406,  0.3192  , -0.234572, -0.328841,  0.246992,
       -0.240015, -0.249935, -0.032197,  0.023549,  0.003931, -0.129455,
        0.307742,  0.135256,  0.029543, -0.266553,  0.285387,  0.108799,
        0.046878,  0.197601,  0.285434,  0.049989,  0.332632, -0.446548,
        0.170719, -0.080808, -0.153681, -0.10546 ])
        """
        pass



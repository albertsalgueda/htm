"""
Use this document to test and experiment with the diferent components of the spatial pooler.py
"""
import time
import numpy as np
from components.sdr import viz,generate_sdr,overlap,overlap_score, vizComplete
from components.pooler import Connection,Neuron,miniColumn,SpatialPool
from components.encoders import TimeEncoder, WordEncoder 

potential_connections = .1 # % of potential connections 
inactive_decrement = .008 # decrement step in permenence for de-learning
active_increment = .1  # increment step for reinforcing connections
permenence_threshold = .95 # the threshold that will determine if the connection is active or not
overlap_threshold = 20 # numer of overlaping connections to consider that a column is active
column_density = 2 # number of neurons per miniColumnn

sparsity = .02
size = 100

def sample():
    input = generate_sdr(size,sparsity)
    pool = SpatialPool(overlap_threshold,potential_connections,column_density,size,permenence_threshold,inactive_decrement,active_increment)
    pool.connect(input)
    pool.overlap(input)

def calculateConnections():
    i = 0
    print('Showing connections for 5 miniColumnns...')
    for c in pool.miniColumns:
        time.sleep(1)
        print(f'Total connections in column {c.id} are: {len(c.totalConnections)}')
        print(f'Active connections in column {c.id} are: {len(c.activeConnections)}')
        print(f'Ratio is {len(c.activeConnections)/len(c.totalConnections)}')
        print('\n')
        i += 1
        if i > 5:
            break

def wordEncoder():
    w = WordEncoder()
    best = w.encode('queen')
    vizComplete(best)
    #check for semantic meaning
    better = w.encode('king')
    vizComplete(better)
    print(overlap_score(best,better)) #if it was a vector, you should compute cos()
    viz(overlap(best,better))

def wordTest():
    w = WordEncoder()
    best = w.encode('queen')
    pool = SpatialPool(overlap_threshold,potential_connections,column_density,size,permenence_threshold,inactive_decrement,active_increment)
    pool.connect(best)
    viz(pool.overlap(best))

wordTest()


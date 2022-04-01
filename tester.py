"""
Use this document to test and experiment with the diferent components of the spatial pooler.py
"""
from sqlite3 import SQLITE_DROP_INDEX, SQLITE_DROP_TABLE
import time
import numpy as np
from components.sdr import viz,generate_sdr,overlap,overlap_score
from components.pooler import Connection,Neuron,miniColumn,SpatialPool
from components.encoders import TimeEncoder, WordEncoder 

potential_connections = .1 # % of potential connections 
inactive_decrement = .008 # decrement step in permenence for de-learning
active_increment = .1  # increment step for reinforcing connections
permenence_threshold = .95 # the threshold that will determine if the connection is active or not
overlap_threshold = 20 # numer of overlaping connections to consider that a column is active
column_density = 2 # number of neurons per miniColumnn

sparsity = .02
size = 32

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
    best = w.encode('bottle')
    #viz(best)
    #check for semantic meaning
    better = w.encode('jar')
    print(overlap_score(best,better))
wordEncoder()
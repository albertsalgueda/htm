"""
Use this document to test and experiment with the diferent components of the spatial pooler.py
"""

from components.sdr import viz,generate_sdr,overlap,overlap_score
from components.pooler import Connection,Neuron,miniColumn,SpatialPool
from components.encoders import TimeEncoder, WordEncoder 

potential_connections = .1 # % of potential connections 
inactive_decrement = .008 # decrement step in permenence for de-learning
active_increment = .1  # increment step for reinforcing connections
permenence_threshold = .1 # the threshold that will determine if the connection is active or not
overlap_threshold = 26 # numer of overlaping connections to consider that a column is active
column_density = 2 # number of neurons per miniColumnn

sparsity = .025
size = 32

input = generate_sdr(size,sparsity)
pool = SpatialPool(overlap_threshold,potential_connections,column_density,size,permenence_threshold,inactive_decrement,active_increment)
pool.connect(input)
pool.overlap(input)
pool.visualize()


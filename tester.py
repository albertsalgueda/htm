"""
Use this document to test and experiment with the diferent components of the spatial pooler.py
"""

from components.sdr import viz,generate_sdr,overlap,overlap_score
from components.pooler import Connection,Neuron,miniColumn,SpatialPool
from components.encoders import TimeEncoder, WordEncoder 

potential_connections = .85 # % of potential connections 
inactive_decrement = .008 # decrement step in permenence for de-learning
active_increment = .1  # increment step for reinforcing connections
permenence_threshold = .8 # the threshold that will determine if the connection is active or not
overlap_threshold = 2 # numer of overlaping connections to consider that a column is active
column_density = 4 # number of neurons per miniColumnn

sparsity = .02
size = 8

input = generate_sdr(size,sparsity)
pool = SpatialPool(overlap_threshold,potential_connections,column_density,size)
pool.connect(input)
pool.overlap(input)
pool.visualize()


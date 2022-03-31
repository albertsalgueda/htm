"""
Use this document to test and experiment with the diferent components of the spatial pooler.py
"""

from components.sdr import viz,generate_sdr,overlap,overlap_score
from components.pooler import Connection,Neuron,Column,SpatialPool
from components.encoders import TimeEncoder, WordEncoder 

potential_connections = .85 # % of potential connections 
active_columns = 40 # number of 
inactive_decrement = .008 # decrement step in permenence for de-learning
active_increment = .1  # increment step for reinforcing connections
permenence_threshold = .5 # the threshold that will determine if the connection is active or not
overlap_threshold = 20 # numer of overlaping connections to consider that a column is active
column_density = 4 # number of neurons per miniColumnn


sparsity = .02 
size = 64

sdr = viz(generate_sdr(size,sparsity))



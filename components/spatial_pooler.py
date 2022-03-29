from matplotlib import pyplot, colors
import numpy as np  

potential_connections = 0.85 # % of potential connections 
active_columns = 40 # number of 
inactive_decrement = .008 # decrement step in permenence for de-learning
acrive_increment = 0.1  # increment step for reinforcing connections
permenence_threshold = 0.5 # the threshold that will determine if the connection is active or not
overlap_threshold = 20 # numer of overlaping connections to consider that a column is active

class Column():
    def __init__(self,id,permenence_threshold,connections):
        self.id = id
        self.permenence_threshold = permenence_threshold
        self.connections = connections
        
    def learn(self):
        pass


class SpatialPool():
    def __init__(self,columns,overlap_threshold,potential_connections):
        self.columns = columns
        self.overlap_threshold = overlap_threshold
        self.potential_connections = potential_connections

    def initialize(self):
        pass

#each connection has a permenence value
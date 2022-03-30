from xml.dom.expatbuilder import parseString
from matplotlib import pyplot, colors
import numpy as np  

potential_connections = 0.85 # % of potential connections 
active_columns = 40 # number of 
inactive_decrement = .008 # decrement step in permenence for de-learning
active_increment = 0.1  # increment step for reinforcing connections
permenence_threshold = 0.5 # the threshold that will determine if the connection is active or not
overlap_threshold = 20 # numer of overlaping connections to consider that a column is active

class Connection():
    def __init__(self,input,column,active_increment,inactive_decrement,permenence_threshold):
        self.input = input  
        self.column = column.id
        self.connection = self.create_connection(input,column)
        self.active_increment = active_increment
        self.inactive_decrement = inactive_decrement
        self.permenence_threshold = permenence_threshold

        self.active = self.isActive()

    def create_connection(self,input,column):
        import random
        synapse = {
                'input':input,
                'column':column, 
                'permenance':random.randint(0,100)/100
                } 
        return synapse

    def isActive(self):
        if self.connection['permenance']>= self.permenence_threshold: 
            return True
        return False

    def increment(self):
        self.connection['permenance'] += self.active_increment

    def decrement(self):
        self.connection['permenance'] -= self.inactive_decrement
    
class Column():
    def __init__(self,id,overlap_threshold):
        self.id = id
        self.overlap_threshold = overlap_threshold
        self.connections = []
        self.active = False
    
    def create_connections(self,input):
        #initialize connections to input source
        pass

    def isActive(self):
        #calculate the number of overlapping connections 
        overlapping = 0 #TODO
        if overlapping >= self.overlap_threshold:
            self.active = True  
        else: self.active = False
        return self.active

class SpatialPool():
    def __init__(self,columns,overlap_threshold,potential_connections):
        self.columns = columns
        self.overlap_threshold = overlap_threshold
        self.potential_connections = potential_connections

    def initialize(self):
        #create the spatial pool
        pass

    def overlap(self):
        #Compute the overlap with the current input for each column
        pass

    def inhibition(self):
        #Compute the winning columns after inhibition
        pass

    def learn(self):
        #Update synapse permanences and internal variables
        pass

    def transform(self):
        #Transform self.columns into a 2d numpy array ( active=1, inactive=0 )
        #returns numpy array
        pass

    def visualize(self):
        #Display Spatial Pooling
        sdr = self.transform()
        colormap = colors.ListedColormap(["white","red"])
        pyplot.figure(figsize=(5,5))
        pyplot.imshow(sdr,cmap=colormap)
        pyplot.show()


col = Column(0,overlap_threshold)
c = Connection((0,0),col,active_increment,inactive_decrement,permenence_threshold)
print(c.connection)
print(c.isActive())
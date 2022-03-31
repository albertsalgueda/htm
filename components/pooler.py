from xml.dom.expatbuilder import parseString
from matplotlib import pyplot, colors
import numpy as np  

"""
Column ( here ) = miniColumn ( brain)
Connection (here ) = synapsis ( brain )

ARQUITECTURA:
Cada columna está hecha por varias neuronas. 
El Spatail pooler está hecho de varias columnas. 
Las neuronas de una columna están connectadas en paralelo a los inputs ( potential connections )
Las neuronas también tienen connexiones entre ellas mismas. 


CONNEXIONES:
Tienen un ratio de permanence: se puede modificar a través del aprendizaje. Si se superal el permenence_threshold, se considera que la connexión está activa. 

"""

class Connection():
    def __init__(self,input,neuron,active_increment,inactive_decrement,permenence_threshold):
        self.input = input  
        self.column = neuron.id
        self.connection = self.create_connection(input,neuron)
        self.active_increment = active_increment
        self.inactive_decrement = inactive_decrement
        self.permenence_threshold = permenence_threshold

        self.active = self.isActive()

    def create_connection(self,input,neuron):
        import random
        synapse = {
                'input':input,
                'neuron':neuron, 
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

class Neuron():
    def __init__(self,id,connections,column):
        self.id = id
        self.connections = [connections]
        self.state = None # Active | Inactive | Predictive
        self.column = column
    
class Column():
    def __init__(self,id,neurons,overlap_threshold):
        self.id = id
        self.overlap_threshold = overlap_threshold
        self.active = False

    def connect(self):
        #connects neurons to input 
        pass

    def overlap(self,input):
        #calculate the number of overlapping connections with input
        overlap = 'TODO' #TODO
        return overlap

    def isActive(self):
        #calculate the number of overlapping connections 
        overlapping = self.overlap() 
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

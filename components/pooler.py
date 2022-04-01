from xml.dom.expatbuilder import parseString
from matplotlib import pyplot, colors
import numpy as np  
import random

"""
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
    def __init__(self,input,neuron,active_increment=.1,inactive_decrement=.008,permenence_threshold=.5):
        self.input = input  
        self.neuron = neuron
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
    def __init__(self,id,miniColumn):
        self.id = id
        self.connections = []
        self.state = None # Active | Inactive | Predictive
        self.miniColumn = miniColumn
    def connect(self):
        #TODO
        #Establish connections to neighboring cells
        pass
    def addConnection(self,connection):
        if connection not in self.connections:
            self.connections.append(connection)
            return True
        else: raise Exception('This connection already exists')
    
class miniColumn():
    def __init__(self,id,column_density,overlap_threshold):
        self.id = id
        self.overlap_threshold = overlap_threshold
        self.active = False
        self.neurons = self.createNeurons(column_density)
    
    def createNeurons(self,column_density):
        #creates neurons
        neurons = []
        id = 0
        for _ in range(column_density):
            neuron = Neuron(id,self.id)
            neurons.append(neuron)
        return neurons

    def connect(self,input_bit):
        #connects neurons to particular input. Ex: (1,1)
        for neuron in self.neurons:
            synapse = Connection(input,neuron.id)
            neuron.addConnection(synapse)

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
    def __init__(self,overlap_threshold,potential_connections,column_density=1,size=64):
        self.overlap_threshold = overlap_threshold
        self.potential_connections = potential_connections
        self.size = size
        self.column_density = column_density
        self.representation = np.zeros((size,size))

        self.miniColumns = self.initialize(size)

    def initialize(self,size):
        #create the spatial pool
        id = 0
        miniColumns = [[0 for i in range(size)] for j in range(size)]
        for i in range(size):
            for j in range(size):
                miniColumns[i][j] = miniColumn(id,self.column_density,self.overlap_threshold)
                id += 1
        return miniColumns
    
    def connect(self,input):
        #creates miniColumn connections to input datapoints
        for c in self.miniColumns:
            for i in range(self.size):
                for j in range(self.size):
                    if random.random() < self.potential_connections: #create connection
                        c.connect(input[i][j])

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
        #Transform self.miniColumns into a 2d numpy array ( active=1, inactive=0 )
        #returns numpy array
        id = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.miniColumns[i][j].active:
                    self.representation[i][j] = 1
                else: self.representation[i][j] = 0
        return self.representation

    def visualize(self):
        #Display Spatial Pooling
        sdr = self.transform()
        colormap = colors.ListedColormap(["white","red"])
        pyplot.figure(figsize=(5,5))
        pyplot.imshow(sdr,cmap=colormap)
        pyplot.show()


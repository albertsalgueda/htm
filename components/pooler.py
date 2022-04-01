from copy import deepcopy
from xml.dom.expatbuilder import parseString
from matplotlib import pyplot, colors
import numpy as np  
import random
from tqdm import tqdm

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
    def __init__(self,input,neuron,active_increment,inactive_decrement,permenence_threshold):
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
                'permenance':random.random()
                } 
        return synapse

    def isActive(self):
        if self.connection['permenance']<self.permenence_threshold: 
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
        else: raise Exception('This connection already exists')
    
class miniColumn():
    def __init__(self,id,column_density,overlap_threshold):
        self.id = id
        self.overlap_threshold = overlap_threshold
        self.active = False
        self.neurons = self.createNeurons(column_density)
        self.activeConnections = []
        self.totalConnections = []
    
    def createNeurons(self,column_density):
        #creates neurons
        neurons = []
        id = 0
        for _ in range(column_density):
            neuron = Neuron(id,self.id)
            neurons.append(neuron)
        return neurons

    def connect(self,input_bit,permenence_threshold,inactive_decrement,active_increment):
        #connects neurons to particular input. Ex: (1,1)
        for neuron in self.neurons:
            synapse = Connection(input_bit,neuron.id,permenence_threshold,inactive_decrement,active_increment)
            neuron.addConnection(synapse)
            self.totalConnections.append(synapse)
            if synapse.active == True: 
                self.activeConnections.append(synapse)
    
    def check(self,input_bit,synapses):
        #returns True if a connection is active with an input bit, else: False
        for s in synapses:
            if s.input == input_bit and s.active:
                return True
        return False

    def overlap(self,input,overlap_threshold):
        #calculate the number of overlapping connections with input
        synapses = self.neurons[0].connections
        overlaps = []
        overlap_score = 0
        for i in range(len(input)):
            for j in range(len(input)):
                if input[i][j]==1 and self.check(input[i][j],synapses):
                    overlaps.append((i,j))
                    overlap_score += 1
        if overlap_score >= overlap_threshold:
            self.active = True

class SpatialPool():
    def __init__(self,overlap_threshold,potential_connections,column_density,size,permenence_threshold,inactive_decrement,active_increment):
        self.overlap_threshold = overlap_threshold
        self.potential_connections = potential_connections
        self.size = size
        self.column_density = column_density
        self.permenence_threshold = permenence_threshold
        self.inactive_decrement = inactive_decrement
        self.active_increment = active_increment

        self.representation = np.zeros((size,size))
        self.miniColumns, self.space = self.initialize(size)

    def initialize(self,size):
        #create the spatial pool
        print('Creating the Space Pool')
        id = 0
        space = [[0 for i in range(size)] for j in range(size)]
        miniColumns = []
        for i in tqdm(range(size)):
            for j in range(size):
                new = miniColumn(id,self.column_density,self.overlap_threshold)
                miniColumns.append(new)
                space[i][j] = new
                id += 1
        return miniColumns, space
    
    def connect(self,input):
        #creates miniColumn connections to input datapoints
        print('Creating synapses...')
        for c in tqdm(self.miniColumns):
            for i in range(self.size):
                for j in range(self.size):
                    if random.random() < self.potential_connections: #create connection
                        c.connect(input[i][j],self.permenence_threshold,self.inactive_decrement,self.active_increment)

    def overlap(self,input):
        #Compute the overlap with the current input for each column
        print('Computing Overlap...')
        for c in tqdm(self.miniColumns):
            #print(c.id,c.active)
            c.overlap(input,self.overlap_threshold)

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
        copy = deepcopy(self.representation)
        for i in range(self.size):
            for j in range(self.size):
                if self.space[i][j].active:
                    copy[i][j] = 1
                else: copy[i][j] = 0
        print(copy)
        return copy

    def visualize(self):
        #Display Spatial Pooling
        sdr = self.transform()
        colormap = colors.ListedColormap(["black","red"])
        pyplot.figure(figsize=(5,5))
        pyplot.imshow(sdr,cmap=colormap)
        pyplot.show()


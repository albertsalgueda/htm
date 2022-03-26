import htm.encoder as encoder
import htm.cortex as cortex
import htm.spatial_pooler as sp
import htm.temporal_memory as tm
import numpy as np
import time
from htm.cortex import initReceptiveFields

# Cortex variables
numInputsX = 25
numInputsY = 25 
numColumnsX = numInputsX
numColumnsY = numInputsY
numNeuronsPerColumn = 32

dimensions = ( numInputsX, numInputsY, numColumnsX, numColumnsY, numNeuronsPerColumn )

# Class initializations
layerIn = encoder.InputLayer( dimensions )
layer3b = cortex.Layer3b( dimensions )
cortex.initReceptiveFields( layerIn, layer3b )

flag = 0

def loop():
	global flag
	#pause = g_main.getPauseFlag()
	pause = False
	if pause == False:
		if flag == 0:
			layerIn.activeateInputs( 0, 4 )
			flag = 1
		else:
			layerIn.activeateInputs( 5, 9 )
			flag = 0

		sp.computeSpatialPooler( layerIn, layer3b )
		tm.computeTemporalMemory( layer3b )

	time.sleep(0.05)
	print( layerIn, layer3b )

print('Total number of columns in the intelligent ststem',len(layer3b.columns))
print('Total number of neurons in the intelligent system',len(layer3b.columns)*len(layer3b.columns[0].neurons))
initReceptiveFields( layerIn, layer3b )
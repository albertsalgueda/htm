# Hierarchical Temporal Memory (HTM)

This project is a Python 3.8+ implementation of [Numenta's HTM](https://numenta.com/) algorithm along with visualization software. The aim of this project is to both understand the implementation of cortical theory while creating a simplified cortical learning system.   

Join the community [here](https://discord.gg/NdFm57nB)

### WARNING !!!

This project is still under development... The software is still not finished. 

# ABOUT THE CODE

## tester.py

No-stake script to play around with the different components. You will also find a list with all the tuning parameters. 

## Components 

### sdr.py

SDR stands for Sparse Distributed Representations. In this document you will find all methods related to SDR ( visualization, creation, operations... )

Learn more about SDR [here](https://numenta.com/assets/pdf/biological-and-machine-intelligence/BaMI-SDR.pdf)

### encoders.py

Classes to convert semantic meaning of input data into SDR Encoders' rules are described within the file.

### pooler.py

Stands for Spatial Pooler. Here you will find the most relevant classes of cortical theory ( the Neuron, the miniColumn, the Connections and why not? The SpatialPooler)

# ABOUT CORTICAL THEORY

You can also find a well compressed summary of cortical theory [here](https://www.oktopus.io/post/htm-zip)

## Cortical Columns

Cortical columns are the basic processing unit of the neocortex. They all have a universal learning algorithm which its understanding and implementation is the main goal of HTM. The brain is made of around 150,000 cortical columns connected in a hierarchical way. 

#### Mini-columns

Mini-columns are  vertical structures through the 6 layers of cortex comprising of about 80-120 neurons.  A neuron's feed forward input, the proximal dendrite, attaches to a receptive field, or particular area of sensory space in which stimulus will trigger the firing of the neuron.  Neurons in a minicolumn have the same receptive field.  Therefore in the HTM algorithm for organizational purposes, each column stores proximal dendrites rather than each neuron in a column.

#### Neurons (Cell in HTM)

The structure of an HTM cell, or neuron, is modeled after pyramidal neurons in the neocortex.  In a real neuron when it is in an active state the axon outputs a short burst of action potentials.  When it is in a predictive state the axon outputs a slower, steady rate of action potentials.  These action potentials are only modeled with a binary "on" or "off" for a cell's state.

#### Dendrite Segments

+ Proximal Dendrite Segment: recieve feedforward input and used to put a neuron in an active state.
+ Apical Dendrite Segments: recieve feedback from higher cortical layers and used to put a neuron in a predictive state.
+ Basal Dendrite Segments: recieve lateral input from nearby neurons and is used to put a neuron in a predictive state.

#### Synapses

+ Potential Synapses: Represents all the axons that pass close enough to a dendrite segment that they could potentially form a synapse.
+ Permanance: A scalar value representing the range of connectedness between an axon and a dendrite.  If the permanance is above a certain threshold, the synapse is connected.

## Spatial Pooling Function

The spatial pooling function operates on a layer of a cortical region.  It uses each column's proximal dendrite input to return active columns that reflect the greatest connectivity with that layer's input.

1. Potential Pool: Each column sees a random subset of the input bits.
2. Overlap Score: How many of column's connected synapses(permanance above threshold) are binary 1.
3. Inhibition: enforce sparcity by selecting active columns from the top overlap scores.
4. Learning: Look at all the active columns and strengthen or weaken connections.
5. Output: active columns

## Temporal Memory Function

The temporal memory function operates at the neuronal level by by using each neuron's basal dendrite input.  Apical dendrites have not been implemented in this version of the algorithm.

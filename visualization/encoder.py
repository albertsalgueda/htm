from matplotlib import pyplot, colors
import numpy as np  

class TimeEncoder():
    def __init__(self,size):
        self.size = size
        
    def current_time(self):
        import time
        current_time = time.time()
        return 'TODO'
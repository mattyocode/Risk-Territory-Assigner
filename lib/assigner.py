import random
import numpy as np

class Assigner:

    # def __init__(self):
    #     self.list = []
    
    def randomise(self, arr):
        return random.sample(arr, len(arr))

    def rand_chunk_territories(self, lst, size):
        gen = (lst[i::size] for i in range(size))
        return list(gen)
import random

class Assigner:

    # def __init__(self):
    #     self.list = []
    
    def randomise(self, arr, number):
        return random.sample(arr, len(arr))

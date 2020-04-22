import random

class Assigner:

    # def __init__(self):
    #     self.list = []
    
    def randomise(self, arr):
        return random.sample(arr, len(arr))

    def assign(self, arr, number): 
        returned_array = []
        splitter = len(arr) / number
        for i in range(0, len(arr), splitter): #the last arg determines how many items in each returned
            returned_array.append(arr[i:i + splitter])
        return returned_array
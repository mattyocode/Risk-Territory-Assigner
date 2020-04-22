import random

class Assigner:
    def randomise(self, arr):
        return random.sample(arr, len(arr))

    def chunk_territories(self, lst, number):
        gen = (lst[i::number] for i in range(number))
        return list(gen)
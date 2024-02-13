from copy import deepcopy

class StatelessQueue:
    def __init__(self, queue):
        self.queue = queue

    def enqueue(self, item):
        cpy = deepcopy(self.queue)
        cpy.append(item)

        return None, StatelessQueue(cpy)

    def dequeue(self):
        cpy = deepcopy(self.queue)

        res = None if cpy == [] else cpy.pop(0)

        return res, StatelessQueue(cpy)
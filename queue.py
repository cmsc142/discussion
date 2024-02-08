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
        # if cpy == []:
        #     res = None
        # else:
        #     res = cpy.pop()

        return res, StatelessQueue(cpy)

start = StatelessQueue([])
_, stack1 = start.enqueue(1)
_, stack2 = stack1.enqueue(2)
res, final = stack2.dequeue()
print(res)
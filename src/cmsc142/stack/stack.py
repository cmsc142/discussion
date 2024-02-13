from copy import deepcopy

class StatelessStack:
    def __init__(self, stack):
        self.stack = stack

    def push(self, item):
        cpy = deepcopy(self.stack)
        cpy.append(item)

        return None, StatelessStack(cpy)

    def pop(self):
        cpy = deepcopy(self.stack)
        res = cpy.pop()

        return res, StatelessStack(cpy)
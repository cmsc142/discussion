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

start = StatelessStack([])
_, stack1 = start.push(1)
_, stack2 = stack1.push(2)
res, stack3 = stack2.pop()

starter = []
starter.append(1)
starter.append(2)
starter.pop()

print(stack1.stack)
print(stack2.stack)
print(stack1.stack)
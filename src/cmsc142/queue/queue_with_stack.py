from random import randint

class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    
    def enqueue(self, x):
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)

        while self.s2:
            self.s1.append(self.s2.pop())

    def dequeue(self):
        return self.s1.pop()
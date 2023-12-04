from collections import deque

f = open("input.txt", 'r').read().split('\n')
f.pop(-1)

class Stacks:
    def __init__(self, number=None, stacks=[]):
        self.id = number
        self.stack = deque(stacks)
    def move_stacks(self, movement):
        for i in range(movement.steps):
            crate = movement.start.stack.pop()
            movement.target.stack.append(crate)
    def append(self, element):
        self.stack.append(element)


class Movement:
    def __init__(self, instruction:str):
            self.steps = instruction[5]
            self.start = instruction[12]
            self.target = instruction[17]

def parse_file(file=f):
    stacks = [Stacks for i in ]
    movements = []
    for i in range(len(file)):
        if file[i].startswith("move"):
            movements.append(Movement(file[i]))
        elif file[i].startswith('['):
            for stack in range(len(file[i])//3):
                stacks[stack].append(file[i][3*stack + 1])
                

def solution_pb1():
    pass

if __name__ == "__main__":
    print(f)
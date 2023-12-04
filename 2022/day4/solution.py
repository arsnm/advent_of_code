f = open("input.txt", 'r').read().split('\n')
f.pop(-1)

class Assignment:
    def __init__(self, assignment):
        assignment = assignment.split('-')
        self.start = int(assignment[0])
        self.stop = int(assignment[1])
        self.length = self.stop - self.start

def solution_pb1(input:list) -> int:
    sol = 0
    for elem in input:
        elem = elem.split(',')
        elf1 = Assignment(elem[0])
        elf2 = Assignment(elem[1])
        if (elf1.start >= elf2.start and elf1.stop <= elf2.stop) or (elf2.start >= elf1.start and elf2.stop <= elf1.stop):
            sol += 1
    return sol
    

def solution_pb2(input:list) -> int:
    sol = 0
    for elem in input:
        elem = elem.split(',')
        elf1 = Assignment(elem[0])
        elf2 = Assignment(elem[1])
        if (elf1.start <= elf2.start <= elf1.stop ) or (elf2.start <= elf1.start <= elf2.stop):
            sol += 1
    return sol
        

if __name__ == "__main__":
    print(f"problem 1 : {solution_pb1(f)}")
    print(f"problem 2 : {solution_pb2(f)}")
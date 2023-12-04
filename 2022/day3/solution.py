f = open("day3/input.txt", "r").read().split("\n")
f.pop(-1)

def prio(character) -> int:
    for i in range(ord('a'), ord('z') + 1):
        if character == chr(i):
            return i + 1 - ord('a')
    for j in range(ord('A'), ord('Z') + 1):
        if character == chr(j):
            return j + 27 - ord('A')
    return 0

class Ruspack:
    def find_doublon(self):
        for i in range(len(self.compart1)):
            for j in range(len(self.compart2)):
                if self.compart1[i] == self.compart2[j]:
                    return self.compart1[i]
        return None
    def find_priority(self):
        if self.doublon != None:
            return prio(self.doublon)
        else:
            return 0
    def __init__(self, content):
        self.compart1 = content[:len(content)//2]
        self.compart2 = content[len(content)//2:]
        self.doublon = Ruspack.find_doublon(self)
        self.priority = Ruspack.find_priority(self)
    def __add__(self, other):
            return self.priority + other.priority

class GroupElves:
    def find_badge(self):
        for i in range(len(self.elf1)):
            for j in range(len(self.elf2)):
                for k in range(len(self.elf3)):
                    if self.elf1[i] == self.elf2[j] and self.elf2[j] == self.elf3[k]:
                        return self.elf1[i]
        return None
    def find_priority(self):
        return prio(self.badge)
    def __init__(self, elf1, elf2, elf3):
        self.elf1 = elf1
        self.elf2 = elf2
        self.elf3 = elf3
        self.badge = GroupElves.find_badge(self)
        self.priority = GroupElves.find_priority(self)

def solution_pb1(input=f) -> int:
    sol = 0
    for ruspack in input:
        sol += Ruspack(ruspack).priority
    return sol

def solution_pb2(input=f) -> int:
    sol = 0
    for i in range(0,len(input),3):
        sol += GroupElves(input[i], input[i+1], input[i+2]).priority
    return sol

if __name__ == "__main__":
    print(f"problem 1 : {solution_pb1(f)}")
    print(f"problem 2 : {solution_pb2(f)}")
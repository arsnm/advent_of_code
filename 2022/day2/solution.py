f = open("day2/input.txt", "r").read().split("\n")
f.pop(-1)

class RPS:
    def calculate_score_pb1(self):
        dict_attack = {'X': 1, 'Y': 2, 'Z': 3}
        score = dict_attack[self.p2]
        if (self.p1 == 'A' and self.p2 == 'X') or (self.p1 == 'B' and self.p2 == 'Y') or (self.p1 == 'C' and self.p2 == 'Z'):
            score += 3
        elif self.p1 == 'A':
            if self.p2 == 'Y':
                score += 6
        elif self.p1 == 'B':
            if self.p2 == 'Z':
                score += 6
        elif self.p1 == 'C':
            if self.p2 == 'X':
                score += 6
        return score
    def calculate_score_pb2(self):
        dict_attack = {'A': 1 , 'B': 2, 'C': 3}
        dict_res = {'X': 0, 'Y': 3, 'Z': 6}
        loop = ['A', 'B', 'C']
        attack_in_loop = loop.index(self.p1)
        score = dict_res[self.p2]
        if self.p2 == 'X':
            score += dict_attack[loop[(attack_in_loop-1)%3]]
        elif self.p2 == 'Y':
            score += dict_attack[loop[attack_in_loop]]
        elif self.p2 == 'Z':
             score += dict_attack[loop[(attack_in_loop+1)%3]]
        return score
    def __init__(self, combat, pb):
            self.p1 = combat[0]
            self.p2 = combat[2]
            if pb == 'pb1':
                self.score = RPS.calculate_score_pb1(self)
            elif pb == 'pb2':
                self.score = RPS.calculate_score_pb2(self)
            else:
                self.score = 0
    def __add__(self, other):
        return self.score + other.score

def solution_pb1(input=f) -> int:
    res = 0
    for combat in input:
        res += RPS(combat, 'pb1').score
    return res  

def solution_pb2(input=f) -> int:
    sol = 0
    for combat in input:
        sol += RPS(combat, 'pb2').score
    return sol  

if __name__ == "__main__":
    print(f"problem 1 : {solution_pb1(f)}")
    print(f"problem 2 : {solution_pb2(f)}")
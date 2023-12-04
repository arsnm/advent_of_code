from heapq import heapify, heappop, heappush

f = open("input.txt", "r")
f = f.read().split('\n')

def solution_pb1(input:list) -> int:
    max_elf = 0
    count_elf = 0
    for i in range(len(input)):
        if input[i] == '':
            max_elf = max(count_elf, max_elf)
            count_elf = 0
        else:
            count_elf += int(input[i])
    return max_elf

def solution_pb2(input:list) -> int:
    heap = []
    heapify(heap)
    count_elf = 0
    for i in range(len(input)):
        if input[i] == '':
            heappush(heap, count_elf)
            count_elf = 0
        else:
            count_elf += int(input[i])
    while len(heap) > 3:
        heappop(heap)
    sol = heappop(heap) + heappop(heap) + heappop(heap)
    return sol

if __name__ == "__main__":
    print(f"problem 1 : {solution_pb1(f)}")
    print(f"problem 2 : {solution_pb2(f)}")
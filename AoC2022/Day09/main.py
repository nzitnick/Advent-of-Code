import time

def p1(input):
    visited = set()
    head = [0.0,0.0]
    tail = [0.0,0.0]
    for x in input:
        x = x.split()
        for y in range(0, int(x[1])):
            prevHead = list(head)
            if x[0] == "R":
                head[0] += 1.0
            elif x[0] == "L":
                head[0] -= 1.0
            elif x[0] == "U":
                head[1] += 1.0
            elif x[0] == "D":
                head[1] -= 1.0
            
            dis = ((head[0] - tail[0]) ** 2 + (head[1] - tail[1]) ** 2) / 2

            if dis >= 1.9:
                tail = list(prevHead)
            visited.add(str(tail))

    print(len(visited))
    
    
def p2(input):
    visited = set()
    rope = []
    for x in range(0, 10):
        rope.append([0, 0])

    for x in input:
        x = x.split()
        for y in range(0, int(x[1])):
            prev = list(rope[0])
            if x[0] == "R":
                rope[0][0] += 1
            elif x[0] == "L":
                rope[0][0] -= 1
            elif x[0] == "U":
                rope[0][1] += 1
            elif x[0] == "D":
                rope[0][1] -= 1
            
            for i in range(1, 10):
                dis = abs(rope[i-1][0] - rope[i][0]) + abs(rope[i-1][1] - rope[i][1])

                if dis == 2:
                    #right
                    if rope[i-1][0] - rope[i][0] > 0 and rope[i-1][1] == rope[i][1]:
                        rope[i][0] += 1
                    #left
                    elif rope[i-1][0] - rope[i][0] < 0 and rope[i-1][1] == rope[i][1]:
                        rope[i][0] -= 1
                    #up
                    elif rope[i-1][1] - rope[i][1] > 0 and rope[i-1][0] == rope[i][0]:
                        rope[i][1] += 1
                    #down
                    elif rope[i-1][1] - rope[i][1] < 0 and rope[i-1][0] == rope[i][0]:
                        rope[i][1] -= 1
                if dis > 2:
                    #up right
                    if rope[i-1][0] - rope[i][0] > 0 and rope[i-1][1] - rope[i][1] > 0:
                        rope[i][0] += 1
                        rope[i][1] +=1
                    #up left
                    elif rope[i-1][0] - rope[i][0] < 0 and rope[i-1][1] - rope[i][1] > 0:
                        rope[i][0] -= 1
                        rope[i][1] +=1
                    #down right
                    elif rope[i-1][0] - rope[i][0] > 0 and rope[i-1][1] - rope[i][1] < 0:
                        rope[i][0] += 1
                        rope[i][1] -=1
                    #down left
                    elif rope[i-1][0] - rope[i][0] < 0 and rope[i-1][1] - rope[i][1] < 0:
                        rope[i][0] -= 1
                        rope[i][1] -=1
            visited.add(str(rope[9]))
    print(len(visited))
    
def main():
    with open('AoC2022/Day09/input.txt') as f:
        input = f.read().splitlines()
            
    p1(input)
    p2(input)
  

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
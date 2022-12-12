import time
import networkx as nx
import matplotlib.pyplot as plt

def p1(g, start, end):
    path = nx.shortest_path(g, source = start, target = end)
    print(len(path) - 1)


    
def p2(g, start, end, input):
    steps = []
    for j, x in enumerate(input):
        for i, y in enumerate(x):
            if y == 'a' or y == 'S':
                start = "[{}, {}]".format(i, j)
                try:
                    path = nx.shortest_path(g, source = start, target = end)
                except:
                    pass
                steps.append(len(path) - 1)
    print(min(steps))
    

def makegraph(g, input):
    for j, x in enumerate(input):
        for i, y in enumerate(x):
            name = "[{}, {}]".format(i, j)
            g.add_node(name, value = y) 
            if y == "S":
                start = "[{}, {}]".format(i, j) 
            if y == "E":
                end = "[{}, {}]".format(i, j) 
                
    for y, nope in enumerate(input):
        for x, value in enumerate(nope):
            name = "[{}, {}]".format(x, y)
            tempval = ord(value)
            if value == 'S':
                tempval = 96
            elif value == 'E':
                tempval = 123
            try:
                up = ord(input[y - 1][x])
            except IndexError:
                pass
            try:
                down = ord(input[y + 1][x])
            except IndexError:
                    pass
            try:
                left = ord(input[y][x - 1])
            except IndexError:
                pass
            try:
                right = ord(input[y][x + 1])
            except IndexError:
                pass
            if up == 69:
                up = 123
            if down == 69:
                down = 123
            if left == 69:
                left = 123
            if right == 69:
                right = 123
            if tempval >= up - 1 and y != 0:
                edgename = "[{}, {}]".format(x , y - 1)
                #print("{} -> {}".format(name, edgename))
                g.add_edge(name, edgename)

            if tempval >= down - 1:
                edgename = "[{}, {}]".format(x, y + 1)
                #print("{} -> {}".format(name, edgename))
                g.add_edge(name, edgename)

            if tempval >= left - 1 and x != 0:
                edgename = "[{}, {}]".format(x - 1, y)
                #print("{} -> {}".format(name, edgename))
                g.add_edge(name, edgename)

            if tempval >= right - 1:
                edgename = "[{}, {}]".format(x + 1, y)
                #print("{} -> {}".format(name, edgename))
                g.add_edge(name, edgename)

    return start, end
    
    
def main():
    with open('AoC2022/Day12/input.txt') as f:
        input = f.read().splitlines()

    g = nx.DiGraph()
    start, end = makegraph(g, input)
        
    p1(g, start, end)
    p2(g, start, end, input)
  

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
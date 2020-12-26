from time import time
import copy

def findRules(rules, i, j,  results, solution, messages):
    while True:

        if j[i[-1]][-1] >= len(rules[i[-1]]):
            if i[-1] == 0:
                results.append(solution)
                return results 
            j[i[-1]][-1] = 0
            if (i[-1] == 8 and i[-2] == 8) or (i[-1] == 11 and i[-2] == 11):
                j[i[-1]].pop()
            i.pop()
            continue
        if rules[i[-1]][j[i[-1]][-1]] == '|':
            j[i[-1]][-1] = 0
            if (i[-1] == 8 and i[-2] == 8) or (i[-1] == 11 and i[-2] == 11):
                j[i[-1]].pop()
            i.pop()
            continue
        if '|' in rules[i[-1]] and j[i[-1]][-1] == 0:
            tempJ = copy.deepcopy(j)
            tempJ[i[-1]][-1] = rules[i[-1]].index('|') + 1
            results = findRules(rules, i.copy(), tempJ, results, solution, messages)
        if rules[i[-1]][j[i[-1]][-1]].isnumeric():
            if (i[-1] == 8 and int(rules[i[-1]][j[i[-1]][-1]]) == 8) or (i[-1] == 11 and int(rules[i[-1]][j[i[-1]][-1]]) == 11):
                i.append(int(rules[i[-1]][j[i[-1]][-1]]))
                j[i[-2]][-1] += 1
                j[i[-2]].append(0)
            else:
                i.append(int(rules[i[-1]][j[i[-1]][-1]]))
                j[i[-2]][-1] += 1

        else:
            solution += rules[i[-1]][0][1]
            temp = []
            for x in messages:
                try:
                    temp.append(x[:len(solution)])
                except IndexError:
                    continue
            if solution not in temp:
                return results
            i.pop()


def problem1(rules, messages):
    i = [0]
    j = [[0]]
    for x in range(len(rules)):
        j.append([0])
    results = []
    solution = '' 

    results = findRules(rules, i, j, results, solution, messages)

    count = 0
    for x in messages:
        #print(x)
        if x in results:
            count += 1
            print(x)
    print(count)


def main():
    startTime = time()
    with open('input.txt') as f:
        ruleBlock, messageBlock = f.read().split('\n\n')
    rules = ruleBlock.splitlines()
    
    rules = [i.split(' ') for i in rules]
    sortedRules = [''] * len(rules)

    for x in rules:
        sortedRules[(int(x[0][:-1]))] = x[1:]
    messages = messageBlock.splitlines()
    problem1(sortedRules, messages)
    print('runtime: {}'.format(time() - startTime))

if __name__ == '__main__':
    main()
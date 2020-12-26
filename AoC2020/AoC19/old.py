
def findRules(rules, i, j,  results, solution):
    print('passed solution: {}'.format(solution))
    tempSolution = ''
    countStep = 0
    while True:
        #print(j)
        #print(i)
        #print(i[-1])
        if j[i[-1]] >= len(rules[0]) and i[-1] == 0:
                #orderdedConcat = [solution[k] for k in order]
                print(solution)
                
                print('solution: {}'.format(solution))
                results.append(solution)
                return results
        if not j[i[-1]] < len(rules[i[-1]]):
                print('end of the line')
                #j[i[-1]] -= 3
                i.pop()
                j[i[-1]] += 1
                continue
        print(rules[i[-1]][j[i[-1]]])
        if  rules[i[-1]][j[i[-1]]] == '|':
            print('going deeper')
            print(solution)
            j[i[-1]] += 1
            results = findRules(rules, i.copy(), j.copy(), results, solution)
            solution += tempSolution
            tempSolution = ''
            i.pop()
            j[i[-1]] += 1
            continue 
        if  not rules[i[-1]][j[i[-1]]].isnumeric():
            print('fukc')
            print(tempSolution)
            if '|' in rules[i[-2]]:
                tempSolution += (rules[i[-1]][0][1])
            else:
                solution += (rules[i[-1]][0][1])
            i.pop()
            #solution[i[-1]] += rules[i[-1]][0][1]
            j[i[-1]] += 1
            continue 
        else:
            i.append(int(rules[i[-1]][j[i[-1]]]))
            countStep += 1


def problem1(rules, messages):
    i = [0]
    j = [0] * len(rules)
    results = []
    order = [0]
    solution = '' 
    print(solution)
    results = findRules(rules, i, j, results, solution)
    print(results)
    print(messages)
    for x in messages:
        if x in results:
            print('nice')
def main():
    with open('input1.txt') as f:
        ruleBlock, messageBlock = f.read().split('\n\n')
    rules = ruleBlock.splitlines()
    rules = [i[3:].split(' ') for i in rules]
    print(rules)
    messages = messageBlock.splitlines()
    problem1(rules, messages)


if __name__ == '__main__':
    main()
def checkRules(value, ranges, error):
    for rule in ranges:
        if int(rule[0]) <= int(value) <= int(rule[1]):
            return False
    error.append(int(value))
    return True

def problem1(rules, tickets):
    error = []
    ranges = []
    goodTickets = []
    for x in rules:
        x = x.split()
        ranges.append(x[-3].split('-'))
        ranges.append(x[-1].split('-'))
    for x in tickets:
        x = x.split(',')
        bad = False
        for y in x:
            bad = checkRules(y, ranges, error)
            if bad:
                break 
        if not bad:
            goodTickets.append(x) 
    print(sum(error)) 
    return goodTickets

def checkRules2(value, rule):
    if int(rule[0]) <= int(value) <= int(rule[1]):
        return True
    return False

def problem2(rules, myTicket, tickets):
    ranges = []
    for x in rules:
        x = x.split()
        ranges.append([x[-3].split('-'), x[-1].split('-')])
    
    order = []
    for ruleNum, rule in enumerate(ranges):
        possible = []
        i = 0
        while i < len(tickets[0]):
            index = 0
            for ticket in tickets:
                if not(checkRules2(ticket[i], rule[0]) or checkRules2(ticket[i], rule[1])):
                   break
                index += 1
                if index == len(tickets):
                    possible.append(i)
            i +=1
        order.append([possible, ruleNum])
    i = 0
    sortOrder = [1] * len(order)
    for x in order:
        sortOrder[len(x[0]) - 1] = x 
    for i, x in enumerate(sortOrder):
        for y in sortOrder[i+1:]:
            y[0].remove(x[0][0])
    total = 1
    myTicket = myTicket.split(',')
    for x in sortOrder:
        if int(x[1]) < 6:
            total *= int(myTicket[int(x[0][0])])
    print(total)


def main():
    with open('input.txt') as f:
        lines = f.read().split('\n\n')
    rules = lines[0].splitlines()
    myTicket = lines[1].splitlines()[1]
    tickets = lines[2].splitlines()[1:]
    goodTickets = problem1(rules, tickets)
    problem2(rules, myTicket, goodTickets)

if __name__ == '__main__':
    main()
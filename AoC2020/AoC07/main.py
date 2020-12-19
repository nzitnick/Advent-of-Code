
def findColor(rules, color, goldRules):
    newColor = []
    for x in rules:
        if color in x:
            y  = x.split()
            containsColor = y[0] + ' ' + y[1]
            if containsColor not in goldRules and containsColor != 'shiny gold':
                goldRules.append(containsColor)
                newColor.append(containsColor)
    goldRules = [findColor(rules, i, goldRules) for i in newColor]
    return goldRules


def countBags(rules, count, total, color):
    for x in rules:
        y = x.split()
        if color == y[0] + ' ' + y[1]:
            striped = x.replace('contain', ',').split(', ')
            for bag in striped[1:]:
                z = bag.split()
                if z[0].isnumeric():
                    bagCount = count * int(z[0])
                    bagColor = z[1] + ' ' + z[2]
                    total += bagCount
                    total = countBags(rules, bagCount, total, bagColor)

    return total


def problemA(rules, color):
    goldRules = []
    findColor(rules, color, goldRules)
    print(len(goldRules))


def problemB(rules):
    print(countBags (rules, 1, 0, 'shiny gold'))


def main():
    with open('input.txt') as f:
        rules = f.read().splitlines()
    problemA(rules, 'shiny gold')
    problemB(rules)


if __name__ == '__main__':
    main()
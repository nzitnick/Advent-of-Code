
def problem1(foods):
    names = set()
    ingredients = {}
    nameCount = {}
    for x in foods:
        x = x.split(' (')

        allergens = x[1].replace('contains ', '').replace(')', '').split(', ')
        name = set(x[0].split())
        names = names.union(name)
        for y in allergens:
            if y not in ingredients:
                ingredients[y] = name
            else:
                ingredients[y] = ingredients[y].intersection(name)
        for y in list(name):
            if y in nameCount:
                nameCount[y] += 1
            else:
                nameCount[y] = 1

    badOnes = set.union(*list(ingredients.values()))


    count = 0
    for x in names.difference(badOnes):
        count += nameCount[x]
    print(count)
    return ingredients


def problem2(ingredients):
    for y in range(len(ingredients)):
        for x in ingredients:
            if len(ingredients[x]) == 1:
                for z in ingredients:
                    if z != x:
                        ingredients[z] = ingredients[z].difference(ingredients[x])

    allergenName = sorted(list(ingredients.keys()))
    stringAllergens = ''
    for x in allergenName:
        stringAllergens += str(list(ingredients[x])[0]) + ','
    print(stringAllergens[:-1])

def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    problem2(problem1(lines))


if __name__ == '__main__':
    main()
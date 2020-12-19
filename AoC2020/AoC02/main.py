

def passwordCheckA(data):
    
    correct = 0
    for x in data:
        count = x['password'].count(x['letter'])
        if (count >= x['lowRange'] and count <= x['highRange']):
            correct += 1
    return correct

def passwordCheckB(data):
    
    correct = 0
    for x in data:
        if ((x['password'][x['lowRange'] - 1] == x['letter']) != (x['password'][x['highRange'] - 1] == x['letter'])):
            correct += 1
    return correct
    


def main():
    data = []
    with open('input.txt') as f:
       inputByLine = f.read().splitlines()
    for x in inputByLine:
        line = x.split()
        passwordInfo = {}
        rangeSplit = line[0].split('-')
        passwordInfo['lowRange'] = int(rangeSplit[0])
        passwordInfo['highRange'] = int(rangeSplit[1])
        passwordInfo['letter'] = line[1][0]
        passwordInfo['password'] = line[2]
        data.append(passwordInfo)

    correctA = passwordCheckA(data)
    print(correctA)

    correctB = passwordCheckB(data)
    print(correctB)

if __name__ == "__main__":
    main()
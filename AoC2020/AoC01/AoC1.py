


def findCoins(inputs):
        for  x in inputs:
            for y in inputs:
                for z in inputs:
                    if x + y + z == 2020:
                        print (x * y * z)
                        return

def betterWay(numbers):
    for x in numbers:
        for y in numbers:
            diff = 2020 - x - y
            if diff in numbers:
                print(x * y * diff)
                return

                
if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.read().splitlines()
    numbers = [int(i) for i in lines]
    findCoins(numbers)
    betterWay(numbers)
    

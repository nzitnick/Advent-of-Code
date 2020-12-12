import math

def problem1(masses):
    print(sum([math.floor(int(i) / 3 - 2) for i in masses]))


def problem2(x):

    mass = int(x)
    fuelMass = 0
    while True:
        mass = math.floor(mass / 3 - 2)
        if mass <= 0:
            break
        fuelMass += mass
    return fuelMass


def main():
    with open('input.txt') as f:
        masses = f.read().splitlines()
    problem1(masses)
    print(sum([problem2(i) for i in masses]))



if __name__ == '__main__':
    main()
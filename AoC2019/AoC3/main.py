def problem1(wires):
    for x in wires:
        wire = x.split(',')
        print(wire)
        allLocations = []
        location = [0,0]
        allLocations.append(location)
        for y in wire:
            if 

def main():
    with open('input.txt') as f:
        wires = f.read().splitlines()
    problem1(wires)

if __name__ == '__main__':
    main()
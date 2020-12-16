from time import time

def problem1(lines):
    position = [0,0]
    angle = 0
    for x in lines:
        if x[0] == 'N' or (x[0] == 'F' and angle == 90):
            position[1] += int(x[1:])
        elif x[0] == 'S' or (x[0] == 'F' and angle == 270):
            position[1] -= int(x[1:])
        elif x[0] == 'E' or (x[0] == 'F' and angle == 0):
            position[0] += int(x[1:])
        elif x[0] == 'W' or (x[0] == 'F' and angle == 180):
            position[0] -= int(x[1:])
        elif x[0] == 'L':
            angle += int(x[1:])
        elif x[0] == 'R':
            angle -= int(x[1:])
        if angle < 0:
            angle += 360
        if angle > 359:
            angle -= 360
    print(abs(position[0]) + abs(position[1]))


def problem2(lines):
    ship = [0,0]
    waypoint = [10,1]
    for x in lines:
        if x[0] == 'N':
            waypoint[1] += int(x[1:])
        elif x[0] == 'S':
            waypoint[1] -= int(x[1:])
        elif x[0] == 'E':
            waypoint[0] += int(x[1:])
        elif x[0] == 'W':
            waypoint[0] -= int(x[1:])

        if x[0] == 'L':
            if x[1:] == '270':
                waypoint = [waypoint[1], -waypoint[0]]
            elif x[1:] == '180':
                waypoint = [-waypoint[0], -waypoint[1]]
            elif x[1:] == '90':
                waypoint = [-waypoint[1], waypoint[0]]
        elif x[0] == 'R':
            if x[1:] == '90':
                waypoint = [waypoint[1], -waypoint[0]]
            elif x[1:] == '180':
                waypoint = [-waypoint[0], -waypoint[1]]
            elif x[1:] == '270':
                waypoint = [-waypoint[1], waypoint[0]]

        elif x[0] == 'F':
            ship[0] += int(x[1:]) * waypoint[0]
            ship[1] += int(x[1:]) * waypoint[1]
    print(abs(ship[0]) + abs(ship[1]))


def main():
    startTime = time()
    with open('input.txt') as f:
        lines = f.read().splitlines()
    #problem1(lines)
    problem2(lines)
    print('run time {}'.format(time() - startTime))

if __name__ == '__main__':
    main()
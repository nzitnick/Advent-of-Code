
def problem1(numbers, preamble):
    previous = []
    i = 0
    while True:
        if i < preamble:
            previous.append(numbers[i])
            i += 1
            continue
        else:
            good = False
            for x in previous:
                for y in previous:
                    if x + y == numbers[i]:
                        previous.pop(0)
                        previous.append(numbers[i])
                        i += 1
                        good = True
                        break
                if good:
                    break
            if not good:
                return(numbers[i])
            

def problem2(numbers, goal):
    i = 0
    while True:
        base = [numbers[i]]
        j = 1
        while True:
            base.append(numbers[i + j])
            if sum(base) == goal:
                print(min(base) + max(base))
                return
            if sum(base) > goal:
                break
            j += 1
        i += 1


def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()
        numbers = [int(i) for i in lines]
    goal = problem1(numbers, 25)
    problem2(numbers, goal)

if __name__ == '__main__':
    main()
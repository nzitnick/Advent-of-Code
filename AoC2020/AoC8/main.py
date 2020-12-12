import copy

def problemA(instructions):
    acc = 0
    i = 0
    while i < len(instructions):
        if instructions[i][0] == 'acc':
            acc += int(instructions[i][1])
        elif instructions[i][0] == 'jmp':
            if int(instructions[i][1]) + i > len(instructions) + 1:
                return acc, 'end'
            i += int(instructions[i][1])
            continue
        elif instructions[i][0] == 'end':
            return acc, 'end'
        instructions[i][0] = 'end'
        i += 1

    return acc , instructions[i - 1][0]

def problemB(instructions):
    i = 0 
    while i < len(instructions):
        testInstructions = copy.deepcopy(instructions)
        if testInstructions[i][0] == 'nop':
            testInstructions[i][0] = 'jmp'
        elif testInstructions[i][0] == 'jmp':
            testInstructions[i][0] = 'nop'  
        else:
            i += 1
            continue
        acc, lastInstruction = problemA(testInstructions)
        if lastInstruction != 'end':
            return acc
        i += 1
    

def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()
    instructions = [lines[i].split() for i in range(len(lines))]
    print(problemA(copy.deepcopy(instructions)))
    print(problemB(instructions))


if __name__ == '__main__':
    main()
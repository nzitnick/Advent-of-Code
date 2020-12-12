
def problemA(instructions):
    acc = 0
    i = 0
    repeat = []
    while i < len(instructions):
        if i not in repeat:
            op, val = instructions[i]
            if op == 'acc':
                acc += int(val)
            elif op == 'jmp':
                if int(val) + i > len(instructions) + 1:
                    return acc
                i += int(val)
                continue
            repeat.append(i)
            i += 1
        else:
            return acc, 'end'

    return acc , instructions[i - 1][0]

def problemB(instructions):
    i = 0 
    while i < len(instructions):
        if instructions[i][0] == 'nop':
            instructions[i][0] = 'jmp'
        elif instructions[i][0] == 'jmp':
            instructions[i][0] = 'nop'  
        else:
            i += 1
            continue
        acc, lastInstruction = problemA(instructions)

        if instructions[i][0] == 'nop':
            instructions[i][0] = 'jmp'
        elif instructions[i][0] == 'jmp':
            instructions[i][0] = 'nop' 

        if lastInstruction != 'end':
            return acc
        i += 1
    

def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()
    instructions = [lines[i].split() for i in range(len(lines))]
    print(problemA(instructions))
    print(problemB(instructions))


if __name__ == '__main__':
    main()
from time import time

def orderOp(equation, i):
    num = ''
    op = ''
    while i < len(equation):
        if equation[i] == ' ':
            i += 1
            continue

        if equation[i].isnumeric():
            if num != '':
                if op == '*':
                    num *= int(equation[i])
                elif op == '+':
                    num += int(equation[i])
            else:
                num = int(equation[i])

        elif equation[i] == '*' or equation[i] == '+':
            op = equation[i]

        elif equation[i] == '(':
            temp, i = orderOp(equation, i + 1)
            if op == '*':    
                num *= temp
            elif op == '+':
                num += temp
            else:
                num = temp

        elif equation[i] == ')':
            return num , i

        i += 1
    return num, i


def problem1(equations):
    total = []
    for equation in equations:
        num = orderOp(equation, 0)
        total.append(num[0])
    print(sum(total))

def problem2(equations):
    total = []
    for equation in equations:
        i = 0 
        while i < len(equation):      
            if equation[i] == '+':
                if equation[i + 1] == '(' or equation[i - 1] == ')':
                    j = i + 2
                    k = i - 1
                    jCount = 1
                    kCount = 1
                    if equation[i + 1] != '(':
                        j = i + 1
                    else:
                        while j < len(equation):
                            if equation[j] == ')':
                                jCount -= 1
                            elif equation[j] == '(':
                                jCount += 1
                            if jCount == 0:                           
                                break
                            j += 1

                    if not(equation[k].isnumeric()):  
                        while k >= 0: 
                            if equation[k-1] == ')':
                                kCount += 1
                            elif equation[k-1] == '(':
                                kCount -= 1
                            if kCount == 0:                           
                                break
                            k -= 1
                    equation = equation[:k] + '(' + equation[k:j+1] + ')' + equation[j+1:]
                elif equation[i + 1].isnumeric():
                    equation = equation[:i-1] + '(' + equation[i-1:i+2] + ')' + equation[i+2:]
                i += 1
            i += 1
        temp = orderOp(equation, 0)
        total.append(temp[0])
    print(sum(total))


def main():
    startTime = time()
    with open('input.txt') as f:
        lines = f.read().splitlines()
        equations = [i.replace(' ', '') for i in lines]
    #problem1(equations)
    problem2(equations)
    print('runtime: {}'.format(time() - startTime))
if __name__ == '__main__':
    main()
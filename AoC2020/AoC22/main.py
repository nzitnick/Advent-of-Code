from time import time

def problem1(player1, player2):
    total = 0
    try:
        while True:
            if player1[0] > player2[0]:
                player1.append(player1.pop(0))
                player1.append(player2.pop(0))
            elif player1[0] < player2[0]:
                player2.append(player2.pop(0))
                player2.append(player1.pop(0))
    except:
        if player2:
            player2.reverse()
            for i, x in enumerate(player2):
                total += (i + 1) * x
        else:
            player1.reverse()
            for i, x in enumerate(player1):
                total += (i + 1) * x
    print(total)


def cardGame(player1, player2):
    total = 0
    oldHands = []
    while True:
        if [player1, player2] in oldHands:      
            return True, total
        oldHands.append([player1.copy(), player2.copy()])

        if player1[0] < len(player1) and player2[0] < len(player2):
            player1Won = cardGame(player1[1:player1[0] + 1], player2[1:player2[0] + 1])
            if player1Won[0]:
                player1.append(player1.pop(0))
                player1.append(player2.pop(0))
            else:
                player2.append(player2.pop(0))
                player2.append(player1.pop(0))
        elif player1[0] > player2[0]:
            player1.append(player1.pop(0))
            player1.append(player2.pop(0))
        elif player1[0] < player2[0]:
            player2.append(player2.pop(0))
            player2.append(player1.pop(0))
        if len(player1) == 0:
            player2.reverse()
            for i, x in enumerate(player2):
                total += (i + 1) * x
            return False, total
        elif len(player2) == 0:
            player1.reverse()
            for i, x in enumerate(player1):
                total += (i + 1) * x
            return True, total

def problem2(player1, player2):
    winningPlayer, total = cardGame(player1, player2)
    if winningPlayer:
        print('player1: {}'.format(total))
    else: 
        print('player2: {}'.format(total))


def main():
    startTime = time()
    with open('input.txt') as f:
        player1, player2 = f.read().split('\n\n')
    player1 = [int(i) for i in player1.split()[2:]]
    player2 = [int(i) for i in player2.split()[2:]]
    #problem1(player1, player2)
    problem2(player1, player2)
    print('runtime: {}'.format(time() - startTime))

if __name__ == '__main__':
    main()
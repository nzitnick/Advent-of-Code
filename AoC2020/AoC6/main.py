
def countA(groups):
    size = []
    for x in groups:
        size.append(len(set(x.replace('\n', ''))))
    print(sum(size))

def countB(groups):
    count = []
    for x in groups:
        y = x.split()
        count.append(len(set.intersection(*[set(i) for i in y])))
    print(sum(count))

def main():
    with open('input.txt') as f:
        groups = f.read().split('\n\n')
    countA(groups)
    countB(groups)

if __name__ == "__main__":
    main()
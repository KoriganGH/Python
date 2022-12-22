def special(x):
    if x > 0 and x % 2 == 0:
        return True


def subsequence(file):
    del file[0]
    ssum = 0
    m = -10000
    flag = False
    for i in file:
        v = int(i)
        if special(v) and flag:
            flag = False
            ssum = 0
            continue
        elif special(v) and not flag:
            flag = 1
        ssum += v
        if ssum > m:
            m = ssum
    print(m)


def main():
    # subsequence(open('11a.txt', 'r').read().split())
    # subsequence(open('11b.txt', 'r').read().split())


if __name__ == '__main__':
    main()

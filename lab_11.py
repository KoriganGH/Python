#6
s = ""
for i in range(int(input())):
    s += input() + '\n'
lst = [word for line in s.split('\n') for word in line.split()]
print(*(sorted(set(lst), key=lambda x: (-lst.count(x), x))), sep='\n')



#8
from collections import defaultdict

N = int(input())
d = defaultdict(list)
for i in range(N):
    lat = [str(j) for j in input().replace(',', '').split()]
    eng = lat[0]
    lat.remove('-')
    for word in lat[1:]:
        d[word].append(eng)
print(len(d))
for i in sorted(d.keys()):
    print(i, '-', *(d[i]))



#12
def rod(dd, aa1, aa2):
    ss = aa1
    while ss in dd:
        ss = dd[ss]
        if ss == aa2:
            return "2"
    ss = aa2
    while ss in dd:
        ss = dd[ss]
        if ss == aa1:
            return "1"
    return "0"


N = int(input())
d = {}
for i in range(N - 1):
    a1, a2 = input().split()
    d[a1] = a2
N = int(input())
s = ""
for i in range(N):
    a1, a2 = input().split()
    s += (rod(d, a1, a2))
print(*[(s[j]) for j in range(len(s))])

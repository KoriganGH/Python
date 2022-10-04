#1(6)

a = int(input())
b = int(input())
l = int(input())
N = int(input())
print(2 * l + (2 * N - 1) * a + 2 * (N - 1) * b)


#2(3)

x = int(input())
y = int(input())
x2 = int(input())
y2 = int(input())
if (x + y + x2 + y2) % 2 == 0:
    print('YES')
else:
    print('NO')


#3(14)

a = float(input())
print(a % 30 * 12)


#4(3)

a = int(input())
b = int(input())
for i in range(a + a % 2 - 1, b-1, -2):
    print(i)


#5(5)

s = 'abcdefabcdefedsafdas'
if s.count('f') == 1:
    for i in range(0, len(s)):
        if s[i] == 'f':
            print(i+1)
if s.count('f') > 1:
    for i in range(0, len(s)):
        if s[i] == 'f':
            print(i+1)
            for j in range(len(s)-1, -1, -1):
                if s[j] == 'f':
                    print(j+1)
                    exit(0)


#6(16)

a = int(input())
temp=0
maxtemp=0
while a!=0:
    b=int(input())
    if a==b:
        temp+=1
        if temp>maxtemp:
            maxtemp=temp
    else:
        temp=0
    a=b
print(maxtemp+1)


#7(3)

s = '123123321456123'
for i in range(0, len(s)-1):
        if s[i] < s[i+1]:
            print(s[i+1])


#8(6)

fib1 = 1
fib2 = 2
n = int(input())
i = 0
while i < n - 4:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1
print(fib2)


#9(5)

n = 6
a = [[0] * n for i in range(n)]
for i in range(n):
    a[i][n - i - 1] = 1
for i in range(n):
    for j in range(n - i, n):
        a[i][j] = 2
for i in a:
    for e in i:
        print(e, end=' ')
    print()

#2
print(len(set(input().split(',')) & set(input().split(','))))



#5
anna, boris = list(map(int, input().split()))
a = set()
for i in range(anna):
    a.add(int(input()))
b = set()
for i in range(boris):
    b.add(int(input()))

print(len(a & b))
print(*sorted(a & b))
print(len(a - b))
print(*sorted(a - b))
print(len(b - a))
print(*sorted(b - a))



#9
students = [{input() for j in range(int(input()))}
            for i in range(int(input()))]
know_all = set.intersection(*students)
know_not_all = set.union(*students)
print(len(know_all), *sorted(know_all), sep='\n')
print(len(know_not_all), *sorted(know_not_all), sep='\n')

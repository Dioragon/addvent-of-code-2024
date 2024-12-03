list1 = []
list2 = []

for _ in range(1000):
    ids = input().split("   ")
    list1.append(int(ids[0]))
    list2.append(int(ids[1]))

list1.sort()
list2.sort()

result = 0
for i in range(1000):
    result += abs(list1[i] - list2[i])

print(result)

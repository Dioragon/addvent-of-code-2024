from collections import Counter

list1 = []
list2 = []

for _ in range(1000):
    ids = input().split("   ")
    id1 = int(ids[0])
    id2 = int(ids[1])
    list1.append(int(ids[0]))
    list2.append(int(ids[1]))

counter = Counter(list2)
result = 0

for i in range(1000):
    result += list1[i] * counter[list1[i]]

print(result)

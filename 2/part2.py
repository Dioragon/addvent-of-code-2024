import sys

def is_strictly_ascending(list):
    for i in range(len(list) - 1):
        if not list[i] < list[i + 1] <= list[i] + 3:
            return False
    
    return True

def is_strictly_descending(list):
    for i in range(len(list) - 1):
        if not list[i] > list[i + 1] >= list[i] - 3:
            return False
    
    return True

counter = 0
for line in sys.stdin:
    report = [int(level) for level in line.split(' ')]
    for levels in [report[:i] + report[i+1:] for i in range(len(report))]:
        if is_strictly_ascending(levels) or is_strictly_descending(levels):
            counter += 1
            break

print(counter)
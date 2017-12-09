import itertools

with open('input') as f:
    jumps = list(map(int, f.readlines()))

for part, offset3 in (('One', 1), ('Two', -1)):
    i, a = 0, list(jumps)
    for iteration in itertools.count(1):
        a[i], i = a[i] + (1 if a[i] < 3 else offset3), i + a[i]
        if i < 0 or i >= len(a):
            print 'Part', part, iteration
            break

banks = (14, 0, 15, 12, 11, 11, 3, 5, 1, 6, 8, 4, 9, 1, 8, 4)
n = len(banks)
seen = {}
for iteration in xrange(1, 100000):
    imax, vmax = max(enumerate(banks), key=lambda x: x[1])
    banks = tuple((i != imax) * b + (vmax / n) + ((i - imax - 1) % n < vmax % n)
             for i, b in enumerate(banks))
    if banks in seen:
        print iteration, iteration - seen[banks]
        break
    seen[banks] = iteration

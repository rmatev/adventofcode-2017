with open('input') as f:
    cmds = [line.replace('inc', '+=').replace('dec', '-=').split()
            for line in f.readlines()]

env = {c[0]: 0 for c in cmds}
global_max = 0
for c in cmds:
    exec(' '.join(c[3:] + [':'] + c[0:3]), {}, env)
    global_max = max(max(env.values()), global_max)
print max(env.values()), global_max

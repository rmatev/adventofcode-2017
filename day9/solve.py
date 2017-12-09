import re

with open('input') as f:
    data = f.read()

data = re.sub(r'!.', '', data)
clean_data = re.sub(r'<[^>]*>', '<>', data)

d = s = 0
for i in clean_data:
     d += i == '{'
     s += d * (i == '}')
     d -= i == '}'

print 'Part One:', s
print 'Part Two:', len(data) - len(clean_data)

a = int(input('A: '))
b = int(input('B: '))
c = int(input('C: '))
d = int(input('D: '))
e = int(input('E: '))
f = int(input('F: '))

x = (c * e) - (b * f) / (a * e) - (b * d)
y = (a * f) - (c * d) / (a * e) - (b * d)

print('X: %.2f'% x)
print('Y: %.2f'% y)

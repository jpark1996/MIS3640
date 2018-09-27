a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
g = 7
h = 8 
i = 9
j = 10
k = 11
l = 12
m = 13
n = 14
o = 15
p = 16
q = 17
r = 18
s = 19
t = 20
u = 21
v = 22
w = 23
x = 24
y = 25
z = 26

def receipts(word):
    count = 0
    for letter in word:
        count += ord(letter)-96
    return count

print('bananas',  '$',receipts('bananas'))
print('rice',     '$',receipts('rice'))
print('paprika',  '$',receipts('paprika'))
print('potato chips',  '$',receipts('potato chips'))
print('-----------------')
print('Total',  '$', receipts('bananas')+receipts('rice')+receipts('paprika')+receipts('potato chips'))

pass 


# modified for question 2


print('{:3} {:14}'.format(
        'bananas', '$52.00'))
print('{:3} {:14}'.format(
        'rice', '$35.00'))
print('{:3} {:14}'.format(
        'paprika', '$72.00'))
print('{:3} {:14}'.format(
        'potato chips', '$78.00'))
print('{:3}'.format('-----------------'))
print('{:3} {:14}'.format(
        'total', '$237.00'))

#modifed for question 3

print('{:3} {:14}'.format(
        'bananas', '$52.00'))
print('{:3} {:14}'.format(
        'rice', '$35.00'))
print('{:3} {:14}'.format(
        'paprika', '$72.00'))
print('{:3}'.format('-----------------'))
print('{:3} {:14}'.format(
        'total', '$237.00'))


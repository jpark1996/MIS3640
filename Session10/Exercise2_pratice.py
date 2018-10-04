'''
Read the documentation of the list methods at https://docs.python.org/3/tutorial/datastructures.html#more-on-lists.
You might want to experiment with some of them to make sure you understand how they work. 
append, extend and sort are particularly useful.
'''
# Stacks
stack = [123,456,789]
stack.append (101112)
stack.append (131415)

print(stack)

stack.pop()

print(stack)

stack.pop()
stack.pop()

print(stack)

# Queues 
from collections import deque
queue = deque(["Jason", "Thomas", "John"])
queue.append ("Jinna")
queue.append ("Hailey")

print(queue)

queue.popleft()

print (queue)

# Squares
squares = []
for x in range (10):
    squares.append(x**3)

print(squares)

'''
or
'''

squares = [x**3 for x in range (10)]

print(squares)

# for ... if clauses
'''
[(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
is equivalent to below 
'''
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append ((x,y))

print(combs)

# Nested list 

matrix = [
    [1,2,3,4],
    [10,11,12,13],
    [101,102,103,104],
    [1000,1001,1002,1003],
]

print(matrix)

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

print(transposed)

# Del

a = [1, 2, 3, 4, 5, 7 ]

del a [1]

print(a)

del a [:] ## delete all##

print(a)

# Tuples and sequences 
t =12345, 54321, 'hello!'

print(t[0]) ##print first one in order##


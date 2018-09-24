# Step 1
a = 4
x = 3 
y = (x + a/x) / 2
print (y)
# Step 2
x = y
y = (x + a/x) / 2
print (y)

# Step 3 ( repeat until gets more accurate)

x = y
y = (x + a/x) / 2
print (y)

x = y
y = (x + a/x) / 2
print (y)

# Step 4 
while True: 
    print (x)
    y = (x + a/x) / 2
    if y == x:
        break 
    x = y

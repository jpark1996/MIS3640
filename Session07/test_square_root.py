def mysqrt (a,x):
    while True: 
        print (x)
        y = (x + a/x) / 2
        if y == x:
            break 
        x = y


import math

def test_square_root(n):
    print ('{:3}{:14}{:14}{:14}'.format ('a','mysqrt(a)','math.sqrt(a)','diff'))
    for a in range (1,n):
        print ('{:3.1f}{:<14.12g}{:<14.12g}{:<14.12g}'.format)

test_square_root (10)

# Another version

for a in range (1,10):
    x = a * 2
    
    print (mysqrt(a,x))

    print (math.sqrt(a))

    diff = ((mysqrt(a,x)) - (math.sqrt(a)))

    print (diff)
   
    


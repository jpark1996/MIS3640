def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)


print (gcd_recursive(10,20))
print (gcd_recursive(169,287))
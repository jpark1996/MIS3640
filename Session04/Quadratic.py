def quadratic(a, b, c):
    d = b**2 - 4*a*c
    if d < 0: 
        return []
    elif d == 0
        return [-b / (2*a)]
    else: 
        root = math.sqrt(d)
        return [(-b + root) / (2*a), (-b - root) / (2*a)]
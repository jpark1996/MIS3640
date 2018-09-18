age = input('please enter your age: ')

if int(age) >= 18: 
    print('adult')
elif int(age): >= 6:
    print('teenager')
else: 
    print('kid')

# Exercise 1

def calculate_bmi(weight, height): 
    bmi = 703 * weight / (height * height)
    if bmi <= 18.5:
        print ("{:.lf}, underweight".format)
    elif 18.5 < bmi <= 25:
        print ("{:.lf}, normal-weighted".format)
    elif 25 < bmi < 30:
        print ("{:.lf}, overweight".format)
    else 30 < bmi: 
        print ("{:.lf}, Obesity".format )
# Exercise 1-2 

def compare(varA, varB):
    if isinstance(varA, str): 
        print('string invovled')
    elif isinstance(varB, str):
        print('string invovled')
    else:
        if varA > varB: 
            print('bigger')
        elif varA == varB:
            print('equal')
        else: 
            print('smaller')
a= 'hello'
b = 3
c = 5
        
compare (a,b)
compare (b,c)



# Recursion 

def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)

Countdown(5) 


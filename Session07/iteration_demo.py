result = 0

# for i in range(10): 
#     print(i+1)
#     result = result + i + 1
#     print('new result after this iteration', result)

# print('The final result:', result)

for i in range(1,11): ##(starting Number, number until this number) 
    result = result + i 
    print('new result after this iteration', result)

print('The final result:', result)

# Calculate the sum of all the odd bumbers from 1 to 1000

result = 0

for i in range(1,1001):
    if i % 2 == 1:
        result = result + i

print('The sum of odd numbers is:', result)

# other version sum of odd number
result = 0

for i in range(1,1001,2):
        result = result + i

print('The sum of odd numbers is:', result)


#factorial 

result = 1 ##since we are doing multiplication 

for i in range (1,11):
    result = result * i 

print ('The factorial of 10 is', result)



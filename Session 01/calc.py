print (42*60 + 42)
print (10 / 1.61)
print (42.7 / (10 / 1.61) ) 
print (( (10 / 1.61) / 42.7)*60)

# Session 2 Exercise 1 Q1 
r = int(input('enter the radius:'))
Question1 = 'The volume of a sphere with radius r is {}.'
import math
print (math.pi)
Answer1 = 4/3 * math.pi * r**3

print(Question1.format(Answer1) )
# Session 2 Ecercise 1 Q2 
Question2 = 'The total wholesale cost for 60 copies is {}.'

Answer2 = 24.95 * 0.6 *60 + 3 + 0.75 * 59

print (Question2.format(Answer2) )

# Session 2 Exercie 1 Q3
Question3 = 'I get home for breakfrest at {} AM.'

import datetime
t = datetime.timedelta (hours = 6, minutes = 52)

easypace = datetime.timedelta (minutes = 16, seconds = 30)

fastpace = datetime.timedelta (minutes = 21, seconds = 36 )

Answer3 = t + easypace + fastpace

print (Question3.format(Answer3) )

# Session 2 Exercise 1 Q4 
Question4 = 'The average of my grade increased {:.1f} %'

Answer4 = 89 - 82  

print (Question4.format(Answer4) )
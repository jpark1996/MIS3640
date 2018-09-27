team ="New England Patriots"
letter = team [1] # starts with 0 (first letter is 0)
print (letter)

# length = team[len(team)-1] = team [-1]/  goes from opposite when it is minus 




prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    if letter == 'O' or letter == 'Q':
        print(letter + 'u' + suffix)
    else:
        print(letter + suffix) 


team = 'New England Patriots'
print(team[0:11]) # samething as team[:11] / Result = New England
print(team[12:20])# samething as [12:] / Result = Patriots
print(team[0:20:2]) # every other letter / samething as [::12]


print (find(team, 'a'))
print (find(team, 'a'))
for i, letter in enumerate(team):
 
#  print (i, letter) 

def count(s, letter):
    c = 0 
    for each in s 
        if each == letter:
            c += 1 
    return c 



print(count(team, 'a')) #should be 2

print (count(team,''))

new_team = team.upper()
print(new_team)





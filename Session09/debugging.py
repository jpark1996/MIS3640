def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    i = 0
    j = len(word2)
    
    while j > 0:
        # print(i, word1[i], j, word2[j])
        print (i,j)
        print (word1[i])
        print (word2[j])

        if word1[i] != word2[j]:
            return False
        i = i + 1
        j = j - 1
    return True 

print (is_reverse('pots', 'stop'))

#another function 

def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)

in_both('babson','college') #print out the common letter in both word

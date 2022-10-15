#Question 11: Calculate the weight of the word banana. ( weight = sum of ascii values of all characters )

name='banana'
z=0
for i in name:
    z+=ord(i)
print(z)

print(sum(map(ord,name)))
#Question 12: Calculate how many times a string occurs in a given file.
 


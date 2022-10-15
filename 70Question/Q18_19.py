#Question 18: Encode a string by adding 10 to all the ascii characters of that string and decode it back

inputstr=input('Enter string to be coded and decoded.')

z=[]
for i in inputstr:
    r=ord(i)+10
    z.append(r)
print('coded string is ',z)

for i in z:
    print(chr(i-10),end="")


#Question 19: Use a function from another file
from func import name

#from func import *
name()

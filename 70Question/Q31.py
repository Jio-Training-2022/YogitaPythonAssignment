#Question 31: Given a user_input as a string, calculate its md5 hash

#MD5 hash function changes or let us say encrypts the input string to
# a new different ..very different thing. 
#older and insecure algorithm that turns data of random lengths into fixed 128-bit hashes.
# All we can guarantee is that it will be 128 bits long, which works out to 32 characters.
# 4bit ==1 character

import hashlib

# initializing string
in_word = input("Enter word to be encrypted: ")
  
# encoding using encode()
# then sending to md5()
result = hashlib.md5(in_word.encode())
print(result)
# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of hash is : ", result.hexdigest())

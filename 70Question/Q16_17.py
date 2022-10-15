# Question 16: Given a number in binary, print its hex , octa and binary representation
inputnum=int(input('Enter binary number'))
instr=str(inputnum)
y=len(instr)-1
sum=0
for i in instr:
    #print(i)
    sum+=int(i)*(2**y)
    y-=1

print('Decimal Number is', sum)





print(bin(sum), "in binary.")
print(oct(sum), "in octal.")
print(hex(sum), "in hexadecimal.")


#Question 17: Solve the fizz buzz problem
for no in range(1,101):
  if no % 3 == 0 and no % 5 == 0:
    print("fizbuzz")
  elif no % 3 ==0:
    print('fizz')
  elif no % 5 ==0:
    print('buzz')
  else:
    print(no)
#calculate the sum of divisor of a number

def divisor(val):
 i = 1
 add = 0
 while i <= val:
  num = val % i
  if num == 0:
   add = add + i
  i = i + 1
 return add
 
print(divisor(8))
#this program will generate the sum of digits of a number

def sum_of_digits(val):
 val = str(val)
 add = 0
 for num in val:
  add = add + int(num)
 return add
 
print(sum_of_digits(23))
#this program will calculate the sum of numbers till the specified value

def sum_of_numbers(val):
 add = 0
 for num in range(val):
  add = add + num
 return add
 
print(sum_of_numbers(10))

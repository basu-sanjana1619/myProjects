#write a program to print three random numbers
import random
l = []
for i in range(0,3):
 num = random.randint(20,50)
 l.append(num)
print(l)
 
 
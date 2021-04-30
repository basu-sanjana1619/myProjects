#write a program to print the day, month, year in the form “Today is 2/2/2016”.
import time
x = time.localtime()
print(time.strftime("%m/%d/%Y - %Z",x))

 
 
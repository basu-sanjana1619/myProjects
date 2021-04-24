#factorial of 4 is 4 *3 *2 *1 = 24. Factorial of 7 is 7 * 6 * 5 * 4 *3 * 2 *1 = 5040

def factorial(num):
 if num == 1:
  return 1
 else:
  return num * factorial(num - 1)

print(factorial(7))


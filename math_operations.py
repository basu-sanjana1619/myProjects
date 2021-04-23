class Math_operation:
 def __init__(self,x,y):
  self.x = x
  self.y = y
 def addition(self):
  z = self.x + self.y
  return "{} + {} = {}".format(self.x,self.y,z)
 def subtraction(self):
  z = self.x - self.y
  return "{} - {} = {}".format(self.x,self.y,z)
 def multiply(self):
  z = self.x * self.y
  return "{} * {} = {}".format(self.x,self.y,z)
 def division(self):
  z = self.x / self.y
  return "{} / {} = {}".format(self.x,self.y,z)
 def get_remainder(self):
  z = self.x % self.y
  return "{} % {} = {}".format(self.x,self.y,z)
 def to_the_power_of(self):
  z = self.x ** self.y
  return "{} ** {} = {}".format(self.x,self.y,z)

m = Math_operation(3,2)
print(m.addition())
print(m.subtraction())
print(m.multiply())
print(m.division())
print(m.get_remainder())
print(m.to_the_power_of())

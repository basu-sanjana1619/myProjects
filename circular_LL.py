class Node():
 def __init__ (self,data):
  self.data = data
  self.next = None
  
class CircularLL():
 def __init__ (self):
  self.head = None
  self.tail = None
 def append(self,value):
  n = Node(value)
  if self.head:
   self.head.next = n
   self.head = n
  else:
   self.head = n
   self.tail = n
  self.head.next = self.tail
  
c = CircularLL()
c.append(10)
c.append(20)
c.append(30)
c.append(40)

first_node = c.tail
print(first_node.data)
node = first_node.next
while node:
 if node.data != first_node.data:
  print(node.data)
 else:
  break
 node = node.next

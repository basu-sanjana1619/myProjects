class Node():
 def __init__ (self,data):
  self.data = data
  self.next = None
  self.prev = None
  
class DoubleLL():
 def __init__ (self):
  self.head = None
  self.tail = None
 def append(self,value):
  n = Node(value)
  if self.head:
   self.head.next = n
   n.prev = self.head
   self.head = n
  else:
   self.head = n
   self.tail = n
 def delete(self,value):
  current_node = self.tail
  prev_node = self.tail
  while current_node:
   if current_node.data == value:
    prev_node.next = current_node.next
    temp = current_node.prev
    current_node.next.prev = temp
   prev_node = current_node
   current_node = current_node.next
    
d = DoubleLL()
d.append(3)
d.append(5)
d.append(7)
d.append(9)
d.append(11)
d.delete(9)
node = d.tail
while node:
 print(node.data)
 node = node.next

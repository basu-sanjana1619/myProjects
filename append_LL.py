class Node():
 def __init__ (self,data):
  self.data = data
  self.next = None
class LinkedList():
 def __init__ (self):
  self.head = None
  self.tail = None
 def append(self,new_value):
  n = Node(new_value)
  if self.head:
   self.head.next = n
   self.head = n
  else:
   self.head = n
   self.tail = n
 def insertBeginning(self,new_value):
  n = Node(new_value)
  if self.tail:
   temp = self.tail
   self.tail = n
   self.tail.next = temp
  else:
   self.tail = n
 def deletion (self,value):
  current_node = self.tail
  previous_node = self.tail
  while current_node:
   if current_node.data == value:
    previous_node.next = current_node.next
   previous_node = current_node
   current_node = current_node.next
      
l = LinkedList()
l.append(2)
l.append(4)
l.append(6)
l.insertBeginning(1)
l.deletion(2)
node = l.tail
while node:
 print(node.data)
 node = node.next


  
 
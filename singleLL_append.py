#In singly linked list there is a head and a tail. 
#Head denotes the starting point and tail denotes the end node which points to null

class Node:
 def __init__(self,data):
  self.data = data
  self.pointer = None
  
class SinglyLL:
 def __init__(self):
  self.head = None
  self.tail = None
 def append(self,val):
  n = Node(val)           #creating an object of class node.
  if self.head:           #if head node is present
   self.head.pointer = n  #then make the head node point to the new node n
   self.head = n          #now make the new node the new head
  else:
  #if head not present, then make the new node head and tail
   self.tail = n   
   self.head = n
   
s = SinglyLL()
s.append(5)                #self.tail points to the first node.
s.append(10)
s.append(15)               #self.head points to the latest node inserted i.e 15. In SLL insertion is done by moving the head.
current = s.tail
count = 0
while current:
 count = count + 1
 print(current.data)
 current = current.pointer
print("size is : " + str(count))

class Node:
 def __init__(self,data):
  self.data = data
  self.pointer = None
  
class SinglyLL:
 def __init__(self):
  self.head = None
  self.tail = None
  
 def append(self,val):
  n = Node(val)           
  if self.head:           
   self.head.pointer = n  
   self.head = n          
  else:
   self.tail = n   
   self.head = n
   
 def delete(self,val):
  current = self.tail         #assign 1st node to current 
  prev = self.tail            #assign 1st node to prev
  while current:              #if current node is present and not None
   if current.data == val:    #check whether that node is equal to the value of the node to be deleted
    if current == self.tail:  #if the node to be deleted is the tail or the first node
     self.tail = current.pointer #make the node which the tail was pointing as the new tail
    else:                        #if the node to be deleted NOT the tail or the first node
     prev.pointer = current.pointer #make the prev node's next point to the current node's next
   prev = current                #update the current node for the while loop. make current node as prev
   current = current.pointer     #make current.next as the new current and start the while loop till current node points to None
   
s = SinglyLL()
s.append(5)                
s.append(10)
s.append(15)               
s.delete(10)
current = s.tail
count = 0
while current:
 count = count + 1
 print(current.data)
 current = current.pointer
print("size is : " + str(count))
#In singly linked list, one node is connected to other and so in. 
#It can only traverse in a single direction

class Node:
 def __init__(self,data):
  self.data = data
  self.pointer = None
  
n1 = Node(4)
n2 = Node(6)
n3 = Node(8)
n1.pointer = n2
n2.pointer = n3
show = ""
while n1 is not None:
 show = show + " " + str(n1.data)
 n1 = n1.pointer
print(show.strip())
 
 
  
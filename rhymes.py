#This program will read through a file and will extracts the email address along with the nursery rhyme name
#from it and will print out
dic = {}
doc = open("rhymes.txt")
for line in doc:
 name = ""
 if line.startswith("Nursery rhymes"):
#splitting the line to get the rhyme name and sender's email. 
  get_index = line.index(",")
#received the rhyme name in format Nursery rhymes: One two three four five.
#capturing only the name and eliminating Nursery rhymes: 
  get_rhyme_name = line[:get_index] 
  get_rhyme_name = get_rhyme_name.split()
  for r in get_rhyme_name:
   if ":" in r:
    index_num = get_rhyme_name.index(r)
    break
  rhyme_name = get_rhyme_name[index_num+1:]
  for rhyme in rhyme_name:
   name = name + " " + rhyme
#received the email address from the line in format Sender: kia@gmail.com.
#capturing only the email and eliminating Sender:    
  get_email = line[get_index+1:]
  get_email = get_email.split()
  for e in get_email:
   if "@" in e:
    email = e
#adding the records in dictionary
  if email not in dic.keys():
   dic[email] = name.strip()
  else:
   dic[email] = dic[email] + ", " + name.strip()
print(dic)

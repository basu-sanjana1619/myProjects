#in python ''' is used to write multiple lines.
unwanted_words = '''["not","see","show","your","you","are","for","in","I","up","then","know",
"not","keep","and","often","nothing","blazing","like","how","could","shut","till","though",
"what","above","when","did","through","dark","lights","light","which","above","to","so","if","never","all","my","upon",
"is","tiny","way","go","so","keep","peep","gone"]'''
count = 1
dic = {}
doc = open("words.txt")
#reading each lines
for line in doc:
#splitting line into list of words
 line = line.split()
#capturing the word and checking each letter is alphabet or not. Eliminating
#the non alphabet parts.
 for word in line:
  word = word.lower()
  w = ""
  for letters in word:
   if letters.isalpha():
    w = w + letters 
#after receiving the updated word without punctuation marks, check 
#whether it is present in unwanted_words list or not. If present skip
  if w not in unwanted_words:
#checking the word is present in dictionary keys or not. If present update
#the count
   if w not in dic.keys():
    dic[w] = count
   else:
    dic[w] = dic[w] + 1
print(dic)
 
def palindrome(word):
 num = 1
 word = word.lower()
 letter = ""
 while num <= len(word):
  letter = letter + word[-num]
  num = num + 1
 reverse_word = letter
 if word == reverse_word:
  return "{} is palindrome".format(word.capitalize())
 else:
  return "{} is not palindrome".format(word.capitalize())

print(palindrome("Noon"))
print(palindrome("HappY"))





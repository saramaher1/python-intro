import re

phrase = 'This is a string and it has some numbers like 5533 and a symbol #hashtag'

x = re.findall("\d", phrase)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
  

x = re.findall("[a-zA-Z]", phrase)

print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
  
x = re.findall("\s", phrase)

print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
  
x = re.findall("\S", phrase)

print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
  
x = re.findall("/[a-zA-Z0-9]+/g", phrase)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
  
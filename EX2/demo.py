# Problem 1
#  Given a list of integers, return True if the sequence of numbers 1, 2, 3
#  appears in the list somewhere.
# For example:
# arrayCheck([1, 1, 2, 3, 1]) → True
# arrayCheck([1, 1, 2, 4, 1]) → False
# arrayCheck([1, 1, 2, 1, 2, 3]) → True
#  ///////////////////////////////////////////////////
#  //////// MY SOlUTION ////////////////////

def array_check(nums):
  for i in range(0,len(nums)-2):
    if nums[i:i+3]==[1,2,3]:
      return True
  return False

array_check([1,2,3,5])

# Problem 2

# Given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo".
 
# For example:
 
# stringBits('Hello') → 'Hlo'
# stringBits('Hi') → 'H'
# stringBits('Heeololeo') → 'Hello'
#  /////////////////////////////////////////////////////////////////
# #  //////// MY SOlUTION ////////////////////
def string_bit(str):
     result=" "
     for i in range(len(str)):
         if i % 2 == 0:
             result = result + str[i]
             
     return result
    
print(string_bit("hello"))
print(string_bit("hi"))
  
# Problem 3

# Given two strings, return True if either of the strings appears at the very end
# of the other string, ignoring upper/lower case differences (in other words, the
# computation should not be "case sensitive").

# Note: s.lower() returns the lowercase version of a string.
# Examples:

# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True
#  //////////////////////////////////////////////////////////////
#  //////// MY SOlUTION ////////////////////

def end_other(a,b):
  a=a.lower()
  b=b.lower()
  return a[-(len(b)):]==b or a==b[-(len(a)):]

print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('abc', 'abXabc') )
# Problem 4
# Given a string, return a string where for every char in the original,
# there are two chars.
 
# doubleChar('The') → 'TThhee'
# doubleChar('AAbb') → 'AAAAbbbb'
# doubleChar('Hi-There') → 'HHii--TThheerree'
 
#  /////////////////////////////////////////////////////////
# #  //////// MY SOlUTION ////////////////////
def doubleChar(str1):
  final_str = ""
  for letter in str1:
    final_str += letter + letter
  return final_str
  
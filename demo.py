# Problem 1:
# Given the string:
# s = 'Lexicon'
 
# Use indexing to print the out the followinf:
# 'L'
# 'n'
# 'Lexi'
# 'con'
# 'on'
# Bonus: Use indexing to reverse the string
# ///////////////////////////////////////////////////////////
# ********** my Solution ***************: 
# s="Lexicon"
# print(s[0])
# print(s[6])
# print(s[:3])
# print(s[4:])
# print(s[6:7])
# print(s[::-1])


# ////////////////////////////////////////////////////////////////////
#Problem 2 :
# Given this nested list:
# my_list = [3,7,[1,4,'hello']]
# Reassign "hello to be "goodbye"
# ///////////////////////////////////////////////////////////
# ********** my Solution ***************: 

# my_list = [3,7,[1,4,'hello']]
# my_list = [3,7,[1,4,'good bye']]
# print(my_list)


# /////////////////////////////////////////////////////////////////////////
# problem 3 :

# Using keys and indexing, grab the 'hello' from the following dictionaries:

# d1 = {'simple_key':'hello'}

# d2 = {'k1':{'k2':'hello'}}

# d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}


# ///////////////////////////////////////////////////////////
# ********** my Solution ***************: 

# print(d1['simple_key'])
# print(d2['k1']['k2'])
# print(d3['k1'][0]['nest_key'][1][0])

# ////////////////////////////////////////////////////////////////////////////


# Problem 4 
# Use a set to find the unique values of the list below:
# my_list = [1,1,1,1,1,2,2,2,2,3,3,3,3]
 
 

# # ///////////////////////////////////////////////////////////
# # ********** my Solution ***************: 
# the_list=set(my_list)
# print(the_list)


# problem 5 
# You are given two variables:
age = 4
name = "Sammy"
 
# Use print formatting to print the following string:
# "Hello my dog's name is Bobby and he is 4 years old"
 
print("hello my dog 's name is Bobby and he is 4 years old")
      
      
      
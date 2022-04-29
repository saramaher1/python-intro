def even_numbers(function):
    def wrap(number):
         return function(number)
    return wrap
@even_numbers
def display(number):
   if(number %2==0):
     print("this is even number")
   else:
     print("this is not even number")  
     
display(5)
display(6)    
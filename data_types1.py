# -*- coding: utf-8 -*-
"""Data types1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sw_5LIC5OFn21Dx2dFXXfHCP43N8Qhpl
"""

a=100  
Str1 ="We are learning Python"  
c = 20.5  
print(type(a))  
print(type(Str1))  
print(type(c))

a = 5  
print("The type of a", type(a))  
  
b = 50.5  
print("The type of b", type(b))  
  
c = 1+3j  
print("The type of c", type(c))  
print(" c is a complex number", isinstance(1+3j,complex))

str = "This sentence has  double quotes"  
print(str)  
s1 = '''''This line has multiline 
string'''  
print(s1)

str1 = 'hello world'         #string str1    
str2 = ' Happy Holidays'      #string str2    
print (str1[0:2])            #printing first two character using slice operator    
print (str1[4])             #printing 4th character of the string    
print (str1*2)               #printing the string twice    
print (str1 + str2)          #printing the concatenation of str1 and str2

list1  = [1, "hi", "Python", 2]    
#Checking type of given list  
print(type(list1))  
  
#Printing the list1  
print (list1)  
  
# List slicing  
print (list1[3:])  
  
# List slicing  
print (list1[0:2])   
  
# List Concatenation using + operator  
print (list1 + list1)  
  
# List repetation using * operator  
print (list1 * 3)

tup  = ("hi", "Python", 2)    
# Checking type of tup  
print (type(tup))    
  
#Printing the tuple  
print (tup)  
  
# Tuple slicing  
print (tup[1:])    
print (tup[0:1])    
  
# Tuple concatenation using + operator  
print (tup + tup)    
  
# Tuple repatation using * operator  
print (tup * 3)     
  
# Adding value to tup. It will throw an error.  
t[2] = "hi"

dict = {1:'Karnataka', 2:'Kerala', 3:'UP', 4:'Punjab'}     
  
# Printing dictionary  
print (dict)  
  
# Accesing value using keys  
print("1st name is "+dict[1])   
print("2nd name is "+ dict[4])    
  
print (dict.keys())    
print (dict.values())

# Python program to check the boolean type  

print(type(True))  
print(type(False))  
print(false)

# Creating Empty set  
set1 = set()  
  
set2 = {'India', 20.4, 100,'OOP'}  
  
#Printing Set value  
print(set2)  
  
# Adding element to the set  
  
set2.add(10)  
print(set2)  
  
#Removing element from the set  
set2.remove(2)  
print(set2)
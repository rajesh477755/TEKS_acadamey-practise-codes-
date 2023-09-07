print("STRING METHODS")
#string methods 
x="Python STrinGS mEthoDS"
#lower case string  method
print(x.lower())
'''This method converts all the characters into lower case '''
#upper case string method
print(x.upper())
''' This method converts all the characters into the upper case'''
#capitalise string  method
print(x.capitalize())
'''This method converts the first character into the upper case'''
#title method
print(x.title())
'''This method converts the first character of all the words into capital letters  '''
#swap case method
print(x.swapcase())
'''This method is used to swap all the upper cases to lower case and vice versa'''
#is an upper string method
print(x.isupper())
'''this particular method is used to check whether all the characters in the string are in upper case or not'''
#is a lower string method
print(x.islower())
''' This particular method is used to check whether 
 all the characters are in lower case or not'''
#is a title string method
print(x.istitle())
'''This particular method is used to check whether all the first characters of each word are capital or not ''' 
x="abd123"
#is a digit string method
print(x.isdigit())
'''This particular method is used to check whether the particular character has digits in it or not '''
#is a numeric string method
print(x.isalpha())
''' This particular method is used to check whether the particular character is having alphabets in it or not '''
#is an alphanumeric
print(x.isalnum())
'''This particular method is used to check whether the given string is having only alphabets and characters or not '''
x="-------Rajesh--------"
# stripe   
print(x.strip('-'))
'''This particular method is used to delete stripes before and after the given string '''
# left stripe
print(x.lstrip('-'))
'''This particular string method is used to delete stripes on the left side of the string '''
# right stripe
print(x.rstrip('-'))
'''This particular string method is used to delete stripes on the right side of the given string '''
x="Rajeshhhh"
#starts with string method
print(x.startswith("R"))
'''this particular method is used to check whether the given string starts with a particular character or not '''
#ends with string method
print(x.endswith("h"))
'''This particular method is used to find out whether the given string ends with a particular character or not'''
# count string method
print(x.count("h"))
'''This particular string method is used to count the of times the given character appears in a specified string  '''
# index string method
print(x.index("a"))
'''This particular string method is used to show the index of a character in a string '''
# replace string method
x=x.replace('R','P')
print(x)
'''This particular string method is used to replace a character in a string  '''


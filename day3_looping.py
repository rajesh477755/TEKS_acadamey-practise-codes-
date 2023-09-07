#conditional statements 
x=int(input("Please enter ur age"))
current_year=2022
age=current_year-x
#if else statement 
''' this is a conditional statement which prints one set of statement if the given condition is true else it will print another set of staments '''
if(age>18):
  print(" You can vote")
else:
  print("you can't vote")
#nested if else statement
'''this is a conditional statement that is execute one loop if the given condition is true else it will execute another loop'''
if(age<18):
  print(" You can't vote")
  if(16<age<18):
    print(" You can apply for a learning license")
  else:
    print("you can't apply for a license")
else:
  print("You can vote \n you can apply for a  license ")
#elif loop statement
'''this is a conditional statement that checks set of conditions and prints set of statement that if a particular condition is true '''
if(age<=21):
  print(" you are eligible to vote and dive and can marry ")
elif(age<=18):
  print("you are eligible to vote and drive but can't marry")
elif(age<=16):
  print("you are not eligible to vote and marry but u can drive vehicles below 110cc")
else:
  print("you are not eligible to vote or dive or marry ")
#looping statements 
#while loop 
'''this is a looping statement the will run the code again and again untill the condition is true if the condition is true then it will execute that code '''
n=int(input("enter a number"))
i=1
x=1
while(i<=n):
  x=x*i
  i=i+1
print(x)
#for loop 
'''this is a looping statement that will execute the code and prints the statements untill the condition is false '''
for i in range (10):
  print(i)
'''in this code the for loop prints the statement untill i value untill it is in specified range '''
num=int(input())
num_str=str(abs(num))
rev=" "
for c in num_str:
  rev=c+rev
if (num<=0):
  print("-"+rev)
else:
  print(rev)
'''in this looping statement the for loop will '''
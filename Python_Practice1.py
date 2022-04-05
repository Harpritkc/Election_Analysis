print("Hello World!")
temperature = int(input("What is the temperature outside?"))
if temperature >80:
    print("Turn on the AC.")
else:
    print("Open the windows")

 #Determine the grade
  
print("WHAT IS THE SCORE")
score = int(input("What is the test score"))
if score >= 90:
    print('your grade is an A.')
elif score >=80:
    print('your grade is a B')
elif score >=70:
    print('your grade is C.')
    

elif score>=60:
    print('your grade is a D.')
else:
    print('your grade is an F.')
#
x =0
while x<=5:
    print(x)
    x=x+1
    
numbers =[0,1,2,3,4]
for num in numbers:
    print(num)
    
# Import the datetime class from the dateti,e module.
import datetime 
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the presnt time.
print("The time right now is ",now)

# Import the datetime class from the dateti,e module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the presnt time.
print("The time right now is ",now)
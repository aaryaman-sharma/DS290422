# Nested if - one if inside another if 

# experience with ages

age  = int(input("Enter your age : "))
experience = int(input("Enter your Experience : "))

if age >= 18:
    if age >= 60:
        print("sorry buddy! You are too old  to work in our organisation")
    else:
        print("You are eligible to work in our organisation")
else:
    print("You are still a bachhu!")


# statement with experience

age  = int(input("Enter your age : "))
experience = int(input("Enter your Experience : "))

if age >= 18:
    if experience >= 2:
        print("You are eligible to work in our organisation")
    else:
        print("You still got to  learn alot. Better luck next time : ")
else:
    print("You are still a bachhu!")


#  ------> Assignment --------->

#   take a input from the user and check whether it is positive value or negative
#   take a input from the user and check whether that value is divisible by 5
#   take a input from the user and check whether that value is divianfsible by 2 and 5
#   take 3 value from the user and find greatest amongst all
#    take marks  for english and science maths and find the total value , percentage , and grade on beses on it
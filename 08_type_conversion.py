# type conversion 
# x = 10 
# y = 12.22
# z = "walid"

# 01_implacit type conversion 

# x=x*y # when we multiply float number to integer it become float. 
# print(type(x)) # basically x is an integer but it multiply with float so x become float.

# x=x+y # so ther is also come float number we can check it .

# 02_ explicit type conversion
# age = input ("what is your age ?  ")
# print(age)
# print(type(age)) # in this line it will show  the type of age is string. 
# and age is not string . so we convert it into integer . how so let see.

# age=int(age)
# print(type(age)) : we can convert it this way and we can convert it on the following way

# print(type(int(age)))

# and the other thing is that integer can not convert the float nummber for example:


age = input ("what is your name ?  ") # if we give float number as input there will show  an error
print( type(int(age))) # if we use float  istead of int and then give float  number so it will be correct
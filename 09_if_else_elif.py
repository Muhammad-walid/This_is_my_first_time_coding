
# if , else , elif , statements.

requir_age_at_school  = 5
student_name =input("what is the  name of student ?  ")
print("the name of this student is " , student_name)
student_age  = input("what is the age of this student ? " )
student_age=int(student_age)
if requir_age_at_school==student_age:
    print(student_name ,  "can join the school ")
elif student_age > requir_age_at_school:
    print(student_name , "should join the higher secondry school")
elif student_age <=3:
    print(student_name , "is still child")
else:
    print(student_name  , "can not join the school")
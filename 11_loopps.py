# two types of loops 
# for loops and while loops.

# # while loop:
# x=0
# while (x<10):
#     print(x)
#     x=x+1
    
# # for loops:
# for x in range(5,10):
#     print(x)

# make an array:
days = ["mon" , "tue" , "wed" , "thu" , "fri" , "sat" , "sun"] 
for d in days:
    # if (d=="fri"):break # stop before friday
    if (d=="fri"):continue # skip friday 
    print(d)
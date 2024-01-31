# if number devisible by 3 - print fizz
# if number devisible by 5 - print buz
# if number devisible by 15 - print fizzbuzz
# 1-1
# 2-2
# 3-fizz
# 4-2
# 5-buzz
# 6-fizz
# ........
# 15-fizzbuzz


# fizz buzz simple mthod
# def fizz_buzz(v):
#     if v%3==0 and v%5==0:
#         print("FIZZBUZZ  :",v) 
#     elif v%3==0:
#         print('FIZZ  :',v)
#     elif v%5==0:
#         print("BUZZ  :",v)
#     else :
#         print("this is :", v)

#     tryagain()
# def tryagain():
#     value=int(input("give me integer number =>   "))
#     fizz_buzz(value)
# tryagain()

# # fizz buzz with the help of for loop mthod
def fizz_buzz(v):
    for i in range(1,v+1):
        if i%3==0 and i%5==0:
            print("FIZZBUZZ  :",i) 
        elif i%3==0:
            print('FIZZ  :',i)
        elif i%5==0:
            print("BUZZ  :",i)
        else :
            print("this is :", i)
    tryagain()
def tryagain():
    value=int(input("give me integer number =>   "))
    fizz_buzz(value)
tryagain()

# fizz buzz with the help of dictionary mthod
# def fizz_buzz(n):
#     d={
#         3:"FIZZ",
#         5:"BUZZ"
#     }
#     for i in range (1,n+1):
#         result=""
#         for k,v in d.items():
#             if i%k==0:
#                 result+=v
#         if not result:
#             result=i
#         print(result)
#     tryagain()
# def tryagain():
#     value=int(input("give me integer number =>   "))
#     fizz_buzz(value)
# tryagain()
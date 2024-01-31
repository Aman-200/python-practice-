# check prime number by using flag
# def prime_num(n):
#     flag=False
#     if n>1:
#         for i in range(2,n): 
#             if n%i==0:   
#                 flag=True
#                 break
#     if flag:
#         print ("this is not prime number => ",n)
#     else:
#         print ("this is prime number => ",n)
#     tryagain()
# def tryagain():
#     value=int(input("give me integer number => "))
#     prime_num(value)
# tryagain()


# def prime_num(n):
#     flag=False
#     if n>1:
#         for i in range(2,(n//2+1)): 
#             if n%i==0:   
#                 flag=True
#                 break
#     print(n//2+1)
#     if flag:
#         print ("this is not prime number => ",n)
#     else:
#         print ("this is prime number => ",n)
#     tryagain()
# def tryagain():
#     value=int(input("give me integer number => "))
#     prime_num(value)
# tryagain()


# check prime number without using flag by for else method
# def prime_num(n):
#     if n>1:
#         for i in range(2,n//2+1): 
#             if n%i==0:   
#                 print ("this is not prime number => ",n)
#                 break
#         else:
#             print ("yes this is prime number => ",n)
#     else:
#         print ("this is prime number => ",n)
#     tryagain()
# def tryagain():
#     value=int(input("give me integer number => "))
#     prime_num(value)
# tryagain()


# check prime number within intarwal by for else method
def prime_num(start,end):
    for n in range (start,end):
        if n>1:
            for i in range(2,n//2+1): 
                if n%i==0:   
                    break
            else:
                print (n)
    tryagain()
def tryagain():
    s=int(input("give me initial number => "))
    e=int(input("give me last number => "))
    prime_num(s,e)
tryagain()
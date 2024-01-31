# fibonacci simple programe
# def fibonacci(v): #4
#     a=0   
#     b=1    
#     while(b<v):
#         c=a+b   
#         a=b     
#         b=c     
#         print ("a => ",a,"fibonacci => ",b )
#     tryagain()
# def tryagain():
#     value=int(input("give me interger number =>  "))
#     fibonacci(value)
# tryagain()


# # fibonacci while programe
# def fibonacci(v): #4
#     a,b=0,1
#     while(b<v):
#         a,b=b,a+b
#         print ("a => ",a,"  fibonacci => ",b )
#     tryagain()
# def tryagain():
#     value=int(input("give me interger number =>  "))
#     fibonacci(value)
# tryagain()


# # fibonacci for programe
def fibonacci(v): 
    if v==1:
        print ("fibonacci",v)
    else:
        for i in range(2,v):
            a,b=i,a+b
            print("fibonacci",b)
    tryagain()
def tryagain():
    value=int(input("give me interger number =>  "))
    fibonacci(value)
tryagain()

 # fibonacci recurrsion programe
# def fibonacci(v): #4
#     if v<=1:
#         return v
#     else:
#         print("fibonacci  => ", fibonacci(v-1) + fibonacci(v-2))    
#     # tryagain()
# def tryagain():
#     value=int(input("give me interger number =>  "))
#     if value<=0:
#         print("fibonacci",value)
#     else:
#         for i in range(value):
#             fibonacci(i)
# tryagain()

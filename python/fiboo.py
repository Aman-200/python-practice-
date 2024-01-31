# def fibo(s):
#     a,b=0,1
#     while s>b:
#         a,b=b,a+b
#         print(a,b)
# fibo(1990)

# def fibo(s):
#     a=0
#     b=1
#     for i in range(s):
#         a,b=b,a+b
#         print(a)
#     tryagain()
# def tryagain():
#     anu=int(input("enter your number  =>  ")) 
#     fibo(anu) 
# tryagain()


def plaindrome(s):
    new=""
    no=""
    n=len(s)
    for i in range (n):
        if s[i]==s[n-i-1]:
            new=new+s[i]
        else:
            no="not"
    print(f"{new} this is {no} plaindrome")

    # b=[print(f"{s[i]}") for i in range(n) if s[i]==s[n-i-1] ] 

plaindrome("5123215") 
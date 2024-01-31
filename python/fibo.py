# def fibo(n):
#     a,b=0,1
#     while n>b:
#         a,b = b,a+b
#         print(b)
# fibo(60)

# def fibo(n):
#     a,b=0,1
#     for i in range(n):
#         a,b=b,a+b
#         print(b,)
# fibo(6)

def fibo(start, end):
    a,b=0,1
    while end>b:
        a,b=b,a+b
        if start==b:
            while end>b:
                a,b=b,a+b
                print(a)
        elif start!=b:
            while end>b:
                a,b=b,a+b
                print(a)
# start=int(input("give me starting number  =>"))
# end=int(input("give me ending number  =>"))
fibo(35,90)



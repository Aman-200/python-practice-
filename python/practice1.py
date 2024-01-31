# def fibonacci(start, end):
#     a,b=0,1
#     while(b < end):
#         a, b= b, b+a
#         if a==start:
#             while (b < end):
#                 print(a)
#                 a, b= b, b+a
#         elif a==start:
#             while (b < end):
#                 print(a)
#                 a, b= b, b+a
# fibonacci(8,35)

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

fibo(5,45)
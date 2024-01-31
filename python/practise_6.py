# def outerfun(fun):
#     def innerfun():
#         print("2, 6 innerfun")
#         return fun()
#     print("1, 4 outerfun")
#     return innerfun
# def show():
#     print("   7 show")
# @outerfun
# def display():
#     print("3   display")
# display()

# main_function=outerfun(show)
# print("   5 out of function")
# main_function()


# l=[i for i in range(20) if i%2!=0]


# l1=[1,2,3,4,5]
# l= list(map(lambda i: i%2!=0, l1))
# l=list(filter(lambda i:i%2!=0, range(20)))
# from functools import reduce
# l= reduce(lambda x,y: x+y, l1,10)
# print(l)


# l1=[1,2,3]
# l2=[11,22,33]
# l=[i*j for i in l1 for j in l2 ]
# print(l)

# d=(i for i in l1)
# print(next(d))
# print(next(d))
# print(next(d))

# l1=[1,2,3]
# l2=[11,22,33]
# # l1.extend("ab")
# l1.append((1,23,2))
# print(l1)

# d={
#     (1,2,3):1,
#     "a":"A",
    # [1]:1
# }
# del d["a"]
# d[3]="e"
# print(d[3] ," | " ,d)

# f=open("f1.txt","w")
# f.write("hi")
# # f.read()
# f.close()

# with open("f2.txt","w") as f:
#     f.write("hiii")


# la=(lambda x:x**3)(3)
# print(la)
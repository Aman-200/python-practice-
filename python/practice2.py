# l1=[1,2,3]
# l2=[4,5,6]
# print(l1,id(l1))
# # l1.append(l2)
# l3=l1.extend(l2)
# print(l3,id(l3))

# t1=(1,2,3)
# t2=(4,5,6)
# print(t1,id(t1))
# t3=t1+t2
# print(t3,id(t3))



# a=12
# b="d"
# c=("qw")
# d1={
#     (1,2,3):[a,b,c],
#     ("a","b","c"):(12,3,4),
#     "id":1
# }

# d1[1]="aman"
# print(d1[(1,2,3)])
# # print(d1.values())
# print(d1.keys())


# file1=open("aman.txt","w")
# file1.write("hellow i am aman")
# file1.close()

# with open("aman1.txt","w") as file2:
#  file2.write("i am aman")

# a= lambda x : x**3
# print(a(5))

# l4=[1,2,3,4,5,6,7]
# cube = list(map(lambda x: x**3,l4))
# print(cube)



# def outerfun(func):   #show
#     def innerfun():
#         print("2 inner function")
#         return func()
#     print("1 outer fun")
#     return innerfun

# def show():
#     print("3 this is show fun")
# newfun = outerfun(show) # newfun = innerfun
# newfun()

# @outerfun
# def display():
#     print("4 display")
# display()



# def decorator_func(func):
#     def wrapper_func():
#         print("2 wrapper_func Worked")
#         return func()
#     print("1 decorator_func worked")
#     return wrapper_func
# def show():
#     print("3 Show Worked")
# decorator_show = decorator_func(show)
# decorator_show()

# Alternative
# @decorator_func
# def display():
#     print('3 display worked')
# display()

# l5 = ["a","b",'c', 1,2,3]
# l5[]="aman"
# print(l5)


# l6=[1,2,3,4,5]
# l7=[6,7,8,9,10]

# a= [i**2 for i in l6]
# a = [(i,j) for i in l6 for j in l7 ]
# a = [i for i in l6 if i%2==1]

# print(a)


# d2= {}
# for i in range(1,10):
#     d2[i]=i**2

# d3 = { i : i**2 for i in range(1,10)}

# print(d3)



# class init_key:
#     def __init__(self, name="aman", languages="python"):
#         self.name = name
#         self.languages = languages
#     # Sample Method 
#     def say_hi(self): 
#         print(f"Hello, my name is {self.name} and my subject is {self.languages}") 
#         return "ok"

# init1 = init_key("rahan", "data structure")
# print(init1.name,init1.languages)
# print(init1.say_hi())


# discount= 5 if 4>5 else 9 if 6>7 else 8
# print(discount)

# for i in range(20):
#     if i%2==0:
#         if i == 10:
#             # break
#             continue
#             # pass
#         print(i,end=",")

# l8=[1,298,3,77,5,3,3,True]
# l9=[1,2,4,5,6,7,10]
# print(sorted(l8))
# print(l8.index(5))
# print(max(l8))
# print(min(l8))
# print(len(l8))
# # print(cmp(l8,l9))
# print(sum(l9))
# print(any(tuple(l8)))
# print(sorted(tuple(l8)))
# print(type(tuple(l8)))
# # print(count(tuple(l8)))
# print(l8.count(3))



# def argss(*args):
#     print(args)
#     print(type(args))

# argss([1,3,4,5])
# argss((1,23,4,))
# argss(1,3,4)

# def kargss(**kwargs):
#     print(kwargs)
#     print(type(kwargs))

# kargss(s = 1,b="r" )
# kargss((1,23,4,))
# kargss(1,3,4)


# f1 = open("file1.txt","w")
# f1.write("i am aman")

# with open("file2.txt","a") as f2:
#     f2.write("this is append(a) file2")

# with open("file2.txt","r") as f2:
#     c=f2.read()
#     print(c)


# a=5
# b="aman"

# try:
#     if a>b:
#         print("try")
# except :
#     print("execpt")
# else:
#     print("else")
# finally:
#     print("finally")


# d3={
#     'A': 1, 
#     'B': 2, 
#     'C': 3
# }

# print(d3.keys())
# print(list(d3))
# print(*d3)
# print(*d3,)

# s1="aman is a b tech student"
# print(s1[:].split(" "))
# print(s1[2::])
# print(s1[::-1].split("a"))

# t3=(1,2,3)
# l1=[1,2,8,3]
# print(t3, id(t3))
# print(l1, id(l1))
# t4=(4,5,6)
# l2=[4,5,8,6]
# # l1 = l1 + l2
# l1.extend(l2)
# t3=t3+t4
# print(t3, id(t3))
# print(l1, id(l1))


# x = list(map(int, input("Enter a multiple value: ").split()))
# print("List of Values: ", x)
# x = [int(x) for x in input("Enter multiple value: ").split()]
# print("Number of list is: ", x)
# x = [int(x) for x in input("Enter multiple value: ").split(",")]
# print("Number of list is: ", x)



# d3={
#     "a": "aman",
#     "b": "bom",
#     "c": "capton"
# }
# d3.clear()
# d3.pop("c")
# del d3["b"]
# del d3["c"]
# print(d3)




# def reverseList(lst):
#     if not lst:
#         return []
#     return [lst[-1]] + reverseList(lst[:-1])
# print(reverseList([1, 2, 3, 4, 5]))


# fruit = ["Apple", "Banana", "Pear"]
# map_object = map(lambda s: s[0] == "A", fruit)
# print(list(map_object)) 



# fruit = ["Apple", "Banana", "Pear"]
# filter_object = filter(lambda s: s[0] == "A", fruit)
# print(list(filter_object))



# The syntax is:
# reduce(function, sequence[, initial])

# from functools import reduce
# list = [2, 4, 7, 3]
# print(reduce(lambda x, y: x + y, list))
# print("With an initial value: " + str(reduce(lambda x, y: x + y, list, 10)))


# from functools import reduce
# def mapf(a,b):
#     c = a+b
#     return c
# print(reduce(mapf,[1,2,3,4,5]))

# print(list(map(lambda x:x**2, [1,2,3,4])))



# def even(n):
#     if n%2==0:
#         return n
#         # pass 
#     # else:
#     #     yield "this is odd"
# print(list(filter(even,range(1,20))))



# duplicate number
# l10 = [1,1,2,3,4,5,6,76,5,4,5,6,7,8]
# l11=[]
# for i in range(len(l10)):
#     for j in range(i+1,len(l10)):
#         if l10[i]==l10[j]:
#             print(l10[i])
#             break
        


# draw pattern
# for i in range(1,6):
#     for j in range(1,i+1): #(1,2)  (2,3)
#         print( i+1,"*", end="")
#     print("\n")


# for i in range(6,1,-1):
    # for j in range(1,i+1):
    #     print("*",end="")
    # print("\n")


# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*", end="")
#     print("\n")
# for k in range(6,1,-1):
#     for l in range(1,k-1):
#         print("*",end="")
    # print("\n")


# for i in range(1,6):
#     for j in range(1,6-i):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print("*",end="")
#     print("\n")


# for i in range(5,0,-1):
#     for j in range(1,6-i):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print("*",end="")
    # print("\n")


# def fact(f):
#     for i in range():
#         f=f*i
#         print(f)
#     print(f)
# fact(6)


# class polymorphish_overloading:
#     def sum(self):
#         print("no argument")

#     def sum(self,a="",b=""):
#         print(a,b,"two argument")

#     def sum(self,a="",b="",c=""):
#         print(a,b,c, "three argument")
    
# pol=polymorphish_overloading()
# pol.sum()
# pol.sum("amn","amsm")
# pol.sum("amn","amsm","djj")


# class A:
#     def c(self):
#         print("C")
#     def a(self):
#         print("A")
# class B(A):   
#     def a(self):
#         super().a()
#         print("B")
# o=B()
# print(o.a())



# import sub,sum
# sub.subb(3,5)
# sum.summ(4,3)

# class encapsulation:
#     _a=10
#     __b=20
#     def view(self):
#         print("protected",self._a)
#         print("private",self.__b)
# o=encapsulation()
# print(o.view())
# print(o._a)
# print(o.__b)


# class employ:
#     increament=1
#     employ_no=0
#     # def __init__(self, id=0, role="learning period", salery=0):
#     def __init__(self, id, role, salery):
#         self.id =id
#         self.role = role
#         self.salery = salery
#         self.increament = employ.increament * 2
#         # employ.employ_no = employ.employ_no + 1
#         employ.emoloy_nom(self)

#     def salery_increament(self):
#         # self.salery = self.salery * self.increament
#         self.salery = self.salery * employ.increament
    
#     def emoloy_nom(self):
#         employ.employ_no = self.employ_no + 1

#     @classmethod
#     def change_increament(cls, amount):
#         cls.increament = amount

#     @staticmethod
#     def working_day(day):
#         if day == "sunday":
#             return False
#         elif day == "saturday":
#             return False
#         else:
#             return True

# class company(employ):
#     pass
# ''' from class employ '''
# emp=employ(1, "python developer",5000)
# emp2 = employ(2, "django developer", 3000)

# # print(emp.id,emp.role,emp.salery, emp.employ_no)
# # emp.salery_increament()
# # emp.emoloy_nom()
# # print(emp.id, emp.role, emp.salery, emp.employ_no)


# # emp2.salery_increament()
# # print(emp2.id, emp2.role, emp2.salery, emp2.employ_no, emp2.increament)

# # emp2.change_increament(10)
# # emp2.salery_increament()
# # print(emp2.id, emp2.role, emp2.salery, emp2.employ_no, emp2.increament)

# print(emp2.working_day("saturday"))


# ''' from class company '''

# com=company(1,"role",1000)
# # print(com.working_day("saturday"))
# print(com.id, com.role, com.salery, com.employ_no, com.increament)



# palindrome

# def palindrome(n):
''' by slicing method '''
    # new = n[::-1]
    # if new == n:
    #     print(new)
    # else:
    #     print(n,new)

''' by for loop method only string'''
    # l=len(n)
    # new = ""
    # for i in range(l):
    #     if n[i]==n[l-i-1]:
    #         new = new + n[i]
    #         print(new,"this is palindrome", n[i],n[l-i-1])
    #     else:
    #         print(new,"this is not palindrome")
    #         break
    
''' by while loop method only string'''
    # l = len(n)
    # new = ""
    # i=0
    # while l>i:
    #     if n[i]==n[l-i-1]:
    #         new = new + n[i]
    #         print(new,"this is palindrome", n[i],n[l-i-1])
    #     else:
    #         print(new,"this is not palindrome")
    #         break
    #     i=i+1

''' by for loop method only integer number'''
#     reminder=0
#     quention=0
#     temp = n
#     while temp>0:   # 12321
#         reminder = n%10   # 1, 2 ,3 ,2, 1
#         quention = n//10   # 1232, 123, 12, 12
#         temp = quention * 10 + reminder  # 1, 
#         print(temp)
# palindrome(12321)

# ''' by for loop method only integer number'''
# def palindrome(n):
#     quention=n
#     reverse=0
#     while(quention > 0): #12321
#         reminder = quention%10 #1,2,3
#         reverse = reverse * 0 + reminder
#         quention = quention//10 #1232, 123, 12
#         print(reverse," ",reminder,quention)
    
# palindrome(12321)

# palindrome with the help of while loop mthod
# def palindrome(v): #1456
#     quention=v   #1456
#     reverse=0
#     while(quention>0):
#         reminder= quention%10   #6 / 5 / 4 / 1
#         reverse = reverse * 10 + reminder #0 * 10 + 6 =6/ 6*10+5=65
#         quention= quention//10  #145
#         print(reminder," ",quention, reverse)
# #     if reverse==v:
# #         print (v,"this is palindrome")
# #     else:
# #         print(v,"this is not palindrome")
# #     tryagain()
# def tryagain():
#     value=int(input("give me integer number =>   "))
#     palindrome(value)
# tryagain()


# def plaindrome(v):
#     reverse = 0
#     quention = v
#     while quention > 0:                     # 12345
#         remaminder = quention % 10          # 5, 4
#         quention = quention // 10           # 1234,123
#         reverse = reverse * 10 + remaminder # 5, 54, 
#         print(remaminder,quention, reverse)
#     if v==reverse:
#         print(f"{v} is plaindrome")
#     else:
#         print(f"{v} is not plaindrome")
# plaindrome(12345)


# def plaindrome(v):
#     l=len(v)
#     new_str=""
#     no=""
#     for i in range(l):
#         if v[i] == v[l-i-1]:
#             new_str = new_str + v[i]
#         else:
#             no ="not"
#             print(f"{v} is not palindrome" )
#     print(f"{new_str} is {no} palindrome")
    
# plaindrome("nitin")


# def string_comprestin(v): 
#     l = len(v)
#     new_s=""
#     count = 1
#     for i in range(l-1):
#         if v[i]==v[i+1]:
#             count+=1
#         else:
#             new_s = new_s + v[i] + str(count)
#             count=1
#     new_s = new_s + v[l-1] + str(count)
#     print(new_s)
# string_comprestin("aanddmwwww")

# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact = fact * i  # 1, 2, 6, 24, 120
#         print(fact,i)
# factorial(6)

# def fact(n):
#     i=1
#     fact=1
#     while i<n+1:
#         fact = fact * i
#         print(fact, i)
#         i=i+1
# fact(6)




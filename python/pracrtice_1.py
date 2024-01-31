# # l1=[1,2,3]
# # l2=[12,13,14]
# # d1={
# #     (1,2,3) : "aman",
# #     2 : [1,2,3]
# # }
# # print(*d1)
# # for i in range(20):
# #     d1[i]=12+i
# # d1[12]=12
# # print(d1)
# # d1.pop(2)
# # del d1
# # del d1[2]
# # d1.clear()
# # print(d1)
# # print(d1[2])

# # l1=[1,2,3]
# # l2=[12,13,14]
# # l_c=[i for i in range(20) if i%2==0]
# # l_c2= [i*j for i in l1 for j in l2 if i*j%2!=0]

# # s_c={i for i in range(20)}

# # g_c=(i for i in range(20))
# # # print(type(g_c),next(g_c),next(g_c),next(g_c))

# # # d_c={i:i**2 for i in range(1,20) if i%2!=0 }
# # # d_c={i:j for i in l1 for j in l2 }

# # print(d_c)

# # l1=[1,2,3]
# # l2=[12,13,14]
# # l1.append(4)
# # # l1.extend("aman")
# # print(l1)


# # a="aman"
# # try:
# #     a=a-a
# #     print(a,"try")
# # except:
# #     print(a,"except")
# # else:
# #     print(a,"else")
# # finally:
# #     print(a,"finally")

# # def outer_fun(fun):
# #     def internal_fun():
# #         print("3 internal")
# #         return fun()
# #     print("1 outer_fun")
# #     return internal_fun
# # def show():
# #     print("4 show")
# # decorator_fun = outer_fun(show)
# # print("2 out_side the fun")
# # decorator_fun()


# # with open("aman.txt", "w") as f1:
# #     f1.write("hellow")

# # x= lambda x:x**2
# # print(x(2))

# # x= (lambda x:x**2)(3)
# # print(x)

# # from abc import ABC, abstractmethod, abstractproperty
# # class car(ABC):
# #     def milage():
# #         pass
# # class tesla(car):
# #     def milage(self):
# #         print("tesla milage is 30km/h")
# # class safari(car):
# #     def milage(self):
# #         print("safari milage is 40km/h")
# # # drive class
# # t=tesla()
# # t.milage()
# # s=safari()
# # s.milage()

# # l3=[1,2,3,4,5,6,7]
# # def squ():
# #     for i in range(4):
# #         yield i**2
# # print(next(squ()),next(squ()),next(squ()),next(squ()),next(squ()))
# # print(next(squ()),next(squ()),next(squ()),next(squ()),next(squ()))

# # a=5
# # descount=3 if a<9 else 10
# # print(descount)


# # for i in range(10):
# #     if i==8:
# #         continue
# #     print(i, end=" ,")

# # l1= [1,2,3,0,2]
# # # l1=(1,2,3,0,2)
# # l1.sort()
# # print(l1)

# # i1= iter(l1)
# # print(next(i1))

# # def show(*args):
# #     print(args)
# # show(1,2,3)

# # def show(**kwargs):
# #     print(kwargs)
# # show(a=2,b=3)

# # a="amn"
# # print(f"this {a}")
# # s="1234567"
# # print(s[::-1])

# # t1=[1,2,3]
# # print(id(t1))
# # t2=[3,2,1]
# # # t1=t1+t2
# # t1.extend(t2)
# # print(id(t1),t1)

# # x = list(map(int, input("Enter a multiple value: ").split()))
# # print("List of Values: ", x)

# # def reverseList(lst):
# #     if not lst:
# #         return []
# #     return [lst[-1]] + reverseList(lst[:-1]) 
# # print(reverseList([1, 2, 3, 4, 5]))

# # l3=[1,2,3,4]
# # x=0
# # def sum(x):
# #     x = x**2
# # l=list(map(lambda x: x+1,l3))
# # l= list(filter(lambda x: x%2!=0, l3))

# # from functools import reduce
# # l=reduce(lambda x,y: x+y, l3)

# # print(l)


# # class

# # class employee:
# #     incriment=2
# #     employee_no=0
# #     def __init__(self,name,salary):
# #         self.name1 = name
# #         self.salary1 = salary
# #         self.incriment=4
# #         employee.employee_no += 1
# #     def incriment_salary(self):
# #         # self.salary1 = self.salary1 * employee.incriment
# #         self.salary1 = self.salary1 * self.incriment
# #     @classmethod
# #     def change_increament_value(cls,amount):
# #         cls.incriment = cls.incriment * amount
# #     @staticmethod
# #     def working_day(day):
# #         if day == "sunday":
# #             print("not working day")
# #         else:
# #             print("working day")

# # e = employee("aman",2000)
# # # print(e.employee_no,e.__dict__)

# # e1=employee("nitin",3000)
# # # print(e1.name1,e1.salary1)
# # # print(e1.employee_no)

# # # print(e.name1,e.salary1)
# # # print(e1.employee_no)
# # e.incriment_salary()
# # e1.incriment_salary()
# # # print(e.name1,e.salary1,)
# # # print(e1.name1,e1.salary1)

# # e.change_increament_value(10)
# # e.incriment_salary()
# # e1.incriment_salary()
# # # print(e.name1,e.salary1,)
# # # print(e1.name1,e1.salary1)
# # e.working_day("sunday")


# # class work(employee):
# #     def __init__(self, name, salary, role, age):
# #         super().__init__(name, salary)
# #         self.role = role
# #         self.age = age
# #     # def work_role(self):
# # w1= work("aman", 2000, "python",23)
# # print(w1.age,w1.name1)



# # coding interview questions

# # for i in range(1,6):
# #     for j in range(1,i+1):
# #         print(j,i,"*",end=" ")
# #     print("\n")
# # for i in range(6,0,-1):
# #     for j in range(1,i+1):
# #         print(j,i,"*",end=" ")
# #     print("\n")


# # def fibonacci_series(start, end):
# #     a,b=0,1
# #     while b<end:   #
# #         a,b = b,a+b 
# #         if start==b:
# #             while b<end :  #3  8
# #                 a,b = b, a+b
# #                 print(b)
# #         else:
# #            print(b)
# # fibonacci_series(3,8)

# # def fibonacci_series(n):  #8
# #     a,b=0,1
# #     for b in range(n):
# #         a,b = b, a+b
# #         print(b)
# # fibonacci_series(8)


# # def factoriall(n):
# #     factorial=1
# #     for i in range(1,n+1):
# #         factorial=factorial*i
# #         print(factorial,1)
# # factoriall(3)


# # def search_element(l,s):
# #     l_i=1
# #     le = len(l)
# #     while l_i<le:
# #         if s==l[l_i]:
# #             print(f"this value is in index {l_i}")
# #             break
# #         else:
# #             l_i +=1   
# # search_element([1,2,3,4,"aman",5],"aman")

            
# def second_largest_number(n):
#     # first=n[0]
#     # second=n[1]
#     # if n[0]>n[1]:
#     #     first=n[0]
#     #     second=n[1]
#     # else:
#     #     first=n[1]
#     #     second=n[0]

#     # for i in range(2,len(n)):
#     #     if n[i]>first:
#     #         second=first
#     #         first=n[i]
#     #     elif n[i]>second:
#     #         second=n[i]
#     #     print(first,second)

#     l=n.sort(reverse=True)
#     print(l)
# second_largest_number([1,88,99,2,3,44,33,22,11])
        

# l=[1,88,99,2,3,44,33,22,11]
# print(l)

# l.sort(reverse=True)
# l.remove(max(l))
# print(l)
# s=sorted(l)
# n=len(s)
# # s=max(s)
# print(s[n-2])





# def paladrom(n):
#     l=len(n)
#     new=""
#     for i in range(l):
#         if n[i]==n[l-i-1]:
#             new=n[i]
#         else:
#             print(n[i],"this is not plaindrome")
#             break
#     if new==n:
#         print(n[i],"this is plaindrome")
# paladrom("12321")


# def palindrome(n):
#     reverse=0
#     quention=n
#     while quention>0:
#         reminder = quention%10   # 1,2,3
#         quention = quention//10  #1232,123,12
#         reverse = reverse * 10 + reminder  # 12321
#         print(reverse,reminder,quention)
#     if reverse==n:
#         print(reverse,"palindrome")
#     else:
#         print(reverse,"not palindrome")
# palindrome(12321)





# def compress(n):
#     l = len(n)
#     count=1
#     new=""
#     for i in range(l-1):
#         if n[i]== n[i+1]:
#             count+=1
#         else:
#             new= new + n[i] + str(count)
#             count=1
#     new= new + n[l-1] + str(count)
#     print(new)
# compress("aaswwww")



def prime(s,e):
    for i in range(s,e):
        if n%i==0:
            # print(i,"not prime")
            break
        else:
            print("n")
prime(6,20)


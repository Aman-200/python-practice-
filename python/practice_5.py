# # name = "adarsh gupta"
# # output = "aDaRsH GuPtA"

# def string_update(s):
#     l = len(s)
#     new=""
#     for i in range(l):
#         if i%2==0:
#             new=new+s[i]         
#         else:
#             new=new+s[i].upper()
#     print(new)        
# string_update("adarsh gupta")



# # input = [1,2,2,3,4,4,5,6,6,6,6]
# # remove any duplicate ex. number 2 
# # output:[1,2,3,4,4,5,6,6,6,6]

# def remove_duplicate_number(n):
#     n2=[]
#     for i in n:
#         if i not in n2:
#             n2.append(i)
#             print(i,n2)
#     entre=int(input("enter want you want to deleate => "))
#     n2.remove(entre)
#     print(n2)
# remove_duplicate_number([1,2,2,3,4,4,5,6,6,6,6])

# class employee:
#     increament=2
#     emp_count=0
#     def __init__(self,namee="name",addreshh="satna",salaryy="00"):
#         self.name=namee
#         self.addresh=addreshh
#         self.salary=salaryy
#         employee.emp_count=employee.emp_count+1
#         self.increament=10
#     def bonus(self):
#         # self.salary=employee.increament * (self.salary)
#         self.salary = employee.increament * (self.salary)

#     @classmethod
#     def increase_increament(cls, amount):
#         cls.increament=amount

#     @staticmethod
#     def office_open_or_not(day):
#         if (day=="sunday"):
#             print(f"today means {day} is holiday")
#         elif (day=="saturday"):
#             print(f"today means {day} is holiday")
#         else:
#             print(f"today means {day} is working day")
# class office(employee):
#     def __init__(self, namee, addreshh, salaryy, languagee, agee):
#         super().__init__(namee, addreshh, salaryy)
#         self.language=languagee
#         self.age=agee

# e=employee("ram","ayodhya",2000)
# # e.bonus()
# o=office(1,2,3,"english",23)
# print(o.name, o.age)
# e.increase_increament(200)
# e.bonus()

# print(e.emp_count, e.name, e.addresh, e.salary, )
# # e1=employee("sita","janat", 3400)
# # print(e1.emp_count, e1.name, e1.addresh, e1.salary)
# # print(e.__dict__)

# e.office_open_or_not("monday")

# def outerfun(fun):
#     def innerfun():
#         print("3 inner fun")
#         return fun()
#     print("1 outer fun")
#     return innerfun

# def display():
#     print("4 display")
# # altranative
# @outerfun
# def show():
#     print("5 show (@ keyword)")
# show()

# function_call = outerfun(display)
# print("2 out of function")
# function_call()


# def outerfun(fun):
#     def innerfun():
#         print("3 inner funtion")
#         return fun()
#     print("1 outer function")
#     return innerfun
# def show():
#     print("4 show ")

# # alternative way
# @outerfun
# def display():
#     print("5 display")
# display()

# # function_call= outerfun(show)
# # print("2 out of  function")
# # function_call()


# for i in range(20):
#     if i%2==0:
#         print(i)
# output=[i*j for i in range(20) for j in range(20,30) if (i%2 !=0)]
# print(output)

# l2=[1,2,3]
# l1=[11,12,13]
# # output=[(i**j)for i in l1 for j in l2 ]
# # output={i:i*i for i in range(9,100,9) }
# # output={i**j for i in l1 for j in l2 }
# output=(i**j for i in l1 for j in l2)

# print(next(output), type(output))
# print(next(output), type(output))
# print(next(output), type(output))
# print(next(output), type(output))


# def genratorr(s):
#     for i in s:
#         # print(next(i),type(i),i)
#         yield i
# l3=[1,2,34,4]
# g = genratorr(l3)
# print(next(g),type(g),g)
# print(next(g),type(g),g)
# print(next(g),type(g),g)


l4=[1,3,1,44,5,66,"Sun","sita"]
l5=["a","b","c","d"]
# l4.extend(l5)
# l4.append(l5)
# l4[5]="radha"
# l5.extend(23)
# l4.remove(1)
# print(l4)

# d1={
#     4:l4,
#     ("a"):"ram",
#     ("a"):"rram"
# }

# t1=(1,3,1,44,5,66,"Sun","sita")
# t1[3]=3
# print(t1[4])


# f = open ("f1.txt", "r")
# # f.write("hhhh")
# f.read()
# f.close()

# with open("f.txt","w") as f1:
#     f1.write("ram")

# l=lambda x: x**5
# print(l(3))

# l6=[1,2,3,21,4,5]
# l=list(map(lambda y: y%2!=0,l6))
# l=list(map(lambda y: y**5,l6))
# print(l)

# from abc import ABC, abstractmethod, abstractclassmethod
# class car(ABC):
#     def milage():
#         pass
# class tesla(car):
#     def milage():
#         print("tesla ")
# class suzki(car):
#     def milage():
#         print("suzki ")
# class lamberginee(car):
#     def milage():
#         print("lamberginee ")

# t=tesla
# t.milage()

# s=suzki
# s.milage()

# def outerfun(fun):
#     def innerfun():
#         print("2, 6 inner fun")
#         return fun()
#     print("1, 4 outerfun")
#     return innerfun

# def display():
#     print("7 display fun")
# # alternative
# @outerfun
# def show():
#     print("3 show fun")
# show()

# function_call=outerfun(display)
# print("5 function calling")
# function_call()

# i=[i for i in range(20) if i%2!=0]
# print(i)
# l=list(map(lambda i:i%2!=0, range(20) ))
# print(l)

# d={}
# for i in range(20):
#     d[i]=i**3
# print(d)

# def generator():
    # for i in range(10):
    #     yield i
# g=generator()

# g=iter(range(20))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# age=80
# discount=30 if age>90 else 10
# print(discount)

# class a1:
#     def method(self):
#         print("a1")
#         return 0
# class a2(a1):
#     def method2(self):
#         print("a2")
# a=a1()
# print(a.method())

# l=[]
# for i in range(20):
#     if i==5:
#         # break
#         continue
#     l.append(i)
# print(l)
 

# l=[12,13,32,55,11,6,9,4,99,44]
# l1=[12,7,7,13,32,55,11,6,9,4,99,7,]
# t1=(12,13,32,55,11,6,9,4,99,44)
# s={23,43,5,61,532,1,2,55,2,2,2,2}
# print(s.add(4))
# print(s.update("7"),s)
# print(set(sorted(s)))
# s.clear()
# s.copy()
# s.remove(2)
# print(s.pop())
# print(s.pop())
# print(s,type(s))
# l1.sort(reverse=True)
# print(sorted(l1),l1)
# print(l1)
# l1=len(l)
# print(l.index(4))
# print(min(l))
# print(cmp(l,l1))
# print(list(t1))
# print(sum(l1))
# print(l1.count(7))
# print(all(l1))
# t1=(12,13,32,55,11,6,9,4,99,44)
# print(sum(t1))

# d={
#     ("a",23): 23,
#     3:"aman"
# }
# del d[3]
# print(d.pop(("a",23)),d)
# print(d.clear(),d)

# print(list(d))
# print([d.keys()])

# d1=d.copy()
# d2=d
# del d[3]
# print(d1,d2)
# print(d.get(3))
# print(d.keys())
# print(d.values())

# print(chr(95))

# def fun1(*ar):
#     print(ar)
# fun1(1,2,3,"s","e")

# def kwargs(**kwargs):
#     print(kwargs)
# kwargs(a="e", b=3)

# with open("f.txt","w") as f1:
#     f1.write("kdsk")

# f=open("f.txt","w")
# f.write("shgsjdddd")
# f.close()

# a=3
# b=4
# try:
#     c=a+b
#     print("1 try")
# except:
#     print("2 expet")
# else:
#     print("4 (else) except not run")
# finally:
#     print("3 finally important code write always print")

# s1="aman kashyap"
# s2="krisna"
# s3="ram"
# # print(f"hi i m {s3} and he is {s2} and this is {s1}")
# print(("hi i m {} and he is {} and this is {}").format(s1,s3,s2))

# s = 'HelloWorld'
# print(s[::-1])
# print(s[:3:])

# t1=(1,2,3)
# t2=(4,5,6)
# print(t1,id(t1))
# print(t2,id(t2))
# t1=t1+t2
# print(t1,id(t1))
# print(t2,id(t2))

# t1=[1,2,3]
# t2=[4,5,6]
# print(t1,id(t1))
# print(t2,id(t2))
# t1.append(t2)
# print(t1,id(t1))
# print(t2,id(t2))
# import array
# l1=[1,2,3]
# l2=[4,5,6]
# # l1=l1.add(l2)

# s="Copy A Dictionary Using copy()"
# print(s.split("i"))

# x = list(map(int, input("Enter a multiple value: ").split()))
# print("List of Values: ", x)

# x = [int(x) for x in input("Enter multiple value: ").split()]
# print("Number of list is: ", x)


# l=(lambda i,y: i**y)(3,3)
# print(l)

# def reverseList(lst):
#     if not lst:
#         return []
#     return [lst[-1]] + reverseList(lst[:-1])
# print(reverseList([1, 2, 3, 4, 5]))

# from functools import reduce
# l1=[1,2,3,4,5]
# # l=list(filter(lambda x: x%2!=0,l1))
# # l=list(map(lambda x: x%2!=0,l1))
# l=(reduce(lambda x,y: x+y,l1,10))
# print(l)

# c= "AaZffWaabccy"
# c=c.lower()
# d={}
# for i in range(97,123):
#     ch=chr(i)
#     count=0
#     for j in c:
#         if ch == j:
#             count=count+1
#     if count>0:
#         d[ch]=count
#         # print(ch," : ", count)  

# # largest frequency 
# # print(sorted(list(d.values())))

# v=d.values()  
# li=sorted(list(v))
# le=len(li)
# print(li[le-1])
# # print(sorted(list(d.values())))

# change your string
# def string_change(s):
#     s1=""
#     ss=s.split(" ")
#     print(ss)
#     for i in ss:
#         s1=s1 + i[::-1] + " "
#     print(s1)
# string = input("enter your string ")
# string_change(string)

# s="hi this is aman gupta"
# li=s.split(" ")
# for i in li:
#     print(i[::-1], end=" ")


# def plaindrome(s):  
#     new_s= s[::-1]
#     if new_s==s:
#         print(f"{s} this is plaindrome")
#     else:
#         print(f"{s} this is not plaindrome")
# plaindrome("123321")


# def plaindrome(s):
#     l=len(s)
#     first=0
#     last=l-1
#     while(last>first):
#         if s[first]==s[last]:
#             first+=1
#             last-=1
#         else:
#             return print("this is not plaindrome")
#         return print("this is plaindrome")
# plaindrome("2112")

# def plaindrome(s):
#     l=len(s)
#     condition=""
#     new_s=""
#     for i in range(l):
#         if s[i]==s[l-i-1]:
#             new_s=new_s+s[i]
#             condition="is"
#         else:
#             return print("this is not plaindrome")
#     print(f"{new_s} this {condition} plaindrome")       
# plaindrome("12321")

# number palindrome
# def num_plaindrome(n):
#     quention=n 
#     reverse=0
#     while(quention>0): #1234
#         reminder=quention%10   #4,3,2,1
#         quention=quention//10  # 123,12,1
#         reverse=reverse*10+reminder #4, 43, ,432, 4321
#         # print(reminder,reverse,quention)
#     if n==reverse:
#         print(f"{reverse} this is plaindrome")
#     else:
#         print(f"{reverse} this is not plaindrome")
# num_plaindrome(12321)

# def plaindrome(n):
#     quention=n
#     reverse=0
#     while(quention>0):    #1234
#         remindre=quention%10 #4,3,2,1
#         quention=quention//10 #123,
#         reverse=reverse*10+remindre #4
#         print(quention,remindre,reverse)
#     if reverse==n:
#         print("this is plaindrome")
#     else:
#         print("this is not plaindrome")
# plaindrome(121)

# def fibonaccii(n):
#     a,b=0,1
#     for i in range(n):
#         a,b=b,a+b
#         print(b)
# fibonaccii(7)

# def prime(n):
#     for i in range(s,e):
#         if n%i==0:
#             return print(f"{i} | {n}| {n%i} |this is not prime")
#         else:
#             print(f"{i} | {n}| {n%i} |this is prime")
# prime(88)


# def prime_inrerwal(s,e):
#     for i in range(s,e):
#         if i>1:
#             for j in range(2,i//2+1):
#                 if i%j==0:
#                     break
#             else:
#                 print(i)
# prime_inrerwal(2,30)


# def string_occ(s):
#     l=len(s)
#     new_s=""
#     count=1
#     for i in range(l-1):
#         if s[i]==s[i+1]:
#             count+=1
#         else:
#             new_s=new_s + s[i] + str(count)
#             count=1
#     new_s=new_s + s[i] + str(count)
#     print(new_s)
# string_occ("aaaffjnnnnjjjaaaaaaaa")


# def string(s):
#     s1=""
#     for i in range(len(s)):
#         if i%2==0:
#             s1=s1+s[i].lower()
#         else:
#             s1=s1+s[i].upper()
#     print(s1)
# string("hi this is aman")


# # input = [1,2,2,3,4,4,5,6,6,6,6]
# # remove any duplicate ex. number 2 
# # output:[1,2,3,4,4,5,6,6,6,6]

# def remo(l):
#     print(l)
#     e=int(input("inter what you want to deleate => "))
#     l1=[e]
#     for i in l:
#         if i==e:
#             l.remove(e)
#         else:
#             l1.append(i)
#     print(l,l1)
# remo([1,2,2,3,4,4,5,6,6,6,6])

# def remove_dublicate(s):
#     print(s)
#     count=1
#     l2=len(s)
#     new_s=""
#     d={}
#     for i in range(0,l2-1):
#         if s[i]==s[i+1]:
#             count+=1
#         else:
#             # new_s=new_s+s[i]+str(count)+"   "
#             d[s[i]]=count
#             count=1
#     # new_s=new_s+s[i]+str(count)+"   "
#     d[s[i]]=count
#     print(d)

#     enter=input("enter want you want to deleate  => ")
#     del d[enter]
#     d[enter]=1
#     print(d)


#     k=list(d.keys())  #<class 'list'>
#     v=list(d.values()) #<class 'list'>
#     print(f"keys {k} | values {v} ")
#     # ks=sorted(k)
#     # vs=sorted(v)
#     l2=[]
#     l=len(k) 
#     for i in range(l):
#         for j in range(v[i]):
#             l2.append(int(k[i]))
#     print(l2)

# l1=[1,2,2,3,9,4,4,5,6,6,6,6,8,8]
# s=""
# for i in l1:
#     s=s+str(i)
# remove_dublicate(s)

# import re
# s="Aman is one 12321-6489 amanammmmmmanananananaamamamamamnnn amannnnnnnnn ammmmmannnnnnn ammmmmmman  haiaiiin anything year contain working experince as a backend django developer in Django Softwares Private Limited and he is a versatile individual looking to pursue a rewarding and challenging career in an organization, that would be mutually beneficial in terms of his learning experience and his contribution to organizational growth. He has knowledge of OPS, developing, testing, and debugging code, designing interfaces; and data analytics, data science, Full Stack Web Developer, object-relational mapping (ORM), Good understanding of SDLC and methodologies, Knowledge of Cloud services. He can quickly learn and master new technologies; he is successful in working in both teams and self-directed settings. Specialties: Python, Django, Django rest APIs, ORM, Git, HTML5 & CSS3, JQuery, Bootstrap, Pandas, Matplotlip, Seaborn, NumPy, Statics, MS Excel and MS Word, Odoo and ERPNext framework"
# c= re.compile(r"a[a-z]g")
# c=re.compile(r".ing")
# c=re.compile(r'ing$')
# c=re.compile(r"^Aman")
# c=re.compile(r"work$")
# c= re.compile(r"am+a*")
# c=re.compile(r"(am)+ | (an)+")
# c=re.compile(r"(am){3}")
# c=re.compile(r"am{3} | aman")
# c=re.compile(r"am{3} & a")
# c=re.compile(r"\AAman")
# c=re.compile(r"\bAman | \bdjango")
# c=re.compile(r"\d{5}-\d{4}")


# c=re.compile(r"work$")
# print(s[::-1])
# m=c.finditer(s)
# for i in m:
#     print(i)


# l=[1,2,3,4,5,5,56,3,3]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]==l[j]:
#             print(l[i],"dublicate")


# a=955
# b=834
# c=444
# maxn=a if a>b>c else b if b>c else c
# print(maxn)

# def plaindrome(s):
#     l=len(s)
#     for i in range(l):
#         if s[i]==s[l-i-1]:
#             # print(s[i],s[l-i-1],"yes")
#             pass
#         else:
#             # print(s[i],s[l-i-1],"no")
#             return print("not plaindrome")
#     return print("plaindrome")
# plaindrome("12345")

# def plaindrome(s):
#     l=len(s)
#     i=0
#     while(i<l):
#         if s[i]==s[l-i-1]:
#             i=i+1
#         else:
#             i=i+1
#             return ("not plaindrome")
#     return print("this is plaindrome")
# plaindrome("123281")



# def second_largest_number(l):
#     if l[0]>l[1]:
#         first=l[0]
#         second=l[1]
#     else:
#         first=l[1]
#         second=l[0]
#     for i in range(2,len(l)):
#         if first<l[i]:
#             second=first
#             first=l[i]
#         elif second<l[i]:
#             second=l[i]
#         print(first,second,l[i],l)
#     # print(l)           

#     print(second)
# second_largest_number([81,66,75,76,3])



# # input = [1,2,2,3,4,4,5,6,6,6,6]
# # remove any duplicate ex. number 2 
# # output:[1,2,3,4,4,5,6,6,6,6]

# def remove_dubplicat(l):
#     s=""
#     count=1
#     for i in l:
#         s=s+str(i)
#     d={}
#     for i in range(len(s)-1):
#         if s[i]==s[i+1]:
#             count+=1
#         else:
#             d[s[i]]=count
#             count=1
#     d[s[i]]=count
#     print(d)

#     enter= input("enter delate element  => ")
#     del d[enter]
#     d[enter]=1
#     print(d)

#     v=list(d.values())
#     k=list(d.keys())
#     print(k,v)
#     l1=[]
#     for i in range(len(v)):
#         for j in range(v[i]):  #[1, 2, 1, 2, 1, 1]
#             for l in k[i]:    #['1', '2', '3', '4', '5', '6']
#                 l1.append(l)
                
#     print(l1)
            
# remove_dubplicat([1,2,2,3,4,4,5,6,6,6,6])




# def remove_dubplicat(l):
#     enter=int(input("enter => "))
#     l2=[enter]
#     for i in l:
#         if enter==i:
#             l.remove(enter)
#         else:
#             l2.append(i)
#     print(l2)
# remove_dubplicat([1,2,2,3,4,4,5,6,6,6,6])


def prime_num(start,end):
    for n in range (start,end):
        if n>1:
            for i in range(2,n): 
                if n%i==0:   
                    break
            else:
                print (n)
prime_num(2,30)
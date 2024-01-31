# def outre_fun(fun):
#     def inner_fun():
#         print("3 inner fun")
#         return show()
#     print("1 outer fun")
#     return inner_fun
# def show():
#     print("4 show")

# outre_function = outre_fun(show)
# print("2 out side the function")
# outre_function()
# l2=[1,2,3]
# l3=[12,13,14]
# l1=[(i*j) for i in l2 for j in l3 ]
# print(l1)

# d1={i:i**3 for i in range(1,10)}
# print(d1)

# s1={i for i in range(20) if i%2==0}
# print(s1)

# t1=(i for i in range(20) if i%2==0)
# print(next(t1))
# print(next(t1))
# print(next(t1))

# def genrator(l1):
#     for i in l1:
#         yield i
# l1=[1,2,3]
# genrator_values = genrator(l1)
# print(next(genrator_values))
# print(next(genrator_values))
# print(next(genrator_values))

# l2=[1,2,3]
# l3="a"
# l2.extend(4)
# print(l2)

# d2={
#     ("a","s","d"):[1,2,3],
#     "as":"aman",
# }
# d2[1]="aman"
# print(d2["as"])
# print(d2.keys())
  

# f1= open("hallo.txt","w") 
# f1.write("aman")
# f1.close()

# with open("f2.txt","w") as f3:
#     f3.write("amannnn")


# l3=[1,2,3,4,5,5]
# l4=list(filter((lambda x: x%2!=0),l3))
# print(l4)


# a=["12"]
# b=["12"]
# print(id(a),id(b))

# for i in range(20):
#     if i%2==0:
#         print(i)

# def fun1(**kwargs):
#     print(kwargs)
# fun1(a=2,b=3)

# a=2
# b="jh"
# try:
#     c=a*b
#     print("try",c)
# except:
#     print("Except")
# else:
#     print("else")
# finally:
#     print("finally")

# d2={
#     ("a","s","d"):[1,2,3],
#     "as":"aman",
# }
# d2[1]="aman"
# # del d2["as"]
# # d2.pop("as")
# d2.clear()
# print(d2)



# class employ:
#     increament=2
#     employ_no=0
#     def __init__(self, name, salary):
#         self.nname = name
#         self.ssalary = salary
#         self.increament=10
#         employ.employ_no = employ.employ_no + 1
#     def change_increament(self):
#         self.ssalary= self.ssalary * self.increament
#     @classmethod
#     def increase_salary(cls, amount):
#         cls.increament = cls.increament + amount
#     @staticmethod
#     def working_day(day):
#         if (day=="monday") | (day=="sunday"):
#             print("not working day")
#         else:
#             print("working day")
# e=employ("aman",2000)
# # print(e.nname,e.ssalary,e.employ_no)
# e1=employ("aman",2000)
# # print(e1.nname,e1.ssalary,e1.employ_no)
# e.increase_salary(2)
# e.change_increament()
# print(e.nname,e.ssalary,e.employ_no)

# print(employ.working_day("sunday"))
# print(e.__dict__)


# def palindrome(s):
#    r=s[::-1]
#    if s==r:
#     print("plaindrome")
#    else:
#     print("not plaindrome")
# palindrome("nit8in")


# def plaindrome(s):
#     r=reversed(s)
#     rr="".join(r)
#     print(rr)
# plaindrome("12345")

# def plaindrome(s):
#     n=len(s)
#     f=s[0]
#     l=s[n-1]
#     i=0
#     while f==l:
#         f=s[i]
#         l=s[n-i-1]
#         i+=1
#     if f==s:
#         print("palindrome")
#     else:
#         print("not palindrome")
# plaindrome("127821")


# def palindrome(v):
#     quention=v
#     reverse=0
#     while quention>0:
#         reminder=quention%10
#         quention=quention//10
#         reverse= reverse*10 + reminder
#         print(reminder,quention,reverse)
# palindrome(123)

# def fibonacci(n):
#     a,b=0,1
#     while n>a:
#         a,b=b,a+b
#         print(a)
# fibonacci(6)


def compress(s):
    s=s.lower()
    s=list(s)
    s.sort()
    # print(s)
    l=len(s)
    count=1
    new_s=""
    d={
        count:s
    }
    for i in range(l-1):
        if s[i]==s[i+1]:
            count+=1
        else:
            new_s = new_s + s[i] + str(count)
            d[count]=s[i]
            count=1
    new_s = new_s + s[l-1] + str(count)
    d[count]=s[i]
    # print(new_s)
    l=list(d.keys())
    print(l)
    # l.sort(reverse=True)
    l1=len(l)
    print(d[l[1]])
    # print(l1)
compress("assaaaSSssss")


# def compress(s):
#     s=s.lower()
#     c=""
#     count=0
#     d={
#         count:c
#     }
#     for i in range(97,123):
#         count=0
#         c=chr(i)
#         for j in s:
#             if c==j:
#                 count+=1        
#         d[count]=c
#         if count>0:
#             print(d)
# compress("aaaaSSssss")



# def prime_num(s,n):
#     for i in range(s,n):
#         if n%i==0:
#             print(i,"prime")
#         # else:
#         #     print(i,"not prime")
# prime_num(2,30)




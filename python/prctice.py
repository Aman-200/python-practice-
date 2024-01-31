# a ="1453,24"  
# new_l=[]
# s=""
# for i in a:           # [new_l.append(int(i)) for i in a if i!=","]
#     if i == ",":
#         continue
#     new_l.append(int(i))
# new_l.sort(reverse=False)
# print(type(new_l), new_l)

# for j in new_l:               
#     if j == 4:              
#         continue             
#     s = s + str(j)
# print(type(s), s)


# a="1453,24"
# l1 = list(a)
# l1.sort()
# print(l1)

# l2= list(set(l1[1:]))
# print(l2)
# l2.sort()
# l3="".join(l2)
# print(l3)
 


# # input = [1,2,2,3,4,4,5,6,6,6,6]
# # remove any duplicate ex. number 2 
# # output:[1,2,3,4,4,5,6,6,6,6]

# def remo(l):   #[1,2,3,4,4,5,6,6,6,6]
#     enter =int(input("enter => "))
#     l1=[enter]
#     for i in l:
#         if (enter==i):
#             l.remove(enter)  
#         else:
#             l1.append(i)
#     print(l1)
# remo([1,2,2,3,4,4,5,6,6,6,6])


# import re
# strr="A Project is the entire Django application and an App is a module inside the project thatdeals with one specific use caseFor Example:- payment system(app) in the eCommerce app(Project).An App is basically a web Application that is created to perform a specific task.A project, on the other hand, is a collection of these apps.Therefore, a single project can consist of number of apps and a single app can be inmultiple projects"
# path= re.compile(r'e$')
# match = path.finditer(strr)
# for i in match:
#     print(i)

# l1=[1,2,3]
# l2=[11,22,33]
# l=[(i*j) for i in l1 for j in l2 if i*j%2!=0]
# print(l)

# l=list((filter((lambda i:i%2!=0),l1)))
# print(l)



# def repeate(l):
#     if l[0]>l[1]:
#         first=l[0]
#         second=l[1]
#     else:
#         second=l[0]
#         first=l[1]
#     for i in range(0,len(l)):
#         if l[i]>first:
#             second=first
#             first=l[i]
            
#         elif second>l[i]:
#             second=l[i]
#     print(first,second)
# l3=[17,2,3,1114,2,112,3,3,4,11,1,18]
# l3.sort(reverse=True)
# print(l3[1],l3)
# repeate(l3)


# def strs(s):
#     s1=""
#     s=s.split(" ")
#     for i in s:
#         # print(i)
#         s1=s1 + i[0].upper() + i[1:] +" "
#     print(s1)
# s="my name is aman and today is may interview"
# strs(s)



# # name = "adarsh gupta"
# # output = "aDaRsH GuPtA"

# def strr(s):
#     s1=""
#     for i in range(len(s)):
#         if i%2!=0:
#             s1=s1 + s[i].upper() 
#         else:
#             s1=s1+s[i]
#     print(s1)
# strr("adarsh gupta")




# def strr(s):
#     s=s.lower()
#     l=len(s)
#     s1=""
#     for i in range(97,123):
#         c=chr(i)
#         count=0
#         for j in s:
#             if c==j:
#                 count+=1
#         if count>0:
#             print(c,":",count)
# strr("aabccAACCCy")


# # input = [1,2,2,3,4,4,5,6,6,6,6]
# # remove any duplicate ex. number 2 
# # output:[1,2,3,4,4,5,6,6,6,6]

# def rem(l):
#     print(l)
#     enter= int(input("enter=> "))
#     l1=[enter]
#     for i in l:
#         if i==enter:
#             del l[i]
#         else:
#             l1.append(i)
#     print(l1)
# rem([1,2,2,3,4,4,5,6,6,6,6])


def rem(s):
    l2=len(s)
    s1=""
    count=1
    d1={
        s1:count
    }
    for i in range(l2-1):
        if s[i]==s[i+1]:
            count+=1
        else:
            d1[s[i]]=count
            count=1
    d1[s[i]]=count
    print(d1)

    enter= input(" enter =>")
    del d1[enter]
    del d1[""]
    d1[enter]=1
    

    k=list(d1.keys())
    v=list(d1.values())
    print(k,v)

    l4=len(v)
    l3=[]
    for c in range(l4):   #[1, 2, 1, 2, 4, 1]
        for j in range(v[c]):
            l3.append(k[c])
    print(l3)


l1=[1,2,2,3,4,4,5,6,6,6,6]
s=""
for i in l1:
    s=s+str(i)

rem(s)

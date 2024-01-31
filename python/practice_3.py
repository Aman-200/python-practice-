# l1=[]
# v="aabdbea,d"
# l1.extend(v)
# l1.sort()
# print(l1)

# def char_occ(l1):
#     length = len(l1)
#     l2=[]
#     # for i in range(length):
#     #     l2= l2.append()
# char_occ(l1)

# def least_occyrance(s):
#     s = s.lower()
#     count=0
#     c=""
#     d={
#         count:c
#     }
#     for i in range(97,123): 
#         c=chr(i) 
#         count=0    
#         for j in s:               #"AAmvwwwaA"
#             if c==j:
#                 count +=1
#         if count>0:
#             d[count]=c
#     print(d)
#     l=list(d.keys())
#     l.sort()
#     print(d[l[1]]," is least repeated value")
# least_occyrance("AAmvwwwaA")


# 

# def string_back(s):
#     s=s.split(" ")
#     for i in s:
#         print(i[::-1],end=" ")
# string_back("hi this side aman kashyap")

# def string_permutuation(s):
#     l=len(s)
#     for j in s:
#         for k in s:
#             for l in s:
#                 if ((j!=k) & (j!=l) & (k!=l)):
#                     print(j,k,l)
#                 else:
#                     continue
# string_permutuation("123")

def string_permutuation(s):
    l=len(s)
    for j in s:
        print(j)
string_permutuation("123")
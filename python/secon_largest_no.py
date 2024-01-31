# def second_highest_number(v):
#     n=len(v)
#     s=sorted(v, reverse=True)
#     print(s)
#     print(s[1])
# second_highest_number([4,5,3,4,54,65,85,67,84,76])

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
#         # print(first,second,l[i],l)
#     # print(l)           
#     print(second,l)
# second_largest_number([81,66,75,76,3])


# def second_highest_number(v):
#     first=0
#     second=0
#     if v[0]>v[1]:
#         first=v[0]
#         last=v[1]
#     else:
#         first=v[1]
#         last=v[0]
#     for i in range(2,len(v)):
#         if first < v[i]:
#             second=first
#             first=v[i]
#         elif second<v[i]:
#             second=v[i]
#         print(second,v)
# second_highest_number([81,66,75,76,3])

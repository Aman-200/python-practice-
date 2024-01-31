# # second highest number
def second_highest_number(l):
    # print(type(l))
    if l[0]>l[1]:
        first=l[0]
        second=l[1]
    else:
        second=l[0]
        first=l[1]
    for i in range(2,len(l)):
        if l[i] > first:
            second=first
            first=l[i]
        elif l[i] > second:
            second=l[i]
    print(second)
def tryagain():
    value=[int(input("give me integer number =>   "))]
    second_highest_number([4,5,3,4,54,65,85,67,84,76])
tryagain()

# second highest number
# def second_highest_number_using_sort(l):
#     l.sort()
#     print(l[-2],l)
# second_highest_number_using_sort([4,5,3,4,54,65,85,67,84,76])
    

# second highest and smalest number
# def second_highest_number_using_sort(l):
#     l.sort(reverse=True)
#     print("l.sort: second smalest number => ",l[-2],l)
#     l.sort()
#     print("l.sort(reverse=True): second highest  number => ",l[-2],l)
# second_highest_number_using_sort([4,5,3,4,54,65,85,67,84,76])
    
# find the nth highest number
# def second_highest_number_using_sort(l,n):
#     l.sort(reverse=True)
#     print(n," highest number is => ",l[n-1],l)
    
# v=[4,5,3,4,54,65,85,67,84,76]
# value=int(input("give me N th highest number =>   "))
# second_highest_number_using_sort(v,value)
    

# find highest number using set snd max
# l=[4,5,3,4,54,65,85,67,84,76]
# new = set(l)
# print(new)
# new.remove(max(new))
# print(new)
# print(max(new))
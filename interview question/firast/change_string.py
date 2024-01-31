# # name = "adarsh gupta"
# # output = "aDaRsH GuPtA"

# def string_manupulation(s):
#     l=len(s)
#     s1=""
#     for i in range(l):
#         if i%2==0:
#             s1=s1+s[i]
#         else:
#             s1=s1+s[i].upper()
#     s=s1
#     print(s)
# string_manupulation("adarsh gupta")



# def string_manupulation(s):
#     new=""
#     s1=""
#     new=s.split(" ")
#     for i in new:
#         s1=s1+i[0].lower()+i[1:].upper()+" "
#     print(s1)
# string_manupulation("this is Aman kashyap and")

# # # frequency of the string
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
#         d[count]=ch
#         # print(count," : ", ch)  

# # largest frequency 
# # print(sorted(list(d.keys())))

# k=d.keys()              #print(type(k))
# li=sorted(list(k))
# le=len(li)              #print(li[le-1])
# # print(d[li[le-1]],"=>",li[le-1],"| dictionary is ",d)
# print(f"the largest number of frequency is {li[le-1]} of {d[li[le-1]]} from the dictonary {d}")



def prime(l):
    for i in range(2,l):
        if l%i==0:
            print(i," not prime")
            break
        
prime(15)
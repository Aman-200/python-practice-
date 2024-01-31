# # least occurance chracter
def least_ch_occurance(s):
    print("your string is  => ",s)
    ch={}
    for i in s:
        if i in ch:
            ch[i]=ch[i]+1
            # print(ch[i]+1,ch[i])
        else:
            ch[i]=1
    print("your string are repeated  => ",ch)
    result = min(ch, key =ch.get)
    print("least chracter is  => ",result)
    tryagain()
def tryagain():
    value=input("give me string  =>  ")
    least_ch_occurance(value)
tryagain()

# using inbuilt function "counter"

# from collections import Counter
# def least_ch_occurance(s):
#     ch={}
#     ch=Counter(s)
#     result = min(ch, key =ch.get)
#     print("least chracter is  => ",result)
# def tryagain():
#     value=input("give me string  =>  ")
#     least_ch_occurance(value)
# tryagain()


# count of any particular element 
# by using count (for aaaaa'string',"list","number")

# l=[1,2,3,4,5,6,4,3,4,5,6]
# print(l.count(4))
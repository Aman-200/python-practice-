# aaabbbcdd = a3b3c1d2

# # compress string by using for loop
# def compress_string(v):
#     n=len(v)
#     new=""
#     count=1
#     for i in range(n-1):
#         if v[i]==v[i+1]:
#             # new = new + v[i] + str(count)
#             count+=1         
#         else:
#             new = new + v[i] + str(count)
#             count=1      
#     new = new + v[n-1] + str(count)
#     print(new)
#     tryagain()
# def tryagain():
#     value=input("give me string  =>  ")
#     compress_string(value)
# tryagain()


# compress string by using while loop
def compress_string(v):
    n=len(v)
    new=""
    count=0
    i=0
    while(i<n-1):
        if v[i]==v[i+1]:
            count+=1
        else:
            new= new + v[i] + str(count)
            count=1
        i=i+1
    new= new + v[i] + str(count)
    print(new)
    tryagain()
def tryagain():
    value=input("give me string  =>  ")
    compress_string(value)
tryagain()
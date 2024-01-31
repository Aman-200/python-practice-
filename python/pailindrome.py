# def palindrome(n):
#     for i in range(len(n)-1):
#         if n==n[::-1]: # nitin
#             print("this is plaindrome")
#         else:
#            print("this is not plaindrome")
# palindrome("nitin")

def palindrome(s):
    n=len(s)
    new=''
    no=""
    for i in range(n):
        if s[i]==s[n-i-1]:
            new=new+s[i]
        else:
            no="not"
    print(f"{new} this is {no} plaindrome")
palindrome("1232")

# def palinderome(s):
#     rev = reversed(s)
#     new_s = "".join(rev)
#     # print(next(new_s))
#     print(new_s)
# palinderome("aman")

# a="aman"
# for i in a:
#     b="".join(i)
#     print(b) #  aman
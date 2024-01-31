# palindrome with the help of slicing mthod

def palindrome(s):
    check=s[::-1]
    if check==s:
        print(s," this is palindrome \n\ntry again ")   
        tryagain()
    else:
        print(s," this is not palindrome \n\ntry again ")
        tryagain()

def tryagain():
    value=input("give me string =>   ")
    palindrome(value)
tryagain()


# palindrome with the help of for loop mthod

# def palindrome(v):
#     r=len(v)
#     for i in range(r):
#         if v[i] == v[r-i-1]: #[5-0-1]
#             print(v[i],i,r-i-1," this is palindrome")
#         else:
#             print(v[i],i,r-i-1," this is not palindrome")
# def tryagain():
#     value = input("give me input =>  ")
#     palindrome(value)
# tryagain()


# palindrome with the help of 'join, reversed' mthod

# def palindrome(v):
#     rev=reversed(v)
#     check="".join(rev)
#     if v==check:
#         print("this is palindrome")
#     else:
#         print("this is not palindrome")
# def tryagain():
#     value=input("give me input =>  ")
#     palindrome(value)
# tryagain()

# palindrome with the help of while loop mthod

# def palindrome(v):
#     l=len(v)
#     first=0
#     last=l-1
#     while(v[first]<v[last]):
#         if v[first]==v[last]:
#             first=first+1
#             last=last-1
#         else:
#             print(v,"  this is not palindrome")
#             tryagain()
#     print(v,"  this is palindrome")
#     tryagain()
# def tryagain():
#     value=input("give me input =>  ")
#     palindrome(value)
# tryagain()

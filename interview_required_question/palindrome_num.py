# palindrome with the help of slicing string mthod
# def palindrome(v):
#     s=str(v)
#     l=len(s)
#     for i in range(l):
#         if s[i]!=s[l-i-1]:
#             print(s[i],s[l-i-1],"this is not palindrome in index num", i, l-i-1, "respectively")
#             return tryagain()
#     print("this is palindrome")
#     return tryagain()
# def tryagain():
#     value=input("give me string =>   ")
#     palindrome(value)
# tryagain()


# palindrome with the help of while loop mthod
def palindrome(v): #1456
    quention=v   #1456
    reverse=0
    while(quention>0):
        reminder= quention%10   #6 / 5 / 4 / 1
        reverse = reverse * 10 + reminder #0 * 10 + 6 =6/ 6*10+5=65
        quention= quention//10  #145
        print(reminder," ",quention, reverse)
    if reverse==v:
        print (v,"this is palindrome")
    else:
        print(v,"this is not palindrome")
    tryagain()
def tryagain():
    value=int(input("give me integer number =>   "))
    palindrome(value)
tryagain()

# def palindrome(v): #1456
#     s=int(len(str(v)))
#     print(s)
#     quention = v  #1456
#     reverse=0
#     for i in range(s,0):
#         reminder = quention % 10   #6
#         quention = v // 10  #145
#         reverse= reverse*10 + reminder #0*10+6=6
#         print(reminder," ",quention, reverse , " ", i)
#         i=s-1
#     if v==reverse:
#         print(v,"this is palindrome")
#     else:
#         print(v,"this is not palindrome")
#     tryagain()
# def tryagain():
#     value=int(input("give me integer number =>   "))
#     palindrome(value)
# tryagain()

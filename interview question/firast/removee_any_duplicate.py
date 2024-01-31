# # input = [1,2,2,3,4,4,5,6,6,6,6]
# # remove any duplicate ex. number 2 
# # output:[1,2,3,4,4,5,6,6,6,6]

def removee_any_duplicate(ss):
    print(ss)
## CHARCTER OCCERANCE WITHIN DICTONARY
    count=1
    length=len(ss)
    s3=""
    d={
        s3:count
    }
    for i in range(length-1):
        if s[i]==s[i+1]:
            count+=1
        else:
            d[s[i]]=count
            count=1
    d[s[length-1]]=count
    print(d)

## DELEAT THE PERTICULAR ELEMENT
    enter=input("what you want to dalete   => ")
    del d[enter]
    del d[""]
    d[enter]=1
    print(d)


## CHANGE DICTIONARY TO LIST
    key=d.keys()
    value=d.values()
    key=list(key)
    value=list(value)
    print("keys are => ",key,"  |   values are => ",value)
    l2=[]
    length=len(value)
    for c in range(length):  #6
        for j in range(value[c]):   # [1, 2, 1, 2, 1, 4]
            l2.append(int(key[c]))  # ['1', '2', '3', '4', '5', '6']
    print(l2)

## OUT OF FUNCTION
l= [1,2,2,3,4,4,5,6,6,6,6]

## CHANGE LIST TO STRING
s=""
for i in l:
    s=s+str(i)
removee_any_duplicate(s)


# # # second way
# def remo(l):   #[1,2,3,4,4,5,6,6,6,6]
#     print(l)
#     enter =int(input("enter what you want to deleate => "))
#     l1=enter    #l2=[enter]
#     for i in l:
#         if (enter==i):
#             l.remove(enter)  
#         else:
#             l1.append(i)
#     print(l1)
# remo([1,2,2,3,4,4,5,6,6,6,6])

# # employ.objects.filter(salary>50000)


# employ
# Name
# age
# id 
# salary

# detail=> user detail table
# dob
# link

# detail.objects.filter(employ__id__gte=5)


# a=[1,2,3,4]
# b=a
# b.remove(3)
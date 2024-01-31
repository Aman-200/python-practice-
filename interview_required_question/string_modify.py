# def string_modify(v,g):
#     print(v.split(g))
#     tryagin()
# def tryagin():
#     value=input('give me string => ')
#     signe=input('give me sine which base you want to split => ')
#     string_modify(value,signe)
# tryagin()

# def string_modify(v,g):
#     l=[]
#     temp=v.split(g) #this_is_goood_morning
#     for i in temp:
#        l.append(i[0].lower() + i[1:].upper())
#     print(l)
#     v=".".join(l)
#     print(v)
#     tryagin()
# def tryagin():
#     value=input('give me string => ')
#     signe=input('give me sine which base you want to split => ')
#     string_modify(value,signe)
# tryagin()


def string_modify(v,g):
    l=[]
    new=""
    temp=v.split(g) #this_is_goood_morning
    for i in temp:
       new = new + i[0].lower() + i[1:].upper() +"."
    new =new[:-1]
    print(new)
    tryagin()
def tryagin():
    value=input('give me string => ')
    signe=input('give me sine which base you want to split => ')
    string_modify(value,signe)
tryagin()
def char_occ(s):
    count=0
    c=""
    d={
        count:c
    }
    for i in range(97,123):
        c=chr(i)
        for j in s:
            if c==j:
                count+=1
                print(c)
            else:
                count=0
        print(count)
char_occ("aaksskkfjaaff")
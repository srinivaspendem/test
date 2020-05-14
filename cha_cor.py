def check(str1:str, str2:str)->bool:
    s1=0
    x1=0
    iend=str1.__len__()
    s2=0
    x2=0
    jend=str2.__len__()
    while s1<iend and s2<jend:
        if x1==x2:
            if str1[s1].isalpha() and str2[s2].isalpha():
                if str1[s1]!=str2[s2]:
                    return False

                else:
                    s1+=1
                    s2+=1
                    x1+=1
                    x2+=1

            else:
                if str1[s1].isalpha()==False:
                    x1+=int(str1[s1])
                    s1+=1

                if str2[s2].isalpha()==False:
                    x2+=int(str2[s2])
                    s2+=1
        elif x1<x2:
            if str1[s1].isalpha():
                x1+=1
            else:
                x1+=int(str1[s1])
            s1+=1
        else:
            if str2[s2].isalpha():
                x2+=1
            else:
                x2+=int(str2[s2])
            s2+=1
    return True
x=input("enter two strings :").split()
print (check(x[0],x[1]))
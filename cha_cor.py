def check(str1:str, str2:str)->bool:
    i=0
    ilen=0
    iend=str1.__len__()
    j=0
    jlen=0
    jend=str2.__len__()
    while i<iend and j<jend:
        if ilen==ilen:
            if str1[i].isalpha() and str2[j].isalpha():
                if str1[i]!=str2[j]:
                    return False

                else:
                    i+=1
                    j+=1
                    ilen+=1
                    jlen+=1

            else:
                if str1[i].isalpha()==False:
                    ilen+=int(str1[i])
                    i+=1

                if str2[j].isalpha()==False:
                    ilen+=int(str2[j])
                    i+=1
        elif ilen<jlen:
            if str1[i].isalpha():
                ilen+=1
            else:
                ilen+=int(str1[i])
            i+=1
        else:
            if str2[j].isalpha():
                jlen+=1
            else:
                jlen+=int(str2[j])
            j+=1
    return True
x=input("enter two strings :").split()
print (check(x[0],x[1]))
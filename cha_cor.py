def expand(origStr):
    expStr = ""
    for i in range(len(origStr)):
        ch = origStr[i]
        if ch.isalpha():
            expStr += ch
        else:
            num = int(ch)
            for j in range(num):
                expStr += "?"
    return expStr

def compare(origStr1, origStr2):
    expStr1 = expand(origStr1)
    expStr2 = expand(origStr2)

    if len(expStr1) != len(expStr2):
        return False

    for i in range(len(expStr1)):
        ch1 = expStr1[i]
        ch2 = expStr2[i]

        if (ch1 != '?' and ch2 != '?') and (ch1 != ch2) :
            return False

    return True

print("ap2e & appl1 = ", compare("ap2e", "appl1"))
print("srini2s, 4nivas = ", compare("srini2s", "4nivas"))


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
# x=input("enter two strings :").split()
# print (check(x[0],x[1]))

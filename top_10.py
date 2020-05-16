from urllib.request import urlopen
link = "http://www.gutenberg.org/files/11/11-0.txt"

f=urlopen(link)
byteinput=f.read()
thewholefile=str(byteinput)
thewholefile=thewholefile.replace("."," ",-1)
thewholefile=thewholefile.replace(","," ",-1)
thewholefile=thewholefile.replace("!"," ",-1)
thewholefile=thewholefile.replace('"'," ",-1)
thewholefile=thewholefile.replace("'"," ",-1)
thewholefile=thewholefile.replace("("," ",-1)
thewholefile=thewholefile.replace(")"," ",-1)
thewholefile=thewholefile.replace(":"," ",-1)
thewholefile=thewholefile.replace("\\n"," ",-1)
thewholefile=thewholefile.replace("\\r"," ",-1)
thewholefile=thewholefile.replace("\\t"," ",-1)
thewholefile=thewholefile.replace("\\"," ",-1)
thewholefile=thewholefile.replace("and"," ",-1)
thewholefile=thewholefile.replace("the"," ",-1)
thewholefile=thewholefile.replace("to"," ",-1)
thewholefile=thewholefile.replace("a"," ",-1)
thewholefile=thewholefile.replace("of"," ",-1)
thewholefile=thewholefile.replace("it"," ",-1)
thewholefile=thewholefile.replace("in"," ",-1)
thewholefile=thewholefile.replace("s"," ",-1)
thewholefile=thewholefile.replace("g"," ",-1)
thewholefile=thewholefile.replace("t"," ",-1)
thewholefile=thewholefile.replace("w"," ",-1)
thewholefile=thewholefile.replace("h"," ",-1)
thewholefile=thewholefile.replace("d"," ",-1)
thewholefile=thewholefile.replace("n"," ",-1)
thewholefile=thewholefile.replace("th"," ",-1)



words=thewholefile.split()
counter=dict()

for word in words:
    if (word.isalpha()):
        if (counter.__contains__(word)):
            counter[word]+=1
        else:
            counter[word]=1

valuelist=list()
for key in counter.keys():
    valuelist.append((counter[key],key))
valuelist.sort()

top=valuelist.__len__()
i=0
while i<10:
    i=i+1
    print(valuelist[top-i])


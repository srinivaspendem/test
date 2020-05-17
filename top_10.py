from urllib.request import urlopen
link = "http://www.gutenberg.org/files/11/11-0.txt"

f=urlopen(link)
byteinput=f.read()
thewholefile=str(byteinput)
thewholefile.replace("the","",-1)
words=thewholefile.split()

counter=dict()

tuple(counter)
for word in words:
    if (word.isalpha()):
        if (counter.__contains__(word)):
            counter[word]+=1
        else:
            counter[word]=1

del counter['the']
del counter['to']
del counter['and']
del counter['a']
del counter['of']
del counter['in']
del counter['it']
valuelist=list()
for key in counter.keys():
    valuelist.append((counter[key],key))
valuelist.sort()

top=valuelist.__len__()
i=0
while i<10:
    i=i+1
    print(valuelist[top-i])


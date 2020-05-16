from urllib.request import urlopen

link = "http://www.gutenberg.org/files/11/11-0.txt"

f = urlopen(link)
byteinput=f.read()
thewholefile=str(byteinput)
words=thewholefile.split()
for i in range(0,10):
   words.remove("of")
   words.remove("in")
   words.remove("by")
   words.remove("the")
   print(words[i])

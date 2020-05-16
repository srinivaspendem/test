from urllib.request import urlopen
from collections import Counter 

link = "http://www.gutenberg.org/files/11/11-0.txt"

f = urlopen(link)
byteinput=f.read()
thewholefile=str(byteinput)
data_set=thewholefile.split()
split_it = data_set.split()  
Counter = Counter(split_it) 
most_occur = Counter.most_common(4) 
print(most_occur) 



#for i in range(0,10):
 #  words.remove("of")
  # words.remove("in")
   #words.remove("by")
   #words.remove("the")
   #print(words[i])

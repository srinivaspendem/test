from urllib.request import urlopen
from collections import Counter 

link = "http://www.gutenberg.org/files/11/11-0.txt"

f = urlopen(link)
byteinput=f.read()
thewholefile=str(byteinput)
data_set=thewholefile.split()  

most_occur = data_set.most_common(4) 
print(most_occur) 




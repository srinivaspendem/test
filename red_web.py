from urllib.request import urlopen

link = "http://www.gutenberg.org/files/11/11-0.txt"

f = urlopen(link)
myfile = f.read()
print(myfile)

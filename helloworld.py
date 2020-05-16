f= open("filename.ext", "r") # open the file in readonly mode
lines = [] # create an empty list to store the lines in the file

for line in f:
    lines.append(line) # loop over the lines in the file and store them in the lines list

for line in lines:
    words_in_line = line.split() # create a list of the words in each line
    print(word_in_line[0], words_in_line[-1]) # print out the 1st and last word of each line


f = open("filename.ext", "r")

for line in f:
    words = line.split()
    print(words[0], words[-1])
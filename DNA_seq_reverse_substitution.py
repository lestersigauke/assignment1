string = raw_input("Please enter your DNA sequence: ")
stringlist = []
letter = ""
for i in range(0,(len(string))):
    letter = string[i]
    if letter == 't' or letter == 'T':
        letter = 'U'
    stringlist.append(letter) 
    
stringlist.reverse()
print "The reversed DNA sequence is ", stringlist
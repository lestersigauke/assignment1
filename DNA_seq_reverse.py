string = raw_input("Please enter your DNA sequence: ")
stringlist = []
for i in range(0,(len(string))):
    stringlist.append(string[i]) 
    
stringlist.reverse()
print "The reversed DNA sequence is ", stringlist
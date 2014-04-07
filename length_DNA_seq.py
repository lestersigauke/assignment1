DNAseq = raw_input("Enter DNA sequence: ")
totallength = len(DNAseq)
counter = 1
average = 0

while DNAseq != "":
    counter = counter+1
    totallength = totallength + len(DNAseq)
    DNAseq = raw_input("Enter third DNA sequence set: ")
    
average = totallength/counter    
print "The average length of the DNA sequences you entered is", average

sequence = raw_input("Enter your DNA sequence: ")

if len(sequence) > 6:
    print "First 3 nucleotides", sequence[:3]
    print "Last 3 nucleotides", sequence[-3:]
else:
    print "Inappropriate sequence entered."
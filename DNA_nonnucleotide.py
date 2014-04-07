sequence = raw_input("Enter your DNA sequence: ")
sequence = sequence.upper()
count = 0
match = 0
for i in range(0,len(sequence)):
    if sequence[i] == 'A':
        match = match + 1
        continue
    if sequence[i] == 'C':
        match = match + 1
        continue    
    if sequence[i] == 'G':
        match = match + 1
        continue    
    if sequence[i] == 'T':
        match = match + 1
        continue    
    
    else:
        count = count + 1 
print count
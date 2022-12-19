import csv 

# binary files can only be opened by programs that understand their structure 
# Text files can be opened in Python (html, CSS, JSON, c, java, csv, tsv)

with open('vgsales.csv', 'r') as file: #read the file 
    fieldnames = ['Rank','Name'] # give the fieldnames to use
    reader = csv.DictReader(file, fieldnames=fieldnames) # reader is an iterator
    # can also use csv.reader(file)   
    next(file) # skips the first index

    i = 0
    for line in file:    
        if i < 1:  
            print(line) 
            i += 1


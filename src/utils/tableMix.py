a = "comparation_table_16.csv"
b = "comparation_table_GSPH_36.csv"

import csv

endcsv = ""

def addGSPH(instance):
    with open("comparation_table_GSPH_36.csv", newline='\n')as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')    
        
        for row in spamreader:
            if(row[0] == instance):
                repo = row[1]
                tiempo = row[-1]
                dist = row[2]
                bks = row[3]
                gap = row[4]
                return f'{instance};{repo};{dist};{bks};{gap};{tiempo}\n'


with open(a) as file:

    spamreader = file.read()
    curr = 0
    for i in spamreader.split('\n'):
        endcsv +=i + '\n'
        if(curr % 8 == 0 and curr != 0):
            endcsv +=addGSPH(i.split(';')[0])
        curr+=1


print(endcsv)

with open("mix.csv","w") as file:
    file.write(endcsv)
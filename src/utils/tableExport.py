
import csv

import sys
file = "comparation_table_16.csv"

line = 0

def getTitle(instance):
    lts = "\\begin{table}[H]\n"
    lts += "\\centering\n"
    lts += "\\caption{Resultados para la instancia " + instance + "}\n"
    lts += "\\begin{tabular}{|l|c|c|c|c|}\n"
    lts += "\\hline\n"
    lts += "\\textbf{Repositorio} & \\textbf{Tiempo (s)} & \\textbf{Distancia} & \\textbf{BKS} & \\textbf{GAPBKS} \\\\ \n"
    lts += "\\hline\n"
    return lts

def closeLatex ():
    lts = "\\hline\n"
    lts += "\\end{tabular}\n"
    lts += "\\end{table}\n"
    return lts


def addGSPH(instance):
    with open("comparation_table_GSPH_36.csv", newline='\n')as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')    
        
        for row in spamreader:
            if(row[0] == instance):
                repo = row[1]
                tiempo = round(float(row[-1]),4)
                dist = round(float(row[2]),None)
                bks = row[3]
                gap = round(float(row[4]),1)                
                return f'{repo} & {tiempo} & {dist} & {bks} & {gap}\\% ' + '\\\\ \n'
                 

with open(file, newline='\n') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
  
    intances = []
    algos = 7
    index = 0

    latex = []
    tmpLatex = ""
    for row in spamreader:
        if(line == 0):
            line+=1
            continue

        current_instance = row[0]
        if(current_instance not in tmpLatex):
            tmpLatex += getTitle(current_instance)
        

        repo = row[1]
        tiempo = round(float(row[-1]),4)
        dist = round(float(row[2]),None)
        bks = row[3]
        gap = round(float(row[4]),1)
        
        tmpLatex += f'{repo} & {tiempo} & {dist} & {bks} & {gap}\\% ' + '\\\\ \n'
        #print(tmpLatex)
        if(index >= algos):
            #Agregar GSPH
            tmpLatex+=addGSPH(current_instance)
            tmpLatex+=closeLatex()
            latex.append(tmpLatex)
            tmpLatex=""
            
            index = -1
        index += 1

j = 0

print(latex[0])

for i in latex:

    table = open(f"tables/instance-{j}.tex",'w')

    table.write(i)
    table.close()
    j+=1
"""

with open(file) as csvFile:
    text = csvFile.read()
    nlines = text.split("\n")
    
    for i in nlines:
        vales = i.split(';')
        indexx = 0
        for j in vales:
            latex += f"{j} & " if indexx < 5 else f"{j} \n"
            indexx+=1
            print(indexx)
    
        
print(latex)

with open("out.tex",'w') as files:
    files.write(latex)"""

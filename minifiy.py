from sys import argv,exit
from os import listdir

dirs = listdir()
file_to_minify = argv[1]

if not file_to_minify in dirs:
    exit(f"il file '{file_to_minify}' non esiste in questa cartella")

html = open(file_to_minify, "r")

minified = ""
for riga in html.readlines():
    minified += riga.strip()

html.close()    

try:
    with open("minified.html","w") as minify_file:
        minify_file.write(minified)
        minify_file.close()
        print(f"{file_to_minify} minificato con successo")
except:
    print('errore durante il minfy')
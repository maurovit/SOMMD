import csv
import os

# Directory contenete il dataset delle immagini
DIRECTORY_DATASET = ""

# Path file csv delle label
DIRECTORY_CSV = ""

# Apriamo il file csv
with open(DIRECTORY_CSV, mode="r") as csv_file:

    # Costruiamo il reader
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    for row in csv_reader:

        # Ignoriamo la prima riga perché relativa al nome delle colonne
        if (line_count == 0):
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:

            # Controlliamo se ci troviamo in una riga (e quindi immagine) da cancellare
            if(row[2] == "akiec" or row[2] == "bcc" or row[2] == "vasc"):
                try:

                    # Cancelliamo l'immagine
                    os.remove(DIRECTORY_DATASET + row[1] + ".jpg")
                    
                except: pass



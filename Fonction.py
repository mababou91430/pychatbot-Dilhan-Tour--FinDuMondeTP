import os


def nom_president():
    L = []
    remplacement = "'!?123456789"
    for filename in os.listdir("speeches-20231124"):
        for i in range(len(remplacement)):
            filename = filename.replace(remplacement[i], "")
        filename = filename.replace("Nomination_", "")
        filename = filename.replace(".txt", "")
        if filename not in L:
            if filename == "Hollande":
                filename = " François" +" "+ filename
                L.append(filename)

            if filename == "Chirac":
                filename = " Jacques" +" "+ filename
                L.append(filename)

            if filename == "Sarkozy":
                filename = " Nicolas" +" "+ filename
                L.append(filename)

            if filename == "Giscard dEstaing":
                filename = " Valéry" +" "+ filename
                L.append(filename)

            if filename == "Mitterant":
                filename = " François" +" "+ filename
                L.append(filename)

            if filename == "Macron":
                filename = " Emmanuel" +" "+ filename
                L.append(filename)
    return L


print(nom_president())

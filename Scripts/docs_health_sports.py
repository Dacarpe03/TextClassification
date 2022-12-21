import os


dani = ["Salud", "Deportes"]
path = "/Users/joelpardo/Desktop/Practica 2/Documentos/"
for z in dani:

    p = path + z

    documentos = os.listdir(p)
    documentos = [t for t in documentos if t != '.DS_Store']

    for i in documentos:

        original = p + "/" + i

        n = i.split("_")
        
        cambiado = p + "/" + n[1]

        # print(original + ":" + cambiado)

        os.rename(original, cambiado)
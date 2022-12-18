import os
    
clases = ["Ciencia", "Politica"]

for z in clases:
    # Introducimos el nombre de la clase y donde queremos que se guarden los documentos '.txt'
    path = "/Users/joelpardo/Desktop/Practica 2/Documentos/" + z + "/"
    path_guardado = path + "txt"
    path_titulo = path + "titulo"

    carpetas = os.listdir(path)

    # Creamos los path de las carpetas (documentos)
    for i in range(1, 61):
        if str(i) not in carpetas:
            os.mkdir(path + str(i))

    if "txt" not in carpetas:
        os.mkdir(path_guardado)

    if "titulo" not in carpetas:
        os.mkdir(path_titulo)

# /Users/joelpardo/Desktop/Practica 2 /Documentos/Ciencia
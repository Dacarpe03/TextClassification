import pytesseract
from PIL import Image
import os 
import shutil

# https://coffeebytes.dev/ocr-con-tesseract-python-y-pytesseract/


clases = ["Ciencia", "Politica"]

# Ciencia:
# - El Pais
# - ABC
# - El confidencial

# Politica:
# - 20 minutos
# - El Pais
# - El diario



for z in clases: 
    # Introducimos el nombre de la clase y donde queremos que se guarden los documentos '.txt'
    path = "/Users/joelpardo/Desktop/Practica 2/Documentos/" + z + "/"
    path_guardado = path + "txt/"
    path_titulo = path + "titulo/"


    # Listamos todos los documentos para esta clase
    carpetas = os.listdir(path)
    # print(carpetas) # '.DS_Store'
    # print(len(carpetas)) # '.DS_Store'

    # Eliminamos la carpeta de guardado y '.DS_Store'
    carpetas = [c for c in carpetas if c != '.DS_Store' and c != 'txt' and c != 'titulo']
    # print(len(carpetas)) # '.DS_Store'

    # Creamos las rutas de cada uno de los documentos
    rutas = []
    for i in carpetas:
        # if i != '.DS_Store' and i != 'txt':
        rutas.append(path + i + "/")

    # # print(rutas)
    # # print(len(rutas))



    # NOTA: Las carpetas y las rutas coinciden en orden

    # Para los documentos y las rutas
    for c, j in zip(carpetas, rutas):
        
        # Sacamos las imagenes por cada documento
        imagenes = os.listdir(j)
        
        # Copiamos el archivo que contiene un titulo a la carpeta de titulos
        shutil.copy(j + "1.png", path_titulo + str(c)+ ".png")

        # Inicializamos lista a vacia. Sirve para guardar el texto de un mismo documento
        texto = []

        # Para cada una de las imagenes 
        for h in imagenes:
            if h != '.DS_Store':
                # Cargo la imagen
                img = Image.open(j + h) # Abre la imagen con pillow
                img.load()

                # Saco el texto
                text = pytesseract.image_to_string(img, lang='spa') # Extrae el texto de la imagen
                # print(text)
                texto.append(text)


        # Guardo el documento '.txt' en la carpeta de guardado
        f = open (path_guardado+str(c)+".txt" ,'w')
        f.writelines(texto)
        f.close()

        print(c)



    # Sacamos los doscumentos exitentes en el path de guardado para comprobar que estan todos
    documentos = os.listdir(path_guardado)
    print(len(documentos))

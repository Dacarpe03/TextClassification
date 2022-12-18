import pandas as pd
import pytesseract
from PIL import Image
import os 

# Cargamos el registro
df = pd.read_excel("/Users/joelpardo/Desktop/Practica 2/Documentos/urls1.xlsx")
# print(df)


# Asignamos las variables
indices = df["Unnamed: 0"].tolist()
category = df["category"].tolist()
title = df["title"].tolist()
links = df["link"].tolist()


generico = "/Users/joelpardo/Desktop/Practica 2/Documentos"
path = generico + "/Links"


clases = ["Ciencia", "Politica"]
contador = indices[len(indices)-1] # 119

for z in clases:

    doc = path + "/" + str(z) + '.txt'

    path_titulos = generico + "/" + str(z) + "/titulo"
    
    
    titulos = os.listdir(path_titulos)
    titulos = [f for f in titulos if f != ".DS_Store"]


    with open(doc,'r') as f:
        lin = f.readlines()
        c = 0

        for i in lin:
            if i != "\n":
                if z == "Ciencia":
                    clase = "science"
                    category.append(clase)

                if z == "Politica":
                    clase = "politics"
                    category.append(clase)

                print(c)
                # Cargo la imagen
                img = Image.open(path_titulos + "/" + titulos[c]) # Abre la imagen con pillow
                img.load()
            

                # Saco el texto
                text = pytesseract.image_to_string(img, lang='spa') # Extrae el texto de la imagen
                # print(text)
                # text = text.strip('\n')
                text = text.replace('\n', '')
                title.append(text.strip())
                c += 1

                # title.append("")
                
                new_string = i.replace('\n', '')
                links.append(new_string.strip())


                contador += 1
                indices.append(contador)
            

print(len(indices))
print(len(category))
print(len(title))
print(len(links))



# print(title)



df_new = pd.DataFrame()

df_new["index"] = indices
df_new["category"] = category


path_rutas = "./Datos/Raw_data" #./TextClassification/

clases2 = df_new["category"].unique().tolist() #0-3

rutas_docs = []
r = []
for h in clases2:
    for a in range(1,61):
        p = path_rutas+ "/" + h + "/" + str(a) + ".txt"
        rutas_docs.append(p)
        r.append(a)

df_new["n_doc"] = r
df_new["title"] = title
df_new["path"] = rutas_docs
df_new["link"] = links

df_new.to_csv('/Users/joelpardo/Desktop/Practica 2/Documentos/urls.csv', header=True, index=False)





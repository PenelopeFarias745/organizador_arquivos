import os

path = "C:/Users/penel/OneDrive/Documentos/CODIGOS/modulo7/aula1/capivara.jpg"

root, extension = os.path.splitext(path)

print("Caminho da root:", root)
print("Caminho da extensão:", extension)


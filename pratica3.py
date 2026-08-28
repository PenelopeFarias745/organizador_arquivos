import os
import shutil

path = "C:/Users/penel/OneDrive/Documentos/CODIGOS/modulo7/aula1/pasta-template"

print("Antes de copiar o arquivo")
print(os.listdir(path))

source = "C:/Users/penel/OneDrive/Documentos/CODIGOS/modulo7/aula1/pasta-template/time.jfif"

destination = "C:/Users/penel/OneDrive/Documentos/CODIGOS/modulo7/aula1/pasta-template/copia-time.jfif"

dest = shutil.copy(source, destination)

print("Após copiar o arquivo:")
print(os.listdir(path))
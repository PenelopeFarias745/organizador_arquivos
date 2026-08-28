import os

print(dir(os))

print(os.getcwd())

# os.mkdir("teste") 

print(os.listdir())

path = "C:/Users/penel/OneDrive/Documentos/CODIGOS/modulo7/aula1/capivara.jpg"
path_error = "C:/Users/penel/OneDrive/Documentos/CODIGOS/modulo7/aula1/capibara2.jpg"

isExist = os.path.exists(path)
print(isExist)

notExist = os.path.exists(path_error)
print(notExist)
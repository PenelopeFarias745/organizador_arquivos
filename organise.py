import os
import shutil

from_dir = "C:/Users/penel/OneDrive/Documentos/CODIGOS/modulo7/aula1/pasta-template"
to_dir = "C:/Users/penel/OneDrive/Documentos/CODIGOS/modulo7/aula1"

list_of_files = os.listdir(from_dir)
# print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    # print(name)
    # print(extension)
    if extension == "":
        continue
    if extension in [".gif", ".png", ".jgp", ".jfif", ".webp", ".jpeg"]:
        path1 = from_dir + "/" + file_name
        path2 = to_dir + "/" + "pasta-organizada"
        path3 = to_dir + "/" + "pasta-organizada" + "/" + file_name
        print("path1", path1)
        print("path3", path3)

        if os.path.exists(path2):
            print("Movendo " + file_name + ".....")
            shutil.move(path1, path3)
        else:
            os.makedir(path2)
            print("Movendo "+ file_name + ".....")
            shutil.move(path1, path3)
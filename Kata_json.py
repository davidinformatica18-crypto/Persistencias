import json

def read(file_path):

    with open(file_path, "r") as archivo: # Abrimos el archivo en modo lectura ("r")

        return json.load(archivo)


def write(file_path, content):

    with open(file_path, "w") as archivo:  # Abrimos el archivo en modo escritura ("w")

        json.dump(content, archivo)


def update(file_path, content):

    with open(file_path, "w") as archivo:  # En esta kata, update hace lo mismo que write:

        json.dump(content, archivo)


def clear(file_path):

    with open(file_path, "w") as archivo:  # Abrimos el archivo en modo escritura

        json.dump({}, archivo)


def delete(file_path):   # Importamos os para poder borrar archivos del sistema

    json.dumo({},archivo)
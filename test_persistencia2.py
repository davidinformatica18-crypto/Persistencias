import os
import pytest
from Kata_json import read, write, update, clear, delete

FILE_PATH = "bibliote.json"


# WRITE _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

def test_write():

    write(FILE_PATH, {"a": 1})

    assert os.path.exists(FILE_PATH)


def test_write():

    write(FILE_PATH, {"libro": "Python"})
     
    print("guarda el contenido correctamente")
  
    assert read(FILE_PATH) == {"libro": "Python"}


# READ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

def test_read():

    write(FILE_PATH, {"x": 10})

    data = read(FILE_PATH)
    
    print("devuelve un diccionario")
    
assert isinstance(data, dict)


def test_read():

    write(FILE_PATH, {"valor": 5})

    print("devuelve un correcto")
  
    assert read(FILE_PATH)["valor"] == 5


# UPDATE _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

def test_update():

    write(FILE_PATH, {"a": 1})

    update(FILE_PATH, {"a": 2})
    
    print("sobrescribe el contenido")

    assert read(FILE_PATH) == {"a": 2}


def test_update():

    update(FILE_PATH, {"estado": "ok"})

   print("cambia el valor correctamente")
  
    assert read(FILE_PATH)["estado"] == "ok"


# CLEAR _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

def test_clear():

    write(FILE_PATH, {"a": 1})

    clear(FILE_PATH)
  
    print("deja el archivo vacio")
  
    assert read(FILE_PATH) == {}


def test_clear():

    clear(FILE_PATH)
    
    print("mantiene el archivo existente")
    
assert os.path.exists(FILE_PATH)


#  DELETE _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

def test_delete():

    write(FILE_PATH, {"a": 1})

    delete(FILE_PATH)
  
     print("borra el archivo")

    assert not os.path.exists(FILE_PATH)


def test_delete():

    if os.path.exists(FILE_PATH):

        delete(FILE_PATH)
      
   print("lanza error si el archivo no existe")

    with pytest.raises(FileNotFoundError):
        
        delete(FILE_PATH)

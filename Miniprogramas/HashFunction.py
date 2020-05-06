# Con el siguiente scripts obtendremos el hash SHA-1 del objeto introducido.
# Las funciones has toman una cantidad de valores arbitraria de datos y devuelven una cadena de bits de una lonjitud fija.

import   hashlib


def hashFile(filename):
    # Utilizaremos el algoritmo hash SHA-1, que tiene 160 bits de longitud
    h = hashlib.sha1()
    
    # Abrirmos el archivo en modo "Read Binary"
    with open (filename,'rb') as file:
        chunk = 0
        while chunk != b'':
            # Por cada iteracion leemos 1024 bytes
            chunk = file.read (1024)
            h.update(chunk)

    # Devolvemos el mensaje resumen en hexadecimal
    return h.hexdigest()

message = hashFile("Logo.ico")
print(message)


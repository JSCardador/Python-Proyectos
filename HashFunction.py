import   hashlib

def hashFile(filename):
    h = hashlib.sha1()
    
    with open (filename,'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read (1024)
            h.update(chunk)

    return h.hexdigest()

message = hashFile("Logo.ico")
print(message)

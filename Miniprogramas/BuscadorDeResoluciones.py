# Este Script imprime la resolucion de una imagen jpg

def ResolutionIMG(File):
    with open(File, 'rb') as img_file:
        img_file.seek(163)
        a = img_file.read(2)
        height = (a[0] << 8) +a[1]

        a = img_file.read(2)
        width = (a[0] << 8) + a[1]

    print(f"La resolucion de {File} es de {width} x {height}")

ResolutionIMG("Nombre.jpg")
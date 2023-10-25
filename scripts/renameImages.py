import os

# Obtiene la ruta de la carpeta actual
ruta_carpeta = os.path.dirname(os.path.abspath(__file__))

# Lista todos los archivos en la carpeta
archivos = os.listdir(ruta_carpeta)

# Filtra solo los archivos de imagen (puedes cambiar las extensiones según tus archivos)
archivos_de_imagen = [archivo for archivo in archivos if archivo.lower().endswith(('.jpg', '.png', '.jpeg', '.gif'))]

# Itera a través de los archivos de imagen y renombra cada archivo
for indice, archivo in enumerate(archivos_de_imagen, start=1):
    # Genera el nuevo nombre del archivo
    nuevo_nombre = f'Poliporo_UK_{indice}{os.path.splitext(archivo)[1]}'  # Conserva la extensión del archivo
    
    # Ruta completa del archivo antiguo y nuevo
    ruta_antigua = os.path.join(ruta_carpeta, archivo)
    ruta_nueva = os.path.join(ruta_carpeta, nuevo_nombre)
    
    # Renombra el archivo
    os.rename(ruta_antigua, ruta_nueva)

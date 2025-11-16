import os
import shutil
import subprocess

# Ruta de la carpeta que quieres copiar
carpeta_origen = r"R:\Shared\Operation\Public\Ingenieria\IoT Systems\Sistema de Inspeccion\Revision actual"
nombre_carpeta_destino = "Revision actual"

# Ruta al escritorio del usuario
escritorio = os.path.join(os.path.expanduser("~"), "Desktop")
carpeta_destino = os.path.join(escritorio, nombre_carpeta_destino)

# Verificar si la carpeta origen existe
if os.path.exists(carpeta_origen):
    try:
        shutil.copytree(carpeta_origen, carpeta_destino)
        print(f"Carpeta copiada en: {carpeta_destino}")
    except FileExistsError:
        print("La carpeta ya existe en el escritorio. Usando la existente.")
else:
    if os.path.exists(carpeta_destino):
        print("No se encontró la carpeta origen, pero ya existe en el escritorio.")
    else:
        print("Error: No se encontró la carpeta origen ni una copia en el escritorio.")
        exit()

# Ruta del ejecutable dentro de la carpeta copiada
ejecutable = os.path.join(carpeta_destino, "Sistema de Captura de Inspeccion.exe")

# Ejecutar el archivo si existe
if os.path.exists(ejecutable):
    try:
        subprocess.Popen(ejecutable)
        print("Ejecutable lanzado correctamente.")
    except Exception as e:
        print(f"Error al ejecutar el archivo: {e}")
else:
    print(f"Error: No se encontró el ejecutable en {ejecutable}")
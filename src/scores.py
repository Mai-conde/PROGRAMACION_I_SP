import json
import os  
def cargar_puntajes()-> list:
    """
    Carga los puntajes guardados desde el archivo JSON.

    Returns:
        list: Lista de diccionarios con los puntajes guardados.
    """
    archivo = "PROGRAMACION_I_SP/data/scores.json"
    datos = []
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            contenido = f.read()
            if contenido.strip() != "":
                datos = json.loads(contenido)
    return datos
def guardar_puntaje(nombre: str, puntaje: int) -> None:
    """
    Guarda un nuevo puntaje en el archivo JSON, manteniendo solo los 3 mejores.

    Args:
        nombre (str): Nombre del jugador.
        puntaje (int): Puntaje obtenido.
    """
    archivo = "PROGRAMACION_I_SP/data/scores.json"
    datos = []
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            contenido = f.read()
            if contenido.strip() != "":
                datos = json.loads(contenido)
    datos.append({"nombre": nombre, "puntaje": puntaje})


    for i in range(len(datos)):
        for j in range(i + 1, len(datos)):
            if datos[j]["puntaje"] > datos[i]["puntaje"]:
                temp = datos[i]
                datos[i] = datos[j]
                datos[j] = temp

    datos = datos[:3]

    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)
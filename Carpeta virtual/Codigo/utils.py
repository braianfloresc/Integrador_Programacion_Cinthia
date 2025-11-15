import csv

def leer_csv(nombre_archivo):
    paises = []
    try:
        with open(nombre_archivo, newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    pais = {
                        "nombre": fila["nombre"],
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"]
                    }
                    paises.append(pais)
                except:
                    print(" Error, se omitió un país.")
        print("Archivo cargado correctamente")
    except FileNotFoundError:
        print(" No se encontró el archivo CSV")
    return paises


def mostrar_lista(paises):
    for p in paises:
        print(f"{p['nombre']} - {p['poblacion']} hab. - {p['superficie']} km² - {p['continente']}")

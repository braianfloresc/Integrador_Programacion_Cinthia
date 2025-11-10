import os
#print("Carpeta actual:", os.getcwd())

import csv

# ---------------- FUNCIONES ----------------

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
                    print(" Error, se omitio un pais.")
        print("Archivo cargado correctamente")
    except FileNotFoundError:
        print(" No se encontro el archivo CSV")
    return paises


def buscar_pais(paises, nombre):
    encontrados = []
    for pais in paises:
        if nombre.lower() in pais["nombre"].lower():
            encontrados.append(pais)
    return encontrados


def filtrar_por_continente(paises, continente):
    return [p for p in paises if p["continente"].lower() == continente.lower()]


def filtrar_por_poblacion(paises, min_pob, max_pob):
    return [p for p in paises if min_pob <= p["poblacion"] <= max_pob]


def filtrar_por_superficie(paises, min_sup, max_sup):
    return [p for p in paises if min_sup <= p["superficie"] <= max_sup]


def ordenar_paises(paises, clave, descendente=False):
    return sorted(paises, key=lambda x: x[clave], reverse=descendente)


def mostrar_estadisticas(paises):
    if not paises:
        print("No hay datos para mostrar")
        return

    mayor_pob = max(paises, key=lambda x: x["poblacion"])
    menor_pob = min(paises, key=lambda x: x["poblacion"])
    prom_pob = sum(p["poblacion"] for p in paises) / len(paises)
    prom_sup = sum(p["superficie"] for p in paises) / len(paises)

    print("\n--- ESTADÍSTICAS ---")
    print("Pais con mayor poblacion:", mayor_pob["nombre"], "-", mayor_pob["poblacion"])
    print("Pais con menor poblacion:", menor_pob["nombre"], "-", menor_pob["poblacion"])
    print("Promedio de poblacion:", round(prom_pob, 2))
    print("Promedio de superficie:", round(prom_sup, 2))

    # cantidad de países por continente
    continentes = {}
    for p in paises:
        cont = p["continente"]
        continentes[cont] = continentes.get(cont, 0) + 1

    print("\nCantidad de países por continente:")
    for c, cant in continentes.items():
        print(f"{c}: {cant}")


def mostrar_lista(paises):
    for p in paises:
        print(f"{p['nombre']} - {p['poblacion']} hab. - {p['superficie']} km² - {p['continente']}")

# ---------------- PROGRAMA PRINCIPAL ----------------

def main():
    paises = leer_csv(r"C:\Users\santi\Desktop\Programacion1\Trabajo en clase\paises.csv")

    if not paises:
        return

    opcion = 0
    while opcion != 7:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Buscar pais por nombre")
        print("2. Filtrar por continente")
        print("3. Filtrar por rango de poblacion")
        print("4. Filtrar por rango de superficie")
        print("5. Ordenar países")
        print("6. Mostrar estadísticas")
        print("7. Salir")

        try:
            opcion = int(input("Elija una opción: "))
        except:
            print("Debe ingresar un numero")
            continue

        if opcion == 1:
            nombre = input("Ingrese nombre o parte del nombre: ")
            resultado = buscar_pais(paises, nombre)
            if resultado:
                mostrar_lista(resultado)
            else:
                print("No se encontraron paises con ese nombre")

        elif opcion == 2:
            cont = input("Ingrese continente: ")
            resultado = filtrar_por_continente(paises, cont)
            mostrar_lista(resultado)

        elif opcion == 3:
            try:
                min_p = int(input("Población mínima: "))
                max_p = int(input("Población máxima: "))
                resultado = filtrar_por_poblacion(paises, min_p, max_p)
                mostrar_lista(resultado)
            except:
                print("Error, ingrese valores numericos")

        elif opcion == 4:
            try:
                min_s = int(input("Superficie minima: "))
                max_s = int(input("Superficie máxima: "))
                resultado = filtrar_por_superficie(paises, min_s, max_s)
                mostrar_lista(resultado)
            except:
                print("Error, ingrese valores numericos")

        elif opcion == 5:
            print("\n1. Por nombre\n2. Por población\n3. Por superficie")
            op2 = input("Elija tipo de orden: ")
            desc = input("¿Descendente? (s/n): ").lower() == "s"

            if op2 == "1":
                ordenados = ordenar_paises(paises, "nombre", desc)
            elif op2 == "2":
                ordenados = ordenar_paises(paises, "poblacion", desc)
            elif op2 == "3":
                ordenados = ordenar_paises(paises, "superficie", desc)
            else:
                print("Opcion no valida")
                continue
            mostrar_lista(ordenados)

        elif opcion == 6:
            mostrar_estadisticas(paises)

        elif opcion == 7:
            print("cerrando programa")
        else:
            print("Opcion no valida")

# ---------------- EJECUCION ----------------

if __name__ == "__main__":
    main()


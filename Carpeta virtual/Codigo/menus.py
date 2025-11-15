from crud_paises import (
    buscar_pais,
    filtrar_por_continente,
    filtrar_por_poblacion,
    filtrar_por_superficie,
    ordenar_paises,
    mostrar_estadisticas
)
from utils import mostrar_lista


def menu_principal(paises):
    opcion = 0

    while opcion != 7:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Buscar país por nombre")
        print("2. Filtrar por continente")
        print("3. Filtrar por rango de población")
        print("4. Filtrar por rango de superficie")
        print("5. Ordenar países")
        print("6. Mostrar estadísticas")
        print("7. Salir")

        try:
            opcion = int(input("Elija una opción: "))
        except:
            print("Debe ingresar un número")
            continue

        if opcion == 1:
            nombre = input("Ingrese nombre o parte del nombre: ")
            resultado = buscar_pais(paises, nombre)
            mostrar_lista(resultado) if resultado else print("No se encontraron países")

        elif opcion == 2:
            cont = input("Ingrese continente: ")
            mostrar_lista(filtrar_por_continente(paises, cont))

        elif opcion == 3:
            try:
                min_p = int(input("Población mínima: "))
                max_p = int(input("Población máxima: "))
                mostrar_lista(filtrar_por_poblacion(paises, min_p, max_p))
            except:
                print("Error, ingrese valores numéricos")

        elif opcion == 4:
            try:
                min_s = int(input("Superficie mínima: "))
                max_s = int(input("Superficie máxima: "))
                mostrar_lista(filtrar_por_superficie(paises, min_s, max_s))
            except:
                print("Error, ingrese valores numéricos")

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
                print("Opción no válida")
                continue

            mostrar_lista(ordenados)

        elif opcion == 6:
            mostrar_estadisticas(paises)

        elif opcion == 7:
            print("Cerrando programa")
        else:
            print("Opción no válida")

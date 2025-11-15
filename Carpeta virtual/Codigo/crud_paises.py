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

    continentes = {}
    for p in paises:
        cont = p["continente"]
        continentes[cont] = continentes.get(cont, 0) + 1

    print("\nCantidad de países por continente:")
    for c, cant in continentes.items():
        print(f"{c}: {cant}")

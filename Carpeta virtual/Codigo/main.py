from utils import leer_csv
from menus import menu_principal

def main():
    nombre_archivo = "paises.csv"   # Se carga el CSV directamente sin ruta

    paises = leer_csv(nombre_archivo)

    if not paises:
        return

    menu_principal(paises)


if __name__ == "__main__":
    main()

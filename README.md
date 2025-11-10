#  Programa de Gestión de Países

## 🧾 Descripción del programa

Este programa en **Python** permite leer datos de un archivo CSV que contiene información sobre países del mundo (nombre, población, superficie y continente).  
A partir de esos datos, el usuario puede realizar diferentes operaciones como:

- Buscar países por nombre.  
- Filtrar por continente.  
- Filtrar por rango de población o superficie.  
- Ordenar los países según distintos criterios.  
- Mostrar estadísticas generales (promedios, país con mayor/menor población, cantidad por continente).

Está diseñado para practicar **lectura de archivos CSV**, **estructuras de datos**, **funciones**, **filtrado y ordenamiento**, y **manejo de errores**.

---

## ⚙️ Instrucciones de uso

1. **Preparar el archivo CSV**
   - Debes tener un archivo llamado `paises.csv` con el siguiente formato (encabezados incluidos):

     ```csv
     nombre,poblacion,superficie,continente
     Argentina,45376763,2780400,América
     Francia,65273511,551695,Europa
     Japón,125800000,377975,Asia
     ```

   - Guarda el archivo en la misma carpeta del script o actualiza la ruta dentro del código:
     ```python
     paises = leer_csv(r"C:\ruta\del\archivo\paises.csv")
     ```

2. **Ejecutar el programa**
   - Abre una terminal o usa Visual Studio Code.
   - Ejecuta el programa con:
     ```bash
     python nombre_del_archivo.py
     ```

3. **Usar el menú principal**
   El programa mostrará un menú con las siguientes opciones:
Buscar país por nombre

Filtrar por continente

Filtrar por rango de población

Filtrar por rango de superficie

Ordenar países

Mostrar estadísticas

Salir


---

##  Ejemplos de uso

### Ejemplo 1 – Buscar país
**Entrada:**
1
Ingrese nombre o parte del nombre: arg

**Salida:**
Argentina - 45376763 hab. - 2780400 km² - América

---

###  Ejemplo 2 – Filtrar por continente
**Entrada:**
2
Ingrese continente: Europa

**Salida:**
Francia - 65273511 hab. - 551695 km² - Europa
Alemania - 83783942 hab. - 357022 km² - Europa

---

###  Ejemplo 3 – Mostrar estadísticas
**Entrada:**
6

**Salida:**
--- ESTADÍSTICAS ---
País con mayor población: China - 1409517397
País con menor población: Uruguay - 3473727
Promedio de población: 230467823.45
Promedio de superficie: 692731.18

Cantidad de países por continente:
América: 12
Europa: 8
Asia: 10
África: 9
Oceanía: 5

---

## 👥 Participación de los integrantes

| Integrante | Rol / Aporte principal |
|-------------|------------------------|
| **Santino Naldini** | Desarrollo de funciones de lectura y filtrado, manejo de errores. |
| **Braian Flores** | Diseño del menú, ordenamiento y estadísticas, documentación y pruebas. |

---

##  Notas adicionales

- Asegúrate de que el archivo CSV esté codificado en **UTF-8** para evitar errores con tildes o caracteres especiales.  
- Puedes modificar la ruta del archivo CSV según tu ubicación local.  
- El programa maneja errores comunes como:
  - Archivo inexistente.
  - Campos vacíos o no numéricos.
  - Entradas incorrectas del usuario.




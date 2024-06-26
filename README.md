﻿# Instrucciones de Uso

Este script está diseñado para crear una base de datos MySQL a partir de un archivo CSV de localidades, así como generar archivos CSV separados por provincia.

## Requisitos

- Python 3.x instalado en tu sistema.
- Un entorno virtual para gestionar las dependencias.


## Instalación

1. Clona este repositorio en tu máquina local.
2. Crea un entorno virtual en la raíz del proyecto:
    ```bash
    virtualenv [nombre de la carpeta]
    ```
      ```powershell
    virtualenv "nombre de la carpeta"
    ```
3. Activa el entorno virtual:
    - En Windows:
      ```
      "powershell"
            cd  myenv\Scripts
             .\activate 
    
        "bash"
        myenv\Scripts\activate
    ```
    - En Unix o MacOS:
        ```bash
        source myenv/bin/activate
        ```
4. Instala las dependencias:
    ```bash
    pip install mysqlclient
    ```

## Uso

1. Asegúrate de tener un servidor MySQL en ejecución.
2. Ajusta los parámetros de conexión en el script si es necesario (host, usuario, contraseña, nombre de la base de datos).
3. Asegúrate de tener un archivo CSV llamado `localidades.csv` en el mismo directorio que el script.
4. Ejecuta el script Python:
    ```bash
    python connection.py
    ```

## Archivos Generados

Después de ejecutar el script, se crearán archivos CSV separados por provincia en el directorio `csv/`.

## Notas

- Es importante mantener el entorno virtual activado mientras se ejecuta el script para asegurarse de que las dependencias estén disponibles y no haya conflictos con otras versiones de bibliotecas.
- Asegúrate de tener los permisos adecuados para crear y manipular archivos en el directorio donde se encuentra el script.

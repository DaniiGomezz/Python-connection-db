import sys
import MySQLdb
import csv
import os
try:
    db = MySQLdb.connect("localhost", "root", "", "localidades", charset='utf8')
    print("La conexión a la base de datos fue correcta")
except MySQLdb.Error as e:
    print("Error al conectar a la base de datos:", e)
    sys.exit(1)
    
cursor = db.cursor()

# Drop table if exists
try:
    cursor.execute("DROP TABLE IF EXISTS localidades")
    db.commit()
    print("La tabla fue eliminada")
except MySQLdb.Error as e:
    db.rollback()
    print("Error al eliminar la tabla:", e)

# Create table
try:
    create_table_query = "CREATE TABLE IF NOT EXISTS localidades (provincia VARCHAR(100) NOT NULL, id INT NOT NULL, localidad VARCHAR(100) NOT NULL, cp INT NOT NULL, id_prov_mstr INT);"
    cursor.execute(create_table_query)
    db.commit()
    print("La tabla fue creada correctamente")
except MySQLdb.Error as e:
    db.rollback()
    print("Error al crear la tabla:", e)

# Insert data from CSV to database
try:
    with open("localidades.csv", newline="", encoding="utf-8") as file_csv:
        reader_csv = csv.reader(file_csv, delimiter=",", quotechar='"')
        header = next(reader_csv)  # Skip header
        localidades = [(fila[0], int(fila[1]), fila[2], (fila[3]), int(fila[4])) for fila in reader_csv]
        add_localities_query = "INSERT INTO localidades (provincia, id, localidad, cp, id_prov_mstr) VALUES (%s, %s, %s, %s, %s)"
        cursor.executemany(add_localities_query, localidades)
        print("Datos insertados con éxito")
        db.commit()
except MySQLdb.Error as e:
     db.rollback()
     print("Error al insertar los archivos:", e)

if not os.path.exists("csv"):
    os.makedirs("csv")
# Create CSV files by province
try:
    cursor.execute("SELECT DISTINCT provincia FROM localidades")
    provincias = cursor.fetchall()
    for provincia in provincias:
        cursor.execute(
            "SELECT id, localidad, cp, id_prov_mstr FROM localidades WHERE provincia = %s", (provincia[0],)
        )
        localidades = cursor.fetchall()
        with open(
            f"csv/Localidades de {provincia[0]}.csv", "w", encoding="utf-8", newline=""
        ) as file:
            writer = csv.writer(file)
            writer.writerows(localidades)
except MySQLdb.Error as e:
    db.rollback()
    print("Error al crear los archivos CSV:", e)
print("Archivos CSV creados con éxito")

db.close()
#sqleando

import psycopg2

conn = psycopg2.connect(
    port= 5432,
    host="localhost",
    database="Libros",
    user="david",
    password="socosom543")
cur = conn.cursor()
sql= "INSERT INTO libros (titulo, autor, editorial, año, precio, estado, observaciones, tapa, isbn, tema) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
data= ("Historias Fantásticas", "Bioy Casares, Adolfo", "Emecé", 2015, 500, "Usado", "Buen estado", "Blanda", 9789500437721, "Cuentos argentinos")

cur.execute(sql,data)
conn.commit()
cur.close()
conn.close()
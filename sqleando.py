#sqleando

import psycopg2


#valor=(titulo, autor, editorial, año, precio, estado, observaciones, tapa, isbn, tema)

def ingresarenbase(valor):
    conn = psycopg2.connect(
        port= 5432,
        host="localhost",
        database="Libros",
        user="david",
        password="")
    cur = conn.cursor()
    sql= "INSERT INTO libros (titulo, autor, editorial, año, precio, estado, observaciones, tapa, isbn, tema) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    data= valor

    cur.execute(sql,data)
    conn.commit()
    cur.close()
    conn.close()

def confirmarenbase(sku):
    conn = psycopg2.connect(
        port= 5432,
        host="localhost",
        database="Libros",
        user="david",
        password="")
    cur = conn.cursor()
    sql="SELECT * FROM libros WHERE isbn="+str(sku)+";"
    cur.execute(sql)
    obje=cur.fetchone()
    cur.close()
    conn.close()
    return obje

#Importa las Librerias
import pymysql

#Define recupera categorias
def recupera_categoria():
    #Conecta con la base de datos
    conn=pymysql.connect(host="localhost",user="root",passwd="",db="ignorancia")
    #Crea un cursor para navegar en la base
    cursor=conn.cursor()
    #Ejecuta un codigo SQL 
    cursor.execute(" select descripcion from categoria")
    categorias=cursor.fetchall()
    print(categorias)
    #Cierra la base de datos
    conn.close()
    return categorias

#Definir recupera preguntas
def recupera_preguntas(cat):
    #Conecta con la base de datos
     conn=pymysql.connect(host="localhost",user="root",passwd="",db="ignorancia")
     #Crea un cursor para navegar en la base
     cursor=conn.cursor()
     #Ejecuta un codigo SQL
     consulta='select b.id_pregunta,b.pregunta,b.opcion1,b.opcion2,b.opcion3,b.opcion4,b.correcto,b.id_categoria'
     consulta=consulta+' from categoria a, pregunta b'
     consulta=consulta+' where a.descripcion="'+cat+'" and b.id_categoria=a.id_categoria '
     cursor.execute(consulta)
     preguntas=cursor.fetchall()
     print(preguntas)
     #Cierra la base de datos
     conn.close()
     return preguntas

#Define tabla Categorias
def tabla_categorias():
    #Conecta con la base de datos
    conn=pymysql.connect(host="localhost",user="root",passwd="",db="ignorancia")
    #Crea un cursor para navegar en la base
    cursor=conn.cursor()
    #Ejecuta un codigo SQL
    cursor.execute(" select id_categoria,descripcion from categoria")
    cats=cursor.fetchall()
    print(cats)
    #Cierra la base de datos
    conn.close()
    return cats

#Define inserta Categorias
def inserta_categoria(descrip):
    #Conecta con la base de datos
    conn=pymysql.connect(host="localhost",user="root",passwd="",db="ignorancia")
    #Crea un cursor para navegar en la base
    cursor=conn.cursor()
    #Ejecuta un codigo SQL
    cursor.execute("insert into categoria (descripcion) values(%s)",(descrip))
    conn.commit()
    #Cierra la base de datos
    conn.close()

#Define borra Categorias
def borra_categoria(ab):
    #Conecta con la base de datos
    conn=pymysql.connect(host="localhost",user="root",passwd="",db="ignorancia")
    cursor=conn.cursor()
    #Ejecuta un codigo SQL
    cursor.execute("delete from categoria where id_categoria=%s",(ab))
    conn.commit()
    #Cierra la base de datos
    conn.close()

#Define selecciona Categorias
def select_categoria(ab):
    #print("----------------",ab)
    #Conecta con la base de datos
    conn=pymysql.connect(host="localhost",user="root",passwd="",db="ignorancia")
    #Crea un cursor para navegar en la base
    cursor=conn.cursor()
    #Ejecuta un codigo SQL
    cursor.execute("select id_categoria,descripcion from categoria where id_categoria=%s",(ab))
    dato=cursor.fetchone()
    return dato

#Define modifica Categorias
def modif_categoria(ab,descripcion):
    #Conecta con la base de datos
    conn=pymysql.connect(host="localhost",user="root",passwd="",db="ignorancia")
    #Crea un cursor para navegar en la base
    cursor=conn.cursor()
    #Ejecuta un codigo SQL
    cursor.execute("update categoria set descripcion=%s where id_categoria=%s",(descripcion,ab))
    conn.commit()
    #Cierra la base de datos
    conn.close()

#Define borra Preguntas
def borra_pregunta(ab):
    #Conecta con la base de datos
    conn=pymysql.connect(host="localhost",user="root",passwd="",db="ignorancia")
    #Crea un cursor para navegar en la base
    cursor=conn.cursor()
    #Ejecuta un codigo SQL
    cursor.execute("delete from pregunta where id_pregunta=%s",(ab))
    conn.commit()
    #Cierra la base de datos
    conn.close()

#Define modifica Preguntas
def modif_pregunta(ab,datos):
    #Conecta con la base de datos
    conn=pymysql.connect(host="localhost",user="root",passwd="",db="ignorancia")
    #Crea un cursor para navegar en la base
    cursor=conn.cursor()
    #Ejecuta un codigo SQL
    cursor.execute("update pregunta set pregunta=%s,opcion1=%s,opcion2=%s,opcion3=%s,opcion4=%s,correcto=%s where id_pregunta=%s",(datos[0],datos[1],datos[2],datos[3],datos[4],datos[5],ab))
    conn.commit()
    #Cierra la base de datos
    conn.close()

#Define selecciona Preguntas
def select_pregunta(ab):
    #print("----------------",ab)
    #Conecta con la base de datos
    conn=pymysql.connect(host="localhost",user="root",passwd="",db="ignorancia")
    #Crea un cursor para navegar en la base
    cursor=conn.cursor()
    #Ejecuta un codigo SQL
    cursor.execute("select id_pregunta,pregunta,opcion1,opcion2,opcion3,opcion4,correcto,id_categoria from pregunta where id_pregunta=%s",(ab))
    dato=cursor.fetchone()
    return dato

#Define tabla Preguntas
def tabla_preguntas(id):
    #Conecta con la base de datos
    conn=pymysql.connect(host="localhost",user="root",passwd="",db="ignorancia")
    #Crea un cursor para navegar en la base
    cursor=conn.cursor()
    #Ejecuta un codigo SQL
    cursor.execute("select id_pregunta,pregunta,opcion1,opcion2,opcion3,opcion4,correcto,id_categoria from pregunta where id_categoria=%s",(id))
    preguntas=cursor.fetchall()
    #Cierra la base de datos
    conn.close()
    return preguntas

#Define inserta Preguntas
def inserta_pregunta(datos,id):
    #Conecta con la base de datos
    conn=pymysql.connect(host="localhost",user="root",passwd="",db="ignorancia")
    #Crea un cursor para navegar en la base
    cursor=conn.cursor()
    #Ejecuta un codigo SQL
    cursor.execute("insert into pregunta (pregunta,opcion1,opcion2,opcion3,opcion4,correcto,id_categoria) values(%s,%s,%s,%s,%s,%s,%s)",(datos[0],datos[1],datos[2],datos[3],datos[4],datos[5],id))
    conn.commit()
    #Cierra la base de datos
    conn.close()

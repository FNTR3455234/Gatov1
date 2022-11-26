#importa las librerias
from tkinter import *
from tkinter import ttk
from conecta_bd import *
from ed_pregunta import *
import pygame

#ponemos los requerimientos de pygame para poder usarlo en sonidos
pygame.init()
pygame.mixer.init()

#se define manipula categoria ( procedimiento que se ejecuta cuando lo llamamos desde el juego_ignorancia)
def manipula_categorias():
    #definicion de la pantalla
    #creamos una pantalla con toplevel que es una pantalla encima de otra pantalla
    pantalla_cat=Toplevel()
    pantalla_cat.resizable(0,0)
    #tamaño de la pantalla
    pantalla_cat.geometry('700x350')
    #color de la pantala
    pantalla_cat.config(background='gold')
    #titulo de la pantalla
    pantalla_cat.title('catalago de categorias')
    #importo una imagen para el fondo de la pantalla
    fon=PhotoImage(file='jue/fondo_categoria.png')
    #etiqueta para poner la imagen de fondo 
    fond=Label(pantalla_cat, image=fon, bg='gold', width=700, height=350).place(x=0,y=0)
    #declaro un stringvar
    str_cat=StringVar()
    #declaro datos en blanco
    datos=()

    #creamos un marco en donde se encontrara nuestra tabla
    marco_per=Frame(pantalla_cat)
    #empacamos nuestro marco
    marco_per.pack()
    #se coloca en su posicion
    marco_per.place(x=20,y=100)
    #definimos nuestro scrollbar que es para podernos despazarnos de manera vertical
    ver_sb=ttk.Scrollbar(marco_per, orient='vertical')
    #va a estar del lado derecho en las coordenadas de Y
    ver_sb.pack(side=RIGHT, fill=Y)
  
    #creamos una tabla  que se coloca en el marco 
    tabl_cat = ttk.Treeview(marco_per, columns=('col1'), yscrollcommand=ver_sb.set)#el yscrollcommand nos permite ligar nuestra tabla con el scrollbar
    #definimos nuestra columna de 155
    tabl_cat.column('#0',width=155)
    #la otra columna de 500
    tabl_cat.column('col1', width=500)
    #en el encabezado le ponemos el id_categoria
    tabl_cat.heading('#0', text='Id_Categoria')
    #encabezado descipcion
    tabl_cat.heading('col1', text='Descripcion')
    #la empacamos
    tabl_cat.pack()
     
    #configuramos nuestro scrollbar
    ver_sb.config(command=tabl_cat.yview)
    
    #defino un sonido que va para los botones
    def sonido_opcion():
        #importo el sonido
        botoson=pygame.mixer.Sound('jue/botones.mp3')
        #ejecuto
        botoson.play()

    #defino recupera db
    def recupera_db():
        #elimina lo que ya tiene el trieview para dejarlo en blanco.
        for record in tabl_cat.get_children():
            tabl_cat.delete(record)
        #categs va a llamar a tabla de categorias que se encuentra en el conecta bd
        categs = tabla_categorias()
        #los espacios en blanco del Treview de tkinter cortan la descripcion a mostrar
        #y solo muestran la primera palabra para eliminar ese problemas, recorrremos
        #el conjunto y cambiamos los espacios por guion bajo _
        for categ in categs:
            #aqui va insertandos elementos en el trieview
            tabl_cat.insert(parent='', index='end', iid=categ[0], text=str(categ[0]), values=(str(categ[1]).replace('_', '')))

    #se crea el procedimiento para agregar categoria
    def agrega_cat():
        #le mando el contenido que tiene la caja de texto e inserta categoria llama al elemento que esta en el conecta bd
        inserta_categoria(str_cat.get())
        #aqui recupera la base de datos
        recupera_db()
        
    #se define el proceso para borrar los datos de la tabla categoria
    def borra_catsel():
        ab=tabl_cat.selection()[0]
        borra_categoria(ab)
        recupera_db()
          
    #definimos la seleccion de la categoria
    def selec_cat():
        #ponemos datos como global
        global datos
        ab=tabl_cat.selection()[0]#el valor 0 se pondra en datos que es igual select_categoria
        datos=select_categoria(ab)#llamamos a select_categoria
        #se imprime el dato que regreso
        print(datos)
        #regresa la descripcion porque la descripcion es el valor 1
        str_cat.set(datos[1])
        #se activa el boton de modifica categoria
        b_modif_cat.config(state=NORMAL)
        #se activa el boton de borra categoria
        b_borra_ded.config(state=NORMAL)
        #se activa el boton de preguntas
        b_pregunta.config(state=NORMAL)
        
    #definimos la modificacion de categoria
    def modif_catsel():
        #me regresa el id de la categoria a modificar
        ab=tabl_cat.selection()[0]
        #se ejecuta esta funcion que se encuentra en la coneccion de la bd
        modif_categoria(ab,str_cat.get())#le mandamos los parametros, el id y la descripcion
        recupera_db()
        
    #aqui empieza a ejecutarse el codigo
    #llamamos el recupera db
    recupera_db()
    #creo una etiqueta con el texto de categoria
    et=Label(pantalla_cat, text='categoria', bg='light sky blue', font='helvetica 14 bold')
    #colocamos en la posicion
    et.place(x=20, y=20)

    #con este define hacemos que nos den las preguntas de las categoria seleccionada
    def edita_preguntas():
        #llamamos a la variable datos como global
        global datos
        #imprimo los datos
        print(datos)
        #llamo a un procedimiento de manipula preguntas que se encuentra en ed_pregunta
        manipula_preguntas(datos)

    # str que defini arriba le asigno un valor en blanco
    str_cat.set('')
    #aqui creo mi caja de texto para capturar informacion
    pre = Entry(pantalla_cat, textvariable=str_cat, font='helvetica 14 bold', bg='white', width=50)
    #se coloca en su ubicacion
    pre.place(x=20, y=20)
    #agrega categoria

    #boton de pregunta que me lleva a las preguntas
    #importamos la imagen
    b_preg=PhotoImage(file='./jue/boton_preguntas.png')
    #aqui creo mi boton con las caracteristicas necesarias, le agrego la funcionalidad de preguntas y de sonido
    b_pregunta = Button(pantalla_cat, image=b_preg, command=lambda:[edita_preguntas(),sonido_opcion()], fg='white', bg='orange', font='arial 12',state=DISABLED)
    #aqui lo coloco en su posicion
    b_pregunta.place(x=580, y=20)
    
    #boton para agregar categoria
    #importo su imagen
    b_cate_agrega=PhotoImage(file=r'./jue/boton_agrega_categoria.png')
    #lo definimos (utilizo en el command a lambda para poner mas funciones en el boton)
    b_per = Button(pantalla_cat, image=b_cate_agrega, command=lambda:[agrega_cat(), sonido_opcion()], fg='white', bg='orange', font='arial 12')
    #su ubicacion
    b_per.place(x=20, y=60)
    
    #boton para modificar la categoria
    b_modif=PhotoImage(file='./jue/boton_modifica_categoria.png')
    #lo definimos (utilizo en el command a lambda para poner mas funciones en el boton) con sus caracteristicas y su funcionalidad
    b_modif_cat=Button(pantalla_cat, image=b_modif, command=lambda:[modif_catsel(), sonido_opcion()], fg='white', bg='orange',font='arial 12',state=DISABLED)
    #la ubicacion
    b_modif_cat.place(x=170, y=60)
    
    #boton para borrar la categoria
    #importo su imagen
    b_borra=PhotoImage(file='./jue/boton_borra_categoria.png')
    #lo definimos (utilizo en el command a lambda para poner mas funciones en el boton) con sus caracteristicas y su funcionalidad
    b_borra_ded=Button(pantalla_cat,image=b_borra, command=lambda:[borra_catsel(), sonido_opcion()], fg='white', bg='orange', font='arial 12', state=DISABLED)
    #su ubicacion
    b_borra_ded.place(x=320, y=60)

    #boton para la seleccion de categoria
    #importo la imagen para el boton
    b_selec=PhotoImage(file='./jue/boton_selecccion_categoria.png')
    #lo definimos (utilizo en el command a lambda para poner mas funciones en el boton)
    b_selec_cat=Button(pantalla_cat, image=b_selec, command=lambda:[selec_cat(), sonido_opcion()], fg='white', bg='orange',font='arial 12')
    #pongo su ubicacion
    b_selec_cat.place(x=500, y=60)

    #ejecucion infinita de la pantalla
    pantalla_cat.mainloop()

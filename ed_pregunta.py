#importa las librerias
from tkinter import *
from tkinter import ttk
from conecta_bd import*
import pygame

#ponemos los requerimientos de pygame para poder usarlo en sonidos
pygame.init()
pygame.mixer.init()

#definimos manipula preguntas
def manipula_preguntas(datos):
    id=datos[0]#declaro una variable id datos como 0
    pantalla_pre=Toplevel()#creo una pantalla
    pantalla_pre.resizable(0,0)#pantalla no redimensionada
    pantalla_pre.geometry('1250x550')#tamaño de la pantalla
    pantalla_pre.config(background='gold')#color de la pantalla
    pantalla_pre.title('Catalago de preguntas')#titulo de la patalla
    #defino mis stringvar
    str_cat=StringVar()#categoria
    str_pre=StringVar()#pregunta
    str_op1=StringVar()#opcion 1
    str_op2=StringVar()#opcion 2
    str_op3=StringVar()#opcion 3
    str_op4=StringVar()#opcion 4
    str_cor=StringVar()#correcta

    #defino mi fondo para la pantalla
    #importo mi imagen
    fon=PhotoImage(file='./jue/fondo_pregunta.png')
    #creo una etiqueta para colocar la imagen en la pantalla
    fond=Label(pantalla_pre, image= fon, bg='gold', width=1250, height=550).place(x=0,y=0)

    #se crea un marco para contener el trieview
    marco_pre=Frame(pantalla_pre)
    #se empaca
    marco_pre.pack()
    #posicion
    marco_pre.place(x=20, y=250)
    #se coloca en vertical
    ver_sb=ttk.Scrollbar(marco_pre, orient='vertical')
    ver_sb.pack(side=RIGHT, fill=Y)

    #creamos una tabla  que se coloca en el marco  con mas columnas
    tabl_pre = ttk.Treeview(marco_pre, columns=('preg','opc1','opc2','opc3','opc4','corr'), yscrollcommand=ver_sb.set)#el yscrollcommand nos permite ligar nuestra tabla con el scrollbar
    #esta es la llave de la tabla con ancho de 50
    tabl_pre.column('#0', width=50)
    tabl_pre.column('preg', width=500)#pregunta de 500
    tabl_pre.column('opc1', width=150)#opcion 1 de 150
    tabl_pre.column('opc2', width=150)#opcion 2 de 150
    tabl_pre.column('opc3', width=150)#opcion 3 de 150
    tabl_pre.column('opc4', width=150)#opcion 4 de 150
    tabl_pre.column('corr', width=50)#correcto de 50

    #encabezados
    #el primer encabezado es el ID
    tabl_pre.heading('#0', text='Id')
    tabl_pre.heading('preg', text='Pregunta')#pregunta
    tabl_pre.heading('opc1',text='Opc1')#opcion 1
    tabl_pre.heading('opc2',text='Opc2')#opcion 2
    tabl_pre.heading('opc3',text='Opc3')#opcion 3
    tabl_pre.heading('opc4',text='Opc4')#opcion 4
    tabl_pre.heading('corr',text='Corre')#correcto
    #lo empacamos
    tabl_pre.pack()
    #ligamos nuestro scrollbar
    ver_sb.config(command=tabl_pre.yview)

    #defino sonidos para los botones
    def sonido_opcion_preguntas():
        botoson=pygame.mixer.Sound('jue/botones.mp3')
        #se ejecuta el sonido
        botoson.play()

    #recuperamos preguntas con el ide
    def recupera_preg(ide):
        #se limpia la tabla
        for record in tabl_pre.get_children():
            tabl_pre.delete(record)
        #aqui se recupera la tabla de preguntas con el ide
        pregs = tabla_preguntas(ide)
        #los espacios en blanco del Treeview de tkinter cortan la descripcion a mostrar
        #y solo muestran la primera palabra para eliminar ese problema recorremos
        #el conjunto y cambiamos los espacios por guion bajo _
        #el for sirve para ir generando registro por registro en el elemnto de la tabla con las caracteristicas que estan dentro del for
        for preg in pregs:
            #se sustituyen por cada _ poner espacio
            tabl_pre.insert(parent='', index='end', iid=preg[0], text=str(preg[0]),values=(str(preg[1]).replace('_',''),
            str(preg[2]).replace('_',''),str(preg[3]).replace('_',''),str(preg[4]).replace('_',''),
            str(preg[5]).replace('_',''),str(preg[6]).replace('_','')))

    #defino el agrega de preguntas
    def agrega_pre():
        #se crea un conjunto con lo que se capturo en pregunta
        datos=(str_pre.get(),str_op1.get(),str_op2.get(),str_op3.get(),str_op4.get(),str_cor.get())
        #el conjunto de arriba se lo enviamos a inserta pregunta
        inserta_pregunta(datos,id)
        #se recupera la pregunta por el id
        recupera_preg(id)

    #definimos borrar pregunta
    def borra_pre():
        #se recupera el elemento que esta seleccionado
        ab=tabl_pre.selection()[0]
        #llamamos a borra que esta en la conexion
        borra_pregunta(ab)
        #aqui se recupera las preguntas
        recupera_preg(id)

    #definimos la modificacion de preguntas
    def modif_pre():
        ab=tabl_pre.selection()[0]
        #se crea un conjunto
        datos=(str_pre.get(),str_op1.get(),str_op2.get(),str_op3.get(),str_op4.get(),str_cor.get())
        #llamamos a modif_pregunta que esta en la conexion
        modif_pregunta(ab,datos)
        #se recupera la pregunta
        recupera_preg(id)
    
    #definimos seleccion de preguntas
    def selec_pre():
        #recupera el elemento que tenemos seleccionado
        ab=tabl_pre.selection()[0]
        #llamamos a seleccion que esta en la conexion
        dato=select_pregunta(ab)
        str_pre.set(dato[1])
        str_op1.set(dato[2])
        str_op2.set(dato[3])
        str_op3.set(dato[4])
        str_op4.set(dato[5])
        str_cor.set(dato[6])
        #habilita los botones de modifica y borra pregunta
        b_modif_pre.config(state=NORMAL)
        b_borra_pre.config(state=NORMAL)
        
    #recuperamos preguntas con el id
    recupera_preg(id)
    str_cat.set(datos[1])
    str_pre.set('')
    str_op1.set('')
    str_op2.set('')
    str_op3.set('')
    str_op4.set('')
    str_cor.set('')
    #ponemos una etiqueta de categoria
    eti=Label(pantalla_pre,text='Categoria',bg='gold', font='helvetica 14 bold').place(x=20, y=7)
    #aqui creo mi caja de texto para capturar informacion y lo penemos desactivado
    cate = Entry(pantalla_pre, textvariable=str_cat, font='helvetica 14 bold', bg='lavender', width=50, state=DISABLED).place(x=140, y=7)

    #ponemos una etiqueta de preguntas
    et2=Label(pantalla_pre,text='Pregunta',bg='gold', font='helvetica 14 bold').place(x=20, y=60)
    #aqui creo mi caja de texto para capturar informacion
    preg = Entry(pantalla_pre, textvariable=str_pre, font='helvetica 14 bold', bg='lavender', width=80).place(x=120, y=60)

    #etiqueta para opcion 1
    et3=Label(pantalla_pre,text='Opcion 1',bg='gold', font='helvetica 14 bold').place(x=20, y=90)
    #aqui creo mi caja de texto para capturar informacion
    opc1 = Entry(pantalla_pre, textvariable=str_op1,font='helvetica 14 bold', bg='lavender', width=30).place(x=120, y=90)

    #etiqueta para la opcion 2
    et4=Label(pantalla_pre,text='Opcion 2',bg='gold', font='helvetica 14 bold').place(x=550, y=90)
    #aqui creo mi caja de texto para capturar informacion
    opc2 = Entry(pantalla_pre, textvariable=str_op2,font='helvetica 14 bold', bg='lavender', width=30).place(x=670, y=90)

    #etiqueta para la opcion 3
    et5=Label(pantalla_pre,text='Opcion 3',bg='gold', font='helvetica 14 bold').place(x=20, y=120)
    #aqui creo mi caja de texto para capturar informacion
    opc3 = Entry(pantalla_pre, textvariable=str_op3,font='helvetica 14 bold', bg='lavender', width=30).place(x=120, y=120)

    #etiqueta para la opcion 4
    et6=Label(pantalla_pre,text='Opcion 4',bg='gold', font='helvetica 14 bold').place(x=550, y=120)
    #aqui creo mi caja de texto para capturar informacion
    opc4 = Entry(pantalla_pre, textvariable=str_op4,font='helvetica 14 bold', bg='lavender', width=30).place(x=670, y=120)

    #etiqueta para la opcion correcta
    et7=Label(pantalla_pre,text='Correcto',bg='gold', font='helvetica 14 bold').place(x=20, y=150)
    #aqui creo mi caja de texto para capturar informacion
    corr = Entry(pantalla_pre, textvariable=str_cor,font='helvetica 14 bold', bg='lavender', width=30).place(x=120, y=150)

    ##########
    #botones
    ##########

    #boton para agregar una pregunta
    #importa la imagen para el boton
    b_preg=PhotoImage(file='./jue/boton_agrega_pregunta.png')
    #lo definimos (utilizo en el command a lambda para poner mas funciones en el boton) pongo de comando a agrega y sonido
    b_per = Button(pantalla_pre, image=b_preg, command=lambda:[agrega_pre(),sonido_opcion_preguntas()], fg='white', bg='orange', font='arial 12')
    #su posicion
    b_per.place(x=20, y=200)

    #boton para modificar pregunta
    #importo la imagen del boton
    b_modificar=PhotoImage(file='./jue/boton_modificar_pregunta.png')
    #lo definimos (utilizo en el command a lambda para poner mas funciones en el boton) pongo de comando a modifica y sonido
    b_modif_pre=Button(pantalla_pre, image=b_modificar, command=lambda:[modif_pre(), sonido_opcion_preguntas()], fg='white', bg='orange',font='arial 12', state=DISABLED)
    #su posicion
    b_modif_pre.place(x=170, y=200)
    
    #boton para borrar pregunta
    #importo la imagen para el boton
    b_borra=PhotoImage(file='./jue/boton_borrar_pregunta.png')
    #lo definimos (utilizo en el command a lambda para poner mas funciones en el boton) pongo de comando a borra y sonido
    b_borra_pre=Button(pantalla_pre, image=b_borra, command=lambda:[borra_pre(), sonido_opcion_preguntas()], fg='white', bg='orange', font='arial 12',state=DISABLED)
    #su posicion
    b_borra_pre.place(x=320, y=200)
    
    #boton de selecciona pregunta
    #importo su imagen 
    b_selecciona=PhotoImage(file='./jue/boton_selecciona_pregunta.png')
    #lo definimos (utilizo en el command a lambda para poner mas funciones en el boton) pongo de comando a seleccionar y sonido
    b_selec_pre=Button(pantalla_pre,image=b_selecciona, command=lambda:[selec_pre(), sonido_opcion_preguntas()], fg='white', bg='orange',font='arial 12')
    #su ubicacion
    b_selec_pre.place(x=480, y=200)
    
    #ejecucion infinita de la pantalla
    pantalla_pre.mainloop()
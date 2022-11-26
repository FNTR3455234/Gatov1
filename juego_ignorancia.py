#importamos todas las librerias necesarias
import random  
from msilib.schema import ComboBox
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
#importamos la libreria pygame que para este juego nos servira para poner sonidos
import pygame
#conectamos el archiivo de conecta a este archivo
from conecta_bd import*
from ed_categoria import*
paused=False
seleccion=()
#se definen los stringvar
#declaramos la variable correcto
correcto=0
#aqui es la posicion inicial de los jugadores
x1=10
x2=10
x3=10
x4=10
#el turno empieza en 1
turno=1
#declaramos datos
datos=()


def carreritas():

#definicion de la pantalla
    pantalla = Toplevel()
    pantalla.resizable(0,0)
    #dimenziones de la pantalla
    pantalla.geometry("1200x650")
    #icono de la pantallas
    pantalla.iconbitmap("./jue/icono.ico")
    #color de la pantalla
    pantalla.config(background="gold")
    #titulo de la pantalla
    pantalla.title("Ignorancia--BD")

#fondo de la imagen
    fon=PhotoImage(file=r"./jue/pista.png")
    #etiqueta para el fondo(su posicion, color, tamaño)
    fond=Label(pantalla,image=fon, bg="gold", width=1200 , height=650).place(x=0 , y=0)

#escribimos esto para que podamos usar pygame en el audio
    pygame.init()
    pygame.mixer.init()

#le ponemos la musica de fondo a nuestro codigo
    pygame.mixer.music.load('jue/f1.mp3')
    #el -1 funciona para que la musica se reproduzca infinitamente
    pygame.mixer.music.play(-1)
    str_preg=StringVar()
    str_res1=StringVar()
    str_res2=StringVar()
    str_res3=StringVar()
    str_res4=StringVar()
    str_sig=StringVar()

#se define un conjunto vacio que sirve como una variable tipo global
    
    #declaro una variable como global para usarla en la pausa de la musica de fondo
    

#definimos la pausa para detener la musica de fondo
    def pausa():
        #pongo paused como global
        global paused
        #creamos un ciclo para reanudar la musica
        if paused:
            #aqui pongo un unpause para que cuando queramos reanudar la musica se reanude
            pygame.mixer.music.unpause()
            #paused igual a falso
            paused=False

    #creamos un ciclo para la pausa 
        else:
            #pausamos la musica con un pause
            pygame.mixer.music.pause()
            #pausa igual a verdadero
            paused=True
            
#definimos el sonido que hara el boton de siguiente
    def sonibo():  
        #importamos la musica
        sonidobotones=pygame.mixer.Sound('jue/botones.mp3')
        sonidobotones.play()#ejecutamos

#definimos el sonido para los botones de respuestas
    def sonido_opciones():
        #importamos la musica
        sonidopciones=pygame.mixer.Sound('jue/sonido_respuesta.mp3')
        sonidopciones.play()#ejecutamos

#definimos el sonido que sonara cada vez que el jugador que no se la ignorancia avanze
    def sonido_gana():
        #importamos la musica
        sonidogana=pygame.mixer.Sound('jue/sonido_de_aplausos.mp3')
        sonidogana.play()#ejecutamos

    #definimos el sonido para cuando avanze la ignorancia
    def sonido_avanza_ignorancia():
        #importamos la musica
        sonidoigno=pygame.mixer.Sound('jue/sonido_ignorancia.mp3')
        sonidoigno.play()#ejecutamos

#definimos la musica que sonara cuando un jugador gane 
    def ganador():
        #importamos la musica
        gana=pygame.mixer.Sound('jue/ganador.mp3')
        gana.play()#ejecutamos

    #definimos el sonido que sonara cuando la ignorancia gane
    def gana_igno():
        #importamos la musica
        igno=pygame.mixer.Sound('jue/gana_ignorancia.mp3')
        igno.play()#ejecutamos


#definimos avanza jugador
    def avanza_jug():
        #ponemos como global a los jugadores
        global x1, x2, x3
        #aqui avanza 100 el jugador 1 si la respuesta esta correcta
        if turno==1:
            x1=x1+100
            #su nueva posicion
            j1.place(x=x1, y=210)
            #este if funcionara para que se detenga el jugador 1 cada vez que llegue a la meta
            if x1>1100:
                #ponemos un boton para salir
                sal.place(x=200,y=220)
                #le ponemos la musica de ganador
                ganador()
                #le escribimos un mensaje de ganador
                messagebox.showinfo(title='GANADOR',message='Gana el Jugador 1')
                #desabilitamos los todos los botones
                r1.config(state=DISABLED)
                r2.config(state=DISABLED)
                r3.config(state=DISABLED)
                r4.config(state=DISABLED)
                sig.config(state=DISABLED)
                categorias.config(state=DISABLED)
                    
    #aqui avanza 100 el jugador 2 si la respuesta esta correcta
            elif turno==2:
                x2=x2+100
                #su nueva posicion
                j2.place(x=x2, y=325)
                #este if funcionara para que se detenga el jugador 2 cada vez que llegue a la meta
                if x2>1100:
                    #ponemos el boton de salir
                    sal.place(x=200,y=220)
                    #musica de ganador
                    ganador()
                    #le escribimos un mensaje de que ganó
                    messagebox.showinfo(title='GANADOR',message='Gana el Jugador 2')
                    #desactivamos todos los botones
                    r1.config(state=DISABLED)
                    r2.config(state=DISABLED)
                    r3.config(state=DISABLED)
                    r4.config(state=DISABLED)
                    sig.config(state=DISABLED)
                    categorias.config(state=DISABLED)
            
            
    #aqui avanza 100 el jugador 3 si la respuesta esta correcta
            elif turno==3:
                x3=x3+100
        #su nueva posicion
                j3.place(x=x3, y=450)
        #este if funcionara para que se detenga el jugador 3 cada vez que llegue a la meta
                if x3>1100:
            #ponemos el boton de salir
                    sal.place(x=200,y=220)
                    #la musica de ganador
                    ganador()
                    #le ponemos el mensaje de que ganó
                    messagebox.showinfo(title='GANADOR',message='Gana el Jugador 3')
                    #desactivamos todos los botones
                    r1.config(state=DISABLED)
                    r2.config(state=DISABLED)
                    r3.config(state=DISABLED)
                    r4.config(state=DISABLED)
                    sig.config(state=DISABLED)
                    categorias.config(state=DISABLED)
        
#definimos la opcion 1 para el boton 
    def opc1():
        #ponemos global al jugador 4 o la ignorancia
        global turno, x4
        #cuando den la respuesta los botones se desabilitan
        r1.config(state=DISABLED)
        r2.config(state=DISABLED)
        r3.config(state=DISABLED)
        r4.config(state=DISABLED)
        #si la respuesta esta correcta
        if correcto==1:
            #llamamos al procedimiento avanza
            avanza_jug()
            #activo el boton de siguiente
            sig.config(state=NORMAL)
            #le pongo un sonido
            sonido_gana()

    #si la respuesta esta mal
        else:
        #la ignorancia avanza
            x4=x4+100
            jugigno.place(x=x4,y=560)
            #el boton de siguiente se habilita
            sig.config(state=NORMAL)
            #sonido de avanza ignorancia
            sonido_avanza_ignorancia()
            #este if funcionara para que se detenga el jugador de la ignorancia cada vez que llegue a la meta
            if x4>1100:
            #ponemos el boton de salida
                sal.place(x=200,y=220)
                #musica de cuando gana la ignorancia
                gana_igno()
                #le ponemos el mensaje de que gano la ignorancia
                messagebox.showinfo(title='GANADOR',message='Ganó la ignorancia , Ponte a ESTUDIAR')
                #desactivamos todos los botones
                r1.config(state=DISABLED)
                r2.config(state=DISABLED)
                r3.config(state=DISABLED)
                r4.config(state=DISABLED)
                sig.config(state=DISABLED)
                categorias.config(state=DISABLED)
            
            
    #se la aumenta 1 al turno
        turno=turno+1
    #si el turno supera a 3 entonces cambia a 1
        if turno>3:
            turno=1
    #modifico la etiqueta del siguiente jugador
        str_sig.set('Jugador '+ str(turno))

#definimos la opcion 2 para el boton 
    def opc2():
        #ponemos global al jugador 4 o la ignorancia
        global turno, x4
        #cuando den la respuesta los botones se desabilitan
        r1.config(state=DISABLED)
        r2.config(state=DISABLED)
        r3.config(state=DISABLED)
        r4.config(state=DISABLED)
        #si la respuesta esta correcta
        if correcto==2:
            #llamamos al procedimiento avanza
            avanza_jug()
            sig.config(state=NORMAL)
            sonido_gana()
        #si la respuesta esta mal
        else:
        #la ignorancia avanza
            x4=x4+100
            jugigno.place(x=x4,y=560)
            #el boton de siguiente se habilita
            sig.config(state=NORMAL)
            #sonido de avanza ignorancia
            sonido_avanza_ignorancia()
            #este if funcionara para que se detenga el jugador de la ignorancia cada vez que llegue a la meta
            if x4>1100:
            #ponemos el boton de salida
                sal.place(x=200,y=220)
                #se pone la musica de cuando gana la ignorancia
                gana_igno()
                #se le pone un mensaje de que gano la ignorancia
                messagebox.showinfo(title='GANADOR',message='Ganó la ignorancia , Ponte a ESTUDIAR')
                #se desactivan los botones
                r1.config(state=DISABLED)
                r2.config(state=DISABLED)
                r3.config(state=DISABLED)
                r4.config(state=DISABLED)
                sig.config(state=DISABLED)
                categorias.config(state=DISABLED)
            
    #se la aumenta 1 al turno
        turno=turno+1
    #si el turno supera a 3 entonces cambia a 1
        if turno>3:
            turno=1
    #modifico la etiqueta del siguiente jugador
        str_sig.set('Jugador '+ str(turno))
    
#definimos la opcion 3 para el boton
    def opc3():
    #ponemos global al jugador 4 o la ignorancia
        global turno, x4
    #cuando den la respuesta los botones se desabilitan
        r1.config(state=DISABLED)
        r2.config(state=DISABLED)
        r3.config(state=DISABLED)
        r4.config(state=DISABLED)
    #si la respuesta esta correcta
        if correcto==3:
            #llamamos al procedimiento avanza
            avanza_jug()
            sig.config(state=NORMAL)
            sonido_gana()
    #si la respuesta esta mal
        else:
        #la ignorancia avanza
            x4=x4+100
            jugigno.place(x=x4,y=560)
            sig.config(state=NORMAL)
            sonido_avanza_ignorancia()
            if x4>1100:
                sal.place(x=200,y=220)
                gana_igno()
                messagebox.showinfo(title='GANADOR',message='Ganó la ignorancia , Ponte a ESTUDIAR')
                r1.config(state=DISABLED)
                r2.config(state=DISABLED)
                r3.config(state=DISABLED)
                r4.config(state=DISABLED)
                sig.config(state=DISABLED)
                categorias.config(state=DISABLED)
            
            
    #se la aumenta 1 al turno
        turno=turno+1
    #si el turno supera a 3 entonces cambia a 1
        if turno>3:
            turno=1
    #modifico la etiqueta del siguiente jugador
        str_sig.set('Jugador '+ str(turno))

#definimos la opcion 4 para el boton
    def opc4():
        #ponemos global al jugador 4 o la ignorancia
        global turno, x4
        #cuando den la respuesta los botones se desabilitan
        r1.config(state=DISABLED)
        r2.config(state=DISABLED)
        r3.config(state=DISABLED)
        r4.config(state=DISABLED)
        #si la respuesta esta correcta
        if correcto==4:
        #llamamos al procedimiento avanza
            avanza_jug()
            sig.config(state=NORMAL)
            sonido_gana()
        #si la respuesta esta mal
        else:
        #la ignorancia avanza
            x4=x4+100
            jugigno.place(x=x4,y=560)
            sig.config(state=NORMAL)
            sonido_avanza_ignorancia()
            if x4>1100:
                sal.place(x=200,y=220)
                gana_igno()
                messagebox.showinfo(title='GANADOR',message='Ganó la ignorancia , Ponte a ESTUDIAR')
                r1.config(state=DISABLED)
                r2.config(state=DISABLED)
                r3.config(state=DISABLED)
                r4.config(state=DISABLED)
                sig.config(state=DISABLED)
                categorias.config(state=DISABLED)
            
            
    #se la aumenta 1 al turno
        turno=turno+1
    #si el turno supera a 3 entonces cambia a 1
        if turno>3:
            turno=1
    #modifico la etiqueta del siguiente jugador
        str_sig.set('Jugador '+ str(turno))

#definimos sel pregunta
    def sel_preg():
        #definimos el global stringvar pregunta
        #global correcto
        global correcto
        #tamaño de la seleccion de las preguntas
        tam=len(seleccion)
        #si el tamaño es diferente a 0
        if tam!=0:
            #aqui se van a generar preguntas aleatorias dependiendo de la categoria
            n = random.randint(0, tam-1)
            #print(n)
            #str de pregunta  en la posicion 1
            str_preg.set(seleccion[n][1])
            #str de respuesta 1 en la posicion 2
            str_res1.set(seleccion[n][2])
            #str de respuesta 2 en la posicion 3
            str_res2.set(seleccion[n][3])
            #str de respuesta 3 en la posicion 4
            str_res3.set(seleccion[n][4])
            #str de respuesta 4 en la posicion 5
            str_res4.set(seleccion[n][5])
            #el correcto es igual a seleccion en la posicion 6
            correcto=seleccion[n][6]
            #se imprime el correcto
            print(correcto)
        #los botones estan normales
            r1.config(state=NORMAL)
            r2.config(state=NORMAL)
            r3.config(state=NORMAL)
            r4.config(state=NORMAL)
        else:
        #si la categoria no tiene preguntas entonces se le escribe que no tiene preguntas
            str_preg.set('categoria sin preguntas')
            #los botones de respuestas se ponen en blanco
            str_res1.set('')
            str_res2.set('')
            str_res3.set('')
            str_res4.set('')
        #se bloquean los botones
            r1.config(state=DISABLED)
            r2.config(state=DISABLED)
            r3.config(state=DISABLED)
            r4.config(state=DISABLED)
        
    #pantalla.update()

#definimos preguntas
    def preguntas(event):
        #lo pongo como global para poder modificarlo
        global seleccion
        #me regresa el elemento del combo que yo seleccione
        cat = event.widget.get()
        #los espacios en blanco del combo de tkinter agregan llaves en el conjunto
        #para eliminar ese problema recorremos el conjunto y cambiamos los espacios
        #por guion bajo _ para hacer la busqueda en la base de datos necesitamos ahora
        # remplazar los giones bajos _ por espacios en blanco
        cat=str(cat).replace('_', '')
        #llamamos a la base de datos en recupera preguntas
        seleccion= recupera_preguntas(cat)
        #llamamos a este procedimiento
        sel_preg()
        #le pongo sonido
        sonibo()
        #desactivo el boton de siguiente
        sig.config(state=DISABLED)

#definimos la pregunta siguiente
    def pregunta_sig():
        #ponemos como global a seleccion (seleccion lo declaramos como un conjunto vacio)
        global seleccion
        cat = categorias.get()
        #los espacios en blanco del combo de tkinter agregan llaves en el conjunto
        #para eliminar ese problema recorremos el conjunto y cambiamos los espacios
        #por guion bajo _ para hacer la busqueda en la base de datos necesitamos ahora
        # remplazar los giones bajos _ por espacios en blanco
        cat=str(cat).replace('_', '')
        #seleccion que recuperamos en la base de datos
        seleccion=recupera_preguntas(cat)
        #llama al procedimiento sel_preg
        sel_preg()
        #se le pone un sonido 
        sonibo()
        #el boton de siguiente lo dasactivo
        sig.config(state=DISABLED)
    
#definimos el edita catgoria
    def edita_categorias():
        #llamamos al procedimiento que se encuentra en el codigo de ed_categoria
        manipula_categorias()

#####################
#procedimiento main
#####################

#recuperamos la categoria
    l_cats=recupera_categoria()
    #los espacios en blanco del combo de tkinter agregan llaves en el contenido
    #para eliminar este problema recorremnos el conjunto y cambiamo los espacios 
    # guion bajo _
    #creamos un conjunto nuevo
    cats=[]
    #se va a hacer un recorrido con este for 
    for cat in l_cats:
        #cada vez que haiga espacios se le pondra un guion bajo
        cat2=str(cat[0]).replace('_','')
        #lo agregamos en nuestro conjunto vacio de cats=[]
        cats.append(cat2)

#se crea una etiqueta para que en la pantalla diga categoria
    eti = Label(pantalla ,bg="gold", text="Categoria", font='helvetica 18 bold')
    #su posicion en la pantalla
    eti.place(x=10 , y=10)

#se crea un combobox que se coloca en la pantalla
    categorias=ttk.Combobox(pantalla, font='helvetica 18 bold')
    #los values se le va a asignar lo que tiene cats (recuerda que cats es lo que le manda recupera_categoria en la base de datos)
    categorias['values']= cats
    #su ubicacion
    categorias.place(x=150 , y=10)
    #cuando ejecute el combobox se va a ir al procedimiento de preguntas
    categorias.bind("<<ComboboxSelected>>", preguntas)


#boton siguiente

#importamos la imagen
    siguiente=PhotoImage(file='./jue/siguiente.png')
    #lo definimos (utilizo en el command a lambda para poner mas funciones en el boton)
    sig = Button(pantalla, image=siguiente , command=lambda:[pregunta_sig(), sonibo()],font='helvetica 14 bold', bg='white', state=DISABLED )
    #su ubicacion
    sig.place(x=700, y=12)



#boton de categorias
#importamos la imagen
    botcat=PhotoImage(file='./jue/bocate.png')
    #lo definimos (utilizo en el command a lambda para poner mas funciones en el boton)
    cat_categ = Button(pantalla, image=botcat, command=lambda:[edita_categorias(), sonibo()], font='helvetica 14 bold', bg='white')
    #ubicacion 
    cat_categ.place(x=950, y=10)

#aqui va que turno sigue 
    str_sig.set('Jugador 1')
    #lo definimos
    sig_jug = Label(pantalla, bg='gold', textvariable=str_sig, font='helvetica 18 bold' )
    #su ubicacion
    sig_jug.place(x=500 , y=10)

    #definir la etiqueta de pregunta
    #lo definimos
    eti = Label(pantalla, bg='gold', text='pregunta', font='helvetica 18 bold')
    #su ubicacion
    eti.place(x=10 , y=60)

#aqui aparece la pregunta que corresponde a la categoria
    str_preg.set("")
    #lo definimos y lo desactivo
    pre = Entry(pantalla, textvariable=str_preg, font='Helvetica 18 bold', bg="white", width=80, state=DISABLED)
    #su ubicacion
    pre.place(x=150, y=60)

#boton de opcion 1 para la respuesta de la pregunta correspondiente a la categoria
    str_res1.set("")
    #lo definimos (utilizo en el command a lambda para poner mas funciones en el boton)
    r1 = Button(pantalla, textvariable=str_res1, command=lambda:[opc1(), sonido_opciones()], font='Helvetica 14 bold' ,bg="light goldenrod", fg='black', width=20)
    #su ubicacion
    r1.place(x=100, y=110)

    #boton de opcion 2 para la respuesta de la pregunta correspondiente a la categoria
    str_res2.set("")
    #lo definimos (utilizo en el command a lambda para poner mas funciones en el boton)
    r2 = Button(pantalla, textvariable=str_res2, command=lambda:[opc2(), sonido_opciones()], font='Helvetica 14 bold' ,bg="light goldenrod", fg='black', width=20)
    #su ubicacion
    r2.place(x=360, y=110)

#boton de opcion 3 para la respuesta de la pregunta correspondiente a la categoria
    str_res3.set("")
    #lo definimos (utilizo en el command a lambda para poner mas funciones en el boton)
    r3 = Button(pantalla, textvariable=str_res3, command=lambda:[opc3(), sonido_opciones()], font='Helvetica 14 bold' ,bg="light goldenrod", fg='black', width=20)
    #su ubicacion
    r3.place(x=620, y=110)

    #boton de opcion 4 para la respuesta de la pregunta correspondiente a la categoria
    str_res4.set("")
    #lo definimos (utilizo en el command a lambda para poner mas funciones en el boton)
    r4 = Button(pantalla, textvariable=str_res4, command=lambda:[opc4(), sonido_opciones()], font='Helvetica 14 bold' ,bg="light goldenrod", fg='black', width=20)
    #su ubicacion
    r4.place(x=880, y=110)

    #se define el jugador 1
    #importamos su imagen
    jug1=PhotoImage(file="./jue/1.png")
    #lo definimos con una etiqueta
    j1=Label(pantalla, image=jug1, bg='white', width=0,height=0 )
    #su ubicacion
    j1.place(x=10 , y=210)

    #se define el jugador 2
    #importamos la imagen
    jug2=PhotoImage(file="./jue/2.png")
    #lo definimos con una etiqueta
    j2=Label(pantalla, image=jug2, bg='white', width=0,height=0 )
    #su ubicacion
    j2.place(x=10 , y=325)

    #se define el jugador 3
    jug3=PhotoImage(file="./jue/3.png")
    #lo definimos con la etiqueta
    j3=Label(pantalla, image=jug3, bg='white', width=0,height=0 )
    #su ubicacion
    j3.place(x=10 , y=450)

    #definimos a la ignorancia
    #se importa su imagen
    juig=PhotoImage(file="./jue/igno.png")
    #lo definimos con una etiqueta
    jugigno=Label(pantalla, image=juig, bg='white', width=0,height=0 )
    #su ubicacion
    jugigno.place(x=10 , y=560)


    #creo un boton para salir, este boton aparece cuando ya haiga ganadao un jugador o la ignorancia
    sal=Button(pantalla, text='Salir', command=exit, bg='gold', font='helvetica 18 bold',width=30, height=3)
    sal.place(x=2000, y=700)

    #aqui cree el boton de pausa para detener la musica
    puas=PhotoImage(file='./jue/boton_pausa.png')
    pau=Button(pantalla, image=puas, command=pausa,bg='red', font='helvetica 14 bold')
    #defino su posicion
    pau.place(x=1150, y=110)

    #ejecucion de la pantalla
    pantalla.mainloop()
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from juego_ignorancia import *
from ed_categoria import *
turno=1
correcto=0

def gato():
    pant=Toplevel()
    pant.resizable(1,1)
    pant.config(bg="light sky blue")
    pant.title("carrera de la ignorancia")
    pant.geometry("1200x700")
   

    eti=Label(pant,bg="light sky blue",text="Gato",font="Helvetica 80 bold")
    eti.place(x=50,y=50)
    
    str_cat=StringVar()
    str_pregs=StringVar()
    str_resp1=StringVar()
    str_resp2=StringVar()
    str_resp3=StringVar()
    str_resp4=StringVar()
    seleccion=()

    def b1():
        global turno
        if turno==1:
            b00.config(state=DISABLED,bg="red")  
            turno=turno+1
        elif turno==2:
            b00.config(state=DISABLED,bg="green")  
            turno=turno+1
        if turno>2:
            turno=1  
    def b2():
        global turno
        if turno==1:
            b01.config(state=DISABLED,bg="red")  
            turno=turno+1
        elif turno==2:
            b01.config(state=DISABLED,bg="green")  
            turno=turno+1
        if turno>2:
            turno=1  
    def b3():
        global turno
        if turno==1:
            b02.config(state=DISABLED,bg="red")  
            turno=turno+1
        elif turno==2:
            b02.config(state=DISABLED,bg="green")  
            turno=turno+1
        if turno>2:
            turno=1
    def b4():
        global turno
        if turno==1:
            b10.config(state=DISABLED,bg="red")  
            turno=turno+1
        elif turno==2:
            b10.config(state=DISABLED,bg="green")  
            turno=turno+1
        if turno>2:
            turno=1
    def b5():
        global turno
        if turno==1:
            b11.config(state=DISABLED,bg="red")  
            turno=turno+1
        elif turno==2:
            b11.config(state=DISABLED,bg="green")  
            turno=turno+1
        if turno>2:
            turno=1
    def b6():
        global turno
        if turno==1:
            b12.config(state=DISABLED,bg="red")  
            turno=turno+1
        elif turno==2:
            b12.config(state=DISABLED,bg="green")  
            turno=turno+1
        if turno>2:
            turno=1
    def b7():
        global turno
        if turno==1:
            b20.config(state=DISABLED,bg="red")  
            turno=turno+1
        elif turno==2:
            b20.config(state=DISABLED,bg="green")  
            turno=turno+1
        if turno>2:
            turno=1
    def b8():
        global turno
        if turno==1:
            b21.config(state=DISABLED,bg="red")  
            turno=turno+1
        elif turno==2:
            b21.config(state=DISABLED,bg="green")  
            turno=turno+1
        if turno>2:
            turno=1
    def b9():
        global turno
        if turno==1:
            b22.config(state=DISABLED,bg="red")  
            turno=turno+1
        elif turno==2:
            b22.config(state=DISABLED,bg="green")  
            turno=turno+1
        if turno>2:
            turno=1
    
            

    def sele_preg():
        global correcto
        tam=len(seleccion)
        if tam!=0:
            n = random.randint(0, tam-1)
            str_pregs.set(seleccion[n][1])
            str_resp1.set(seleccion[n][2])
            str_resp2.set(seleccion[n][3])
            str_resp3.set(seleccion[n][4])
            str_resp4.set(seleccion[n][5])
            correcto=seleccion[n][6]
            #se imprime el correcto
            print(correcto)
            #los botones estan normales
        else:
            #si la categoria no tiene preguntas entonces se le escribe que no tiene preguntas
            str_pregs.set('categoria sin preguntas')
            #los botones de respuestas se ponen en blanco
            str_resp1.set('')
            str_resp2.set('')
            str_resp3.set('')
            str_resp4.set('')
            
    def preguntas(event):
        global seleccion
        cat = event.widget.get()
        cat=str(cat).replace('_', '')
        seleccion= recupera_preguntas(cat)
        sele_preg()
    
    l_cats=recupera_categoria()
    cats=[]
    for cat in l_cats:
        cat2=str(cat[0]).replace('_','')
        cats.append(cat2)

    eti = Label(pant ,bg="gold", text="Categoria", font='helvetica 18 bold')
    eti.place(x=20 , y=420)

    pre=Label(pant, text='Pregunta',bg='Light sky blue', font='helvetica 14 bold')
    pre.place(x=20, y=500)
    str_pregs.set('')
    pre_ent=Entry(pant, textvariable=str_pregs, font='helvetica 18 bold', bg='white',width=60, state=DISABLED)
    pre_ent.place(x=115,y=500)

    cat=Label(pant, text='Categoria',bg='light sky blue', font='helvetica 14 bold')
    cat.place(x=20, y=420)
   
    

    #se crea un combobox que se coloca en la pantalla
    categorias=ttk.Combobox(pant, font='helvetica 18 bold')
    categorias['values']= cats
    categorias.place(x=150 , y=420)
    categorias.bind("<<ComboboxSelected>>", preguntas)
    


















#260

    str_resp1.set("")
    re1=Button(pant,textvariable=str_resp1,font='helvetica 14 bold ', bg='white', fg='black', width=20)
    re1.place(x=20,y=570)

    str_resp2.set("")
    re2=Button(pant,textvariable=str_resp2,font='helvetica 14 bold ', bg='white', fg='black', width=20)
    re2.place(x=280,y=570)

    str_resp3.set("")
    re3=Button(pant,textvariable=str_resp3,font='helvetica 14 bold ', bg='white', fg='black', width=20)
    re3.place(x=540,y=570)

    str_resp4.set("")
    re4=Button(pant,textvariable=str_resp4,font='helvetica 14 bold ', bg='white', fg='black', width=20)
    re4.place(x=800,y=570)

    rei=Button(pant,text='Reiniciar',font='helvetica 14 bold',bg='white',fg='black')
    rei.place(x=900,y=270)

    sal=Button(pant, text='Salir',font='helvetica 14 bold',bg='white',fg='black')
    sal.place(x=1025,y=270)

    mod_ju=Button(pant,text='Modificar Jugador',font='helvetica 14 bold',bg='white', fg='black')
    mod_ju.place(x=900,y=320)

    cam_per=Button(pant,text='Cambiar Personaje',font='helvetica 14 bold',bg='white', fg='black')
    cam_per.place(x=900,y=370)

    b00=Button(pant,command=b1,font="Helvetica 18 bold",bg="blue",fg="black",width=3)
    b00.place(x=350,y=120)
    b01=Button(pant,command=b2,font="Helvetica 18 bold",bg="blue",fg="black",width=3)
    b01.place(x=420,y=120)
    b02=Button(pant,command=b3,font="Helvetica 18 bold",bg="blue",fg="black",width=3)
    b02.place(x=490,y=120)
    b10=Button(pant,command=b4,font="Helvetica 18 bold",bg="blue",fg="black",width=3)
    b10.place(x=350,y=190)
    b11=Button(pant,command=b5,font="Helvetica 18 bold",bg="blue",fg="black",width=3)
    b11.place(x=420,y=190)
    b12=Button(pant,command=b6,font="Helvetica 18 bold",bg="blue",fg="black",width=3)
    b12.place(x=490,y=190)
    b20=Button(pant,command=b7,font="Helvetica 18 bold",bg="blue",fg="black",width=3)
    b20.place(x=350,y=260)
    b21=Button(pant,command=b8,font="Helvetica 18 bold",bg="blue",fg="black",width=3)
    b21.place(x=420,y=260)
    b22=Button(pant,command=b9,font="Helvetica 18 bold",bg="blue",fg="black",width=3)
    b22.place(x=490,y=260)
    pant.mainloop()
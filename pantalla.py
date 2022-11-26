from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gato import*
from ed_categoria import*
from ed_pregunta import*

pant=Tk()
pant.resizable(1,1)
pant.config(bg="Light blue")
pant.title("carrera de la ignorancia")
pant.geometry("1200x700")


def carrera():
    carreritas()

def edita_categorias():
        manipula_categorias()

def cat():
      gato()
r1=Button(pant,text="Carrera",command=carrera,font="Helvetica 18 bold",bg="blue",fg="black",width=15)
r1.place(x=210,y=520)

r2=Button(pant,text="Catalogos",command=edita_categorias,font="Helvetica 18 bold",bg="blue",fg="black",width=15)
r2.place(x=440,y=520)

r3=Button(pant,text="Gato",command=cat,font="Helvetica 18 bold",bg="blue",fg="black",width=15)
r3.place(x=680,y=520)

pant.mainloop()

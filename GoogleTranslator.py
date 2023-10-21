from tkinter import * 
from tkinter import ttk 
from googletrans import Translator,LANGUAGES

def change(text="type",src = "english",dest = "hindi"):
    trans1= text
    src1 = src
    dest1 = dest
    trans = Translator()
    trans1 = trans.translator(text,src= src1,dest=dest1)
    return trans1.text

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    masg = Sor_txt.get(1.0,END)
    textget = change(text = masg, src = s,dest = d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,text_get)


root =Tk() 
root.title("Translator")
root.geometry("500x600")
root.config(bg='Red')

lab_txt=Label(root,text="Translator",font=(" Time New Roman",30,"bold"),bg="Green")
lab_txt.place(x=100,y=40,height=40,width=300)


frame =Frame(root).pack(side=BOTTOM)

lab_txt=Label(root,text="Source Text",font=(" Time New Roman",20,"bold"),fg="Black",bg="red")
lab_txt.place(x=100,y=100,height=19,width=300)

Sor_txt= Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
Sor_txt.place(x=10,y=120,height=100,width=480)


list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(frame,value= list_text)
comb_sor.place(x=10,y=230,height=30,width=100)
comb_sor.set("English",)

button_change = Button(frame,text="Translate",relief=RAISED,command=data)
button_change.place(x=120,y=231,height=30,width=100)

comb_dest = ttk.Combobox(frame,value= list_text)
comb_dest.place(x=231,y=231,height=30,width=100)
comb_dest.set("English") 

lab_txt=Label(root,text="Dest Text",font=(" Time New Roman",20,"bold"),fg="Black",bg="red")
lab_txt.place(x=100,y=400,height=25,width=300)

dest_txt= Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
dest_txt.place(x=10,y=450,height=100,width=480)

root.mainloop()
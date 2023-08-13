from tkinter import *
def click(event):
    global scvalue
    text=event.widget.cget("text")
    print(text)
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            value=eval(screen.get())
        scvalue.set(value)
        screen.update()
    elif text=="C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()
        
        

root=Tk()
root.geometry("500x700")
root.title("Calculator By Manas")

scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue ,font="lucida 40 bold")
screen.pack(fill=X,ipadx=8,pady=7,padx=6)

#frame banake 3-3 karke buttons pack karte jaenge
f=Frame(root,bg="grey")
b=Button(f,text="C",font="lucida 30 bold",padx=3,pady=6)

b.pack(side=LEFT,padx=9,pady=6)
b.bind("<Button-1>",click)
b=Button(f,text="(",font="lucida 30 bold",padx=8,pady=3)
b.pack(side=LEFT,padx=9,pady=6)
b.bind("<Button-1>",click)
b=Button(f,text=")",font="lucida 30 bold",padx=8,pady=3)
b.pack(side=LEFT,padx=9,pady=6)
b.bind("<Button-1>",click)
b=Button(f,text="/",font="lucida 30 bold",padx=6,pady=3)
b.pack(side=LEFT,padx=9,pady=6)
b.bind("<Button-1>",click)


f.pack()
f=Frame(root,bg="grey")
b=Button(f,text="9",font="lucida 30 bold",padx=6,pady=6)

b.pack(side=LEFT,padx=7,pady=6)
b.bind("<Button-1>",click)
b=Button(f,text="8",font="lucida 30 bold",padx=6,pady=3)
b.pack(side=LEFT,padx=7,pady=6)
b.bind("<Button-1>",click)
b=Button(f,text="7",font="lucida 30 bold",padx=6,pady=3)
b.pack(side=LEFT,padx=7,pady=6)
b.bind("<Button-1>",click)
b=Button(f,text="*",font="lucida 30 bold",padx=6,pady=3)
b.pack(side=LEFT,padx=7,pady=6)
b.bind("<Button-1>",click)


f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="6",font="lucida 30 bold",padx=6,pady=3)

b.pack(side=LEFT,padx=8,pady=6)
b.bind("<Button-1>",click)
b=Button(f,text="5",font="lucida 30 bold",padx=6,pady=3)
b.pack(side=LEFT,padx=7,pady=6)
b.bind("<Button-1>",click)
b=Button(f,text="4",font="lucida 30 bold",padx=6,pady=3)
b.pack(side=LEFT,padx=8,pady=6)
b.bind("<Button-1>",click)
b=Button(f,text="-",font="lucida 30 bold",padx=6,pady=3)
b.pack(side=LEFT,padx=7,pady=6)
b.bind("<Button-1>",click)


f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="3",font="lucida 30 bold",padx=6,pady=3)

b.pack(side=LEFT,padx=7,pady=6)
b.bind("<Button-1>",click)
b=Button(f,text="2",font="lucida 30 bold",padx=6,pady=3)
b.pack(side=LEFT,padx=7,pady=6)
b.bind("<Button-1>",click)
b=Button(f,text="1",font="lucida 30 bold",padx=6,pady=3)
b.pack(side=LEFT,padx=7,pady=6)
b.bind("<Button-1>",click)
b=Button(f,text="+",font="lucida 30 bold",padx=3,pady=3)
b.pack(side=LEFT,padx=7,pady=6)
b.bind("<Button-1>",click)


f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="0",font="lucida 30 bold",padx=6,pady=3)

b.pack(side=LEFT,padx=7,pady=6)
b.bind("<Button-1>",click)
b=Button(f,text=".",font="lucida 30 bold",padx=8,pady=3)
b.pack(side=LEFT,padx=6,pady=6)
b.bind("<Button-1>",click)
b=Button(f,text="%",font="lucida 30 bold",padx=2,pady=3)
b.pack(side=LEFT,padx=7,pady=6)
b.bind("<Button-1>",click)
b=Button(f,text="=",font="lucida 30 bold",padx=6,pady=3)
b.pack(side=LEFT,padx=7,pady=6)
b.bind("<Button-1>",click)


f.pack()


root.mainloop()
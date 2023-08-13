from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled - Notepad")
    file=None
    TextArea.delete(1.0,END) #pehli line ke 0th character tak sab hata do
    
def openFile():
    global file
    file=askopenfilename(defaultextension='.txt',filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file) + " - Notepad") #basename poore file path mein se name extract karke de dega
        TextArea.delete(1.0,END)
        f=open(file,'r')
        TextArea.insert(1.0,f.read())
        f.close()
def saveFile():
    global file 
    if file==None:
        file=asksaveasfilename(initialfile= "Untitled.txt",defaultextension='.txt',filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file=="":
            file=None
        else:
            f=open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()
            root.title(os.pathbasename(file) +" - Notepad")
            print("File saved")
    else:
        f=open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close()
        
        
        
        
def quitApp():
    root.destroy()
def cut():
    TextArea.event_generate(("<<Cut>>"))
def copy():
    TextArea.event_generate(("<<Copy>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))
    
def about():
    showinfo("Notepad","Notepad by Mansi")
    



if __name__=="__main__":
    #Basic tkinter setup
    root=Tk()
    root.title("Untitled - Notepad")
    #root.wm_iconbitmap("1.ico")
    root.geometry("644x788")
    
    #Add textArea
    TextArea=Text(root,font="lucida 13")
    
    file=None
    
    TextArea.pack(fill=BOTH,expand=True)
    
    #creating Menu Bar
    #let's create a menubar
    MenuBar=Menu(root)
    #FileMenu starts
    FileMenu=Menu(MenuBar,tearoff=0)
    #To open new file 
    FileMenu.add_command(label="New",command=newFile)
    #To open an already existing file
    FileMenu.add_command(label="Open",command=openFile)    
    #to save the current file
    FileMenu.add_command(label="Save",command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit",command=quitApp)
    MenuBar.add_cascade(label="File",menu=FileMenu)
    #FileMenu ends
    
    #edit menu starts
    EditMenu=Menu(MenuBar,tearoff=0)
    #to give a cut feature
    EditMenu.add_command(label="Cut",command=cut)
    EditMenu.add_command(label="Copy",command=copy)
    EditMenu.add_command(label="Paste",command=paste)
    MenuBar.add_cascade(label="Edit",menu=EditMenu)
    #edit menu ends
    
    #Help Menu starts
    HelpMenu=Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label="About Notepad", command=about)
    MenuBar.add_cascade(label="Help",menu=HelpMenu)
    
    
    root.config(menu=MenuBar)
    #Adding scrollbar using rules from Tkinter lecture no. 22
    Scroll=Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)
    root.mainloop()    
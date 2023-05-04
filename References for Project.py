from tkinter import *

def deleteItem():
    myList.delete(ANCHOR)
def addItem():
    myList.insert(END, myEntry.get())
    myEntry.delete(0, END)




if __name__=='__main__':
    window = Tk()
    window.title("Start Menu")
    
    
    myFrame = Frame(window)
    myFrame.pack(pady=10)
    
    myList = Listbox(
        width=25,
        height=5,
        bg="tan",
        borderwidth=2,
        fg="black"
    )
    myList.pack(side=LEFT, fill=BOTH)
    
    stuff = []
    for item in stuff:
        myList.insert(END, item)
        
    myScrollBar = Scrollbar(myFrame)
    myScrollBar.pack(side=RIGHT, fill=BOTH)
    
    myList.config(yscrollcommand=myScrollBar.set)
    myScrollBar.config(command=myList.yview)
    
    myEntry = Entry(window, font=(24))
    myEntry.pack(pady=20)
    
    buttonFrame = Frame(window)
    buttonFrame.pack(pady=20)
    deleteButton = Button(buttonFrame, text="Delete", command=deleteItem)
    addButton = Button(buttonFrame, text="Add Item", command=addItem)
    
    deleteButton.grid(row=0, column=0)
    addButton.grid(row=0, column=1, padx=20)

    window.mainloop()
    
    
    
    
    
    
    
    
    
    
    
    
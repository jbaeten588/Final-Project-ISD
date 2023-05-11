from tkinter import *


items = []



def openSecondWindow ():
    '''Second window allowing to-do list to be made'''
    
    secondWindow = Toplevel()
    secondWindow.title("To-do List Menu")
    secondWindow.geometry("500x500")
    secondWindow.config(background="lightblue")
    heading = Label(secondWindow, text="Enter List Item:", fg="black", bg='lightblue')
    heading.config(font=("Times New Roman", 24))
    heading.pack(padx=10, pady=10)
    userEntry = Entry(secondWindow)
    userEntry.pack(padx=10, pady=10)
    buttonFrame = Frame(secondWindow, bg="lightblue")
    buttonFrame.pack(pady=20)
    
    
    
    def deleteItem():
        '''Button function that allows check-buttons to be deleted'''
        
        for item in items:
            if item['state'].get():
                item['widget'].destroy()
                items.remove(item)
        
                    
    def addItem(text=None):
        '''Button function that allows check-buttons to be added to the list'''
        
        if not text:
            text = userEntry.get()
        state = IntVar()
        items.append({
                'widget': Checkbutton(secondWindow,
                                      text=text,
                                      fg="black",
                                      activebackground="yellow",
                                      variable=state
                                      ),
                'state': state
            }
        )
        items[len(items) - 1]['widget'].pack(fill=BOTH, padx=100, pady=15)
        userEntry.delete(0, END)
        
    addButton = Button(buttonFrame, text="Add Item", command=addItem)
    deleteButton = Button(buttonFrame, text="Delete", command=deleteItem)
    deleteButton.grid(row=0, column=2, padx=10)
    addButton.grid(row=0, column=0, padx=10)
    listTitle = Label(secondWindow, text="To-Do List:", fg="black", bg="lightblue")
    listTitle.config(font=("Times New Roman", 18, "bold"))
    listTitle.pack(padx=10, pady=10)
    itemList = []
    for item in itemList:
        addItem(item)
        
if __name__=='__main__':
    '''First window and it displays start menu'''
    
    window = Tk()
    window.title("Start Menu")
    window.geometry("500x500")
    window.config(background="lightblue")
    
    mainLabel = Label(text="What would you like to accomplish today?",fg="black", bg="lightblue")
    mainLabel.config(font=("Times New Roman", 24))
    startLabel = Label(text="Click here to begin: ", fg="black", bg="lightblue")
    startLabel.config(font=("Times New Roman", 22, "bold"))
    startButton = Button(text="Start", relief='flat', width=15, borderwidth=0, height=3,command=openSecondWindow)
    startButton.config(font=("Times New Roman", 20, "bold"))
    mainLabel.pack(fill=BOTH, padx=10, pady=10)
    startLabel.pack(fill=BOTH, padx=10, pady=10)
    startButton.pack(padx=20, pady=20)

    
    
    window.mainloop()


#https://www.geeksforgeeks.org/python-grid-method-in-tkinter/ 
#https://pythonassets.com/posts/create-a-new-window-in-tk-tkinter/
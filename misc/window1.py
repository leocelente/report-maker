#!/usr/bin/python3
from tkinter import *
from tkinter import ttk
from tkinter import filedialog



if __name__ == "__main__":

    def browseLog(*args):
        filename = filedialog.askopenfilename()
        if not filename == "":
            logFilename.set(filename)

    def addField():
        value = fieldString.get()
        lbxFields.insert(0, value)

    def editField():
        index = lbxFields.curselection()
        lbxFields.insert(index, fieldString.get())

    def removeField():
        value = lbxFields.curselection()
        lbxFields.delete(value)

    def parse():
        pass

    root = Tk()
    # -- Window Options -- 
    root.geometry("800x600")
    root.grid_columnconfigure(12)
    root.grid_rowconfigure(12)
    root.resizable(False, False)  # Fix Window Size
    content = ttk.Frame(root)

    # frame = ttk.Frame(content, relief="sunken", width=800, height=600)

    # Variables
    tokenSeparator  = StringVar()
    logFilename     = StringVar(value="<log file>")
    parserString    = StringVar()
    fieldString     = StringVar()

    fields_list     = StringVar()
    fields_list.set(())
    

    # Component Creation
    lblBrowse       = ttk.Label(content,    textvariable=logFilename)

    btnBrowse       = ttk.Button(content, text="Browse",    command=browseLog)

    lbxFields       = Listbox(content,      listvariable=fields_list)
    txtAddField     = ttk.Entry(content,    textvariable=fieldString)
    btnAddField     = ttk.Button(content, text="Add",       command=addField)
    btnRemField     = ttk.Button(content, text="Remove",    command=removeField)
    btnEdtField     = ttk.Button(content, text="Edit",      command=editField)
    btnParse        = ttk.Button(content, text="Parse",     command=parse)
    btnCancel       = ttk.Button(content, text="Cancel",    command=root.destroy)

    txtSeparator    = ttk.Entry(content,    textvariable=tokenSeparator)


    # Component Placement in grid
    content.grid        (column=0, row=0)
    lblBrowse.grid      (column=0, row=0, columnspan=4)
    btnBrowse.grid      (column=0, row=1)
    txtAddField.grid    (column=0, row=2)
    btnAddField.grid    (column=0, row=3)
    lbxFields.grid      (column=0, row=4)
    btnEdtField.grid    (column=0, row=5)
    btnRemField.grid    (column=0, row=6)
    btnParse.grid       (column=0, row=7)
    btnCancel.grid      (column=0, row=8)

    root.mainloop()


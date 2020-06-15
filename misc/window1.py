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
        index = int(lbxFields.curselection()[0])
        lbxFields.insert(index, fieldString.get())
        lbxFields.delete(index+1)
        

    def removeField():
        idx = lbxFields.curselection()
        lbxFields.delete(idx)

    def moveUp():
        idx = lbxFields.curselection()[0]
        if idx == 0:
            return None
        above = idx-1
        abv_txt = lbxFields.get(above)
        lbxFields.delete(above)
        lbxFields.insert(idx, abv_txt)


    def moveDn():
        idx = lbxFields.curselection()[0]
        if idx == lbxFields.size()-1:
            return None
        txt = lbxFields.get(idx)
        lbxFields.delete(idx)
        lbxFields.insert(idx+1, txt)


    def parse():
        fields = fields_list.get()[1:-1].split(',') # removes parantheses
        if fields[1] == '':
            fields = fields[:-1] # removes empty item when size is 1
        output = dict()
        for field in fields:
            field = field[1:-1] # removes single quotes
            name = field.split(':')[0]
            datatype = field.split(':')[1]
            output[name] = datatype
        print(output)

        

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
    fields_list.set(('a:i', 'b:f', 'c:d'))
    

    # Component Creation
    lblBrowse       = ttk.Label(content,    textvariable=logFilename)

    btnBrowse       = ttk.Button(content, text="Browse",    command=browseLog)
    lbxFields       = Listbox(content,    selectmode="SINGLE", listvariable=fields_list)
    txtAddField     = ttk.Entry(content,  textvariable=fieldString)
    btnAddField     = ttk.Button(content, text="Add",       command=addField)
    btnMovDnField   = ttk.Button(content, text="Move Down", command=moveDn)
    btnMovUpField   = ttk.Button(content, text="Move Up",   command=moveUp)

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
    btnMovUpField.grid  (column=1, row=4)
    btnMovDnField.grid  (column=1, row=5)
    btnEdtField.grid    (column=0, row=6)
    btnRemField.grid    (column=0, row=7)
    btnParse.grid       (column=0, row=8)
    btnCancel.grid      (column=0, row=9)

    root.mainloop()

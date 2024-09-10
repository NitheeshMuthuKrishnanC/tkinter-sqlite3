from tkinter import * 
from tkinter import ttk
from database import *
from tkinter import messagebox


window = Tk()
window.title("Employee Management System")
window.geometry("900x500")
window.config(bg = "#EFBC9B")
window.iconbitmap('./asserts/employee.ico')

name = StringVar()
age= StringVar()
doj = StringVar()
address = StringVar()
gender = StringVar()
#Entries

entries = Frame(window , bg = "#27374D")
entries.pack(side= "top", fill= X)
title = Label(entries , text= "Employees Management Service" , font= ("Calibri" , 18 , "bold") , fg="white", bg="#27374D", padx= 10, pady= 10)
title.grid(row= 0 , columnspan= 2, sticky='w')

# Name
lName = Label(entries , text = "Name",font= ("Calibri" , 14 ) , fg="white", bg="#27374D" , padx= 10 , pady= 5)
lName.grid(row=1,column=0)
lTextN = Entry(entries , width= 20 ,textvariable = name,font= ("Calibri" , 14 ))
lTextN.grid(row= 1 , column= 1,sticky='w')

#Age
lName = Label(entries , text = "Age",font= ("Calibri" , 14 ) , fg="white", bg="#27374D" , padx= 10 , pady= 5)
lName.grid(row=1,column=3)
lTextA = Entry(entries , width= 20 ,textvariable = age,font= ("Calibri" , 14 ))
lTextA.grid(row= 1 , column= 4,sticky='w')

#Gender
lName = Label(entries , text= "Gender",font= ("Calibri" , 14 ) , fg="white", bg="#27374D" , padx= 10 , pady= 5)
lName.grid(row= 2 , column= 0)
lTextG = ttk.Combobox(entries,width= 18,font= ("Calibri" , 14 ),textvariable= gender)
lTextG['values'] = ('Male','Female','Trans','Others')
lTextG.grid(row=2 , column= 1,sticky='w')

#Date OF Join
lName = Label(entries , text = "Date of join ",font= ("Calibri" , 14 ) , fg="white", bg="#27374D" , padx= 10 , pady= 5)
lName.grid(row=2,column=3)
lTextD = Entry(entries , width=  20,textvariable = doj,font= ("Calibri" , 14 ))
lTextD.grid(row= 2 , column= 4 , sticky= "w")



#Address

lName = Label(entries , text = "Address",font= ("Calibri" , 14 ) , fg="white", bg="#27374D" , padx= 10 , pady= 5)
lName.grid(row=3,column=0)
lTextAd = Text(entries , height=2,width= 70 ,font= ("Calibri" , 14 ))
lTextAd.grid(row= 4 , column= 0 , columnspan= 5 ,sticky='w',padx=20)

def getData(e):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row 
    row = data['values']

    name.set(row[1])
    age.set(row[2])
    doj.set(row[3])
    gender.set(row[4])
    lTextAd.delete(1.0,END)
    lTextAd.insert(END,row[5])

def displayAll():
    tv.delete(*tv.get_children())
    for row in fetch():
        tv.insert("",END,values= row)

def add_emp():
    if lTextN.get() == "" or lTextA.get() == "" or lTextAd.get(1.0,END) == "" or lTextG.get() == "" or lTextD.get() == "":
        messagebox.showerror("Enter vaild input ","Fill all details")
    else:
        insert(lTextN.get(),lTextA.get(),lTextD.get(),lTextG.get(),lTextAd.get(1.0,END))
        messagebox.showinfo("Success","Values insertes to DB")

    clearAll()
    displayAll()

def update_emp():
    if lTextN.get() == "" or lTextA.get() == "" or lTextAd.get(1.0,END) == "" or lTextG.get() == "" or lTextD.get() == "":
        messagebox.showerror("Enter vaild input ","Fill all details")
    else:
        update(row[0],lTextN.get(),lTextA.get(),lTextD.get(),lTextG.get(),lTextAd.get(1.0,END))
        messagebox.showinfo("Success","Values Updated")

    clearAll()
    displayAll()

def delete_emp():
    remove(row[0])

    clearAll()
    displayAll()

def clearAll():
    name.set("")
    age.set("")
    doj.set("")
    gender.set("")
    lTextAd.delete(1.0,END)

btn_frame = Frame(entries , bg="#27374D" ,padx= 20)
btn_frame.grid(row= 6 , column= 0, columnspan=4,padx= 10, pady= 10 , sticky= 'w')

btnAdd = Button(btn_frame,command= add_emp,text= 'Add employee',font= ("Calibri" , 14 ) , fg="white", bg="#9BCF53",bd = 0).grid(row=0, column=0 , padx= 10)

btnUpdate = Button(btn_frame,command= update_emp,text= 'Update employee',font= ("Calibri" , 14 ) , fg="white", bg="#378CE7",bd = 0).grid(row=0, column=1 , padx= 10)

btnDelete = Button(btn_frame,command= delete_emp,text= 'Delete Employee',font= ("Calibri" , 14 ) , fg="white", bg="#E72929",bd = 0).grid(row=0, column=2 , padx= 10)

btnClear = Button(btn_frame,command= clearAll,text= 'Clear all',font= ("Calibri" , 14 ) , fg="white", bg="#3D3B40",bd = 0).grid(row=0, column=3 , padx= 10)



#Tree Frame
tree_frame = Frame(window , bg="#9CAFAA")
tree_frame.place(x = 0, y=269,width= 900, height= 600)

style = ttk.Style()
style.configure("mystyle.Treeview",font= ("Calibri" , 10 ),rowheight = 50,columnheight = 5)


tv = ttk.Treeview(tree_frame,columns= (1,2,3,4,5,6),style= "mystyle.Treeview")
tv.heading("1",text= "ID")
tv.column("1", width= 2)
tv.heading("2",text= "Name")
tv.column("2", width= 10)
tv.heading("3",text= "Age")
tv.column("3",width=5)
tv.heading("4",text= "DOJ")
tv.column("4", width= 5)
tv.heading("5",text= "Gender")
tv.column("5", width= 10)
tv.heading("6",text= "Address")
tv.column("6", width= 10)

tv.bind('<ButtonRelease-1>',getData)
tv['show'] = 'headings'
tv.pack(fill= X)

displayAll()
window.mainloop()
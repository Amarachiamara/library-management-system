from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import sqlite3
from sqlite3 import Error
import os
import sys
py = sys.executable

#creating window
class Add(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'libico.ico')
        self.maxsize(500,500)
        self.minsize(500,500)
        self.title('Add User')
        f = StringVar()
        a = StringVar()
        b = StringVar()
        c = StringVar()
        d = StringVar()
        e = StringVar()
#uploading image
        def convertToBinaryData(filename):
            with open(filename, 'rb') as file:
                blobData = file.read()
            return blobData
#verifying input
        def asi():
            if len(f.get()) < 1:
                messagebox.showinfo("Oop's", "Please Enter Your Class Roll Number")
            elif len(a.get()) < 1:
                messagebox.showinfo("Oop's","Please Enter Your User Name")
            elif len(b.get()) < 1:
                messagebox.showinfo("Oop's", "Please Enter Your User Id")
            elif len(c.get()) < 1:
                messagebox.showinfo("Oop's", "Please Enter Your User class")
            elif len(d.get()) < 10 or len(d.get()) > 10:
                messagebox.showinfo("Oop's", "Please Enter Your User Tel Number")
            elif len(e.get()) < 1:
                messagebox.showinfo("Error", "Please Select a Image")
            else:
                try:
                    self.conn = sqlite3.connect('library_administration.db')
                    self.myCursor = self.conn.cursor()
                    pc = self.myCursor.execute("Insert into students('Roll_no','name','Student_Id','class','Phone_number','Image') values (?,?,?,?,?,?)",[f.get(),a.get(),b.get(),c.get(),d.get(),convertToBinaryData(e.get())])
                    self.conn.commit()
                    if pc:
                        messagebox.showinfo("Done","User Inserted Successfully")
                        ask = messagebox.askyesno("Confirm","Do you want to add another user?")
                        if ask:
                            self.destroy()
                            os.system('%s %s' % (py, 'Add_Student.py'))
                        else:
                            self.destroy()
                    else:
                        messagebox.showerror("Error","Something goes wrong")
                    self.myCursor.close()
                    self.conn.close()
                except Error:
                    messagebox.showerror("Error","Something goes wrong")

        # label and input box
        label4 = Label(self, text='Student Details', fg='red', font=('Arial', 25, 'bold')).pack()
        lbl = Label(self, text='Class Roll Number:', font=('Comic Scan Ms', 10, 'bold')).place(x=70, y=82)
        S_name = Entry(self, textvariable=f, width=30).place(x=200, y=84)
        label = Label(self, text='Student Name:', font=('Comic Scan Ms', 10, 'bold')).place(x=70, y=130)
        S_name = Entry(self, textvariable=a, width=30).place(x=200, y=132)
        label5 = Label(self, text='Student Id:', font=('Comic Scan Ms', 10, 'bold')).place(x=70, y=180)
        S_ID = Entry(self, textvariable=b, width=30).place(x=200, y=182)
        label6 = Label(self, text='Student Class:', font=('Comic Scan Ms', 10, 'bold')).place(x=70, y=230)
        S_Class = Entry(self, textvariable=c, width=30).place(x=200, y=232)
        label7 = Label(self, text='Phone Number:', font=('Comic Scan Ms', 10, 'bold')).place(x=70, y=280)
        def fileDialog():
            filename = filedialog.askopenfilename(initialdir = "/",title = "Select A File",filetype = (("jpeg","*.jpg"),("png","*.png"),("All Files","*.*")))
            e.set(filename)
        label8 = Label(self,text="Upload image", font=('Comic Scan Ms', 10, 'bold')).place(x=70,y=330)
        upload_image = Entry(self,textvariable = e,width = 30).place(x=200,y=330)
        butt=Button(self,text="Browse",width=7,command=fileDialog).place(x=400,y=328)
        S_phone_number = Entry(self, textvariable=d, width=30).place(x=200, y=282)
        S_butt = Button(self, text="Submit",width = 15,command=asi).place(x=230, y=390)

Add().mainloop()
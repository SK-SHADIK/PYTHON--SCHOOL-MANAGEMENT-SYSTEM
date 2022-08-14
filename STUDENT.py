from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk  # FROM PILLOW LIBARIRY WE TAKE FOR IMAGES
import pymysql #FOR DATABASE



class  STUDENT:
    def __init__(self,root):
        self.root=root
        self.root.title("STUDENT") #WINDOW NAME
        self.root.geometry("1920x700+0+0") #WINDOW SIZE

        #FOR BACKGROUND IMAGE
        self.bg=ImageTk.PhotoImage(file="IMG/STUDENT.jpg")
        bg=Label(self.root,image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        #variable
        self.SLNO=StringVar()
        self.ID=StringVar()
        self.NAME=StringVar()
        self.EMAIL=StringVar()
        self.CONTACT=StringVar()
        self.DOB=StringVar()
        self.GENDER=StringVar()
        self.SEARCH_BY=StringVar()
        self.SEARCH_TXT=StringVar()

        #TITLE
        title=Label(self.root, text="SCHOOL MANAGEMENT SYSTEM --- STUDENT", font=("times new roman",40,"bold"), bg="orange").pack(side=TOP, fill=X)

        #FROM 

        From=Frame(self.root, bd=5, relief=RIDGE, bg="salmon").place(x=20, y=100, width=500, height=580)

        From_title=Label(From, text="STUDENT FROM: ", bg="salmon", fg="green", font=("times new roman",20,"bold")).place(x=30, y=110)

        slno=Label(From, text="SLNO NUMBER: ", bg="salmon", fg="black", font=("times new roman",18,"bold")).place(x=30, y=150, width=200, height=20)
        txt_slno=Entry(From,textvariable=self.SLNO, font=("times new roman",15,"bold"), bd=5).place(x=250, y=150, width=200, height=30)

        Id=Label(From, text="ID NUMBER: ", bg="salmon", fg="black", font=("times new roman",18,"bold")).place(x=30, y=200, width=200, height=20)
        txt_Id=Entry(From, font=("times new roman",15,"bold"),textvariable=self.ID, bd=5).place(x=250, y=200, width=200, height=30)

        name=Label(From, text="NAME: ", bg="salmon", fg="black", font=("times new roman",18,"bold")).place(x=30, y=250, width=200, height=20)
        txt_name=Entry(From, font=("times new roman",15,"bold"), bd=5,textvariable=self.NAME).place(x=250, y=250, width=200, height=30)

        email=Label(From, text="EMAIL: ", bg="salmon", fg="black", font=("times new roman",18,"bold")).place(x=30, y=300, width=200, height=20)
        txt_email=Entry(From, font=("times new roman",15,"bold"), bd=5,textvariable=self.EMAIL).place(x=250, y=300, width=200, height=30)

        cont=Label(From, text="CONTACT NUMBER: ", bg="salmon", fg="black", font=("times new roman",15,"bold")).place(x=30, y=350, width=200, height=20)
        txt_cont=Entry(From, font=("times new roman",15,"bold"), bd=5,textvariable=self.CONTACT).place(x=250, y=350, width=200, height=30)

        dob=Label(From, text="DOB: ", bg="salmon", fg="black", font=("times new roman",18,"bold")).place(x=30, y=400, width=200, height=20)
        txt_dob=Entry(From, font=("times new roman",15,"bold"), bd=5, textvariable=self.DOB).place(x=250, y=400, width=200, height=30)

        address=Label(From, text="ADDRESS: ", bg="salmon", fg="black", font=("times new roman",18,"bold")).place(x=30, y=450, width=200, height=20)
        self.txt_address=Entry(From, font=("times new roman",15,"bold"), bd=5)
        self.txt_address.place(x=250, y=450, width=200, height=50)

        gender=Label(From, text="GENDER: ", bg="salmon", fg="black", font=("times new roman",18,"bold")).place(x=30, y=520, width=200, height=20)
        self.comb_gender=ttk.Combobox(From, font=("times new roman",15,"bold"), state='readonly',justify=CENTER,textvariable=self.GENDER)
        self.comb_gender['values']=("Select One","MALE","FEMALE","OTHER")
        self.comb_gender.place(x=250, y=520, width=200, height=30)
        self.comb_gender.current(0)

        #BUTTON

        btn=Frame(From, bd=5, relief=RIDGE, bg="aqua").place(x=30, y=600, width=470) #BAR

        addbtn=Button(btn, text="Add", font=("times new roman",15,"bold"), bg="green", fg="white",cursor="hand2", command=self.add_data).place(x=30, y=620, width=100, height=40)

        updatebtn=Button(btn, text="Update", font=("times new roman",15,"bold"), bg="black", fg="white", cursor="hand2", command=self.update_data).place(x=150, y=620, width=100, height=40)

        deletebtn=Button(btn, text="Delete", font=("times new roman",15,"bold"), bg="red", fg="white", cursor="hand2", command=self.delete_data).place(x=270, y=620, width=100, height=40)

        clearbtn=Button(btn, text="Clear", font=("times new roman",15,"bold"), bg="black", fg="white", cursor="hand2", command=self.clear_data).place(x=390, y=620, width=100, height=40)

        #VIEW DETAILS

        details=Frame(self.root, bd=5, relief=RIDGE, bg="coral").place(x=530, y=100, width=980, height=580)

        search=Label(details, text="SEARCH BY: ", font=("time new roman",12,"bold"),bg="coral",fg="white",).place(x=550, y=110)
        self.comb_search=ttk.Combobox(details, font=("times new roman",12,"bold"), state='readonly',justify=CENTER, textvariable=self.SEARCH_BY)
        self.comb_search['values']=("ID","NAME","CONTACT")
        self.comb_search.place(x=680, y=110, width=200, height=30)
        self.comb_search.current(0)

        txt_search=Entry(details, font=("times new roman",15,"bold"), bd=5, textvariable=self.SEARCH_TXT).place(x=900, y=110, width=200, height=30)

        searchbtn=Button(btn, text="SEARCH", font=("times new roman",15,"bold"), bg="black", fg="white",cursor="hand2", command=self.search_data).place(x=1130, y=110, width=120, height=30)

        showallbtn=Button(btn, text="SHOW ALL", font=("times new roman",15,"bold"), bg="black", fg="white", cursor="hand2", command=self.fetch_data).place(x=1270, y=110, width=120, height=30)

        exitbtn=Button(btn, text="EXIT", font=("times new roman",15,"bold"), bg="black", fg="white", cursor="hand2", command=self.exit).place(x=1400, y=110, width=80, height=30)
        

        #TABLE SECTION
        table=Frame(details, bd=5, relief=RIDGE, bg="seagreen")
        table.place(x=550, y=150, width=950, height=520)

        #FOOTER
        footer=Label(self.root, text="copyright @ 2022 --- SMS", font=("times new roman",8,"bold"), bg="orange").pack(side=BOTTOM, fill=X)


        #SCROOLBAR
        scrollx=Scrollbar(table,orient=HORIZONTAL)
        scrolly=Scrollbar(table,orient=VERTICAL)

        self.student_table=ttk.Treeview(table,column=("SLNO", "ID", "NAME", "EMAIL", "CONTACT NO", "DOB", "ADDRESS", "GENDER"),xscrollcommand=scrolly,yscrollcommand=scrollx)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command=self.student_table.xview)
        scrolly.config(command=self.student_table.yview)

        self.student_table.heading("SLNO",text="SL NO")
        self.student_table.heading("ID",text="ID")
        self.student_table.heading("NAME",text="NAME")
        self.student_table.heading("EMAIL",text="EMAIL")
        self.student_table.heading("CONTACT NO",text="CONTACT NO.")
        self.student_table.heading("DOB",text="DATE OF BIRTH")
        self.student_table.heading("ADDRESS",text="ADDRESS")
        self.student_table.heading("GENDER",text="GENDER")

        self.student_table['show']='headings'
        self.student_table.column("SLNO", width=100)
        self.student_table.column("ID", width=100)
        self.student_table.column("NAME", width=100)
        self.student_table.column("EMAIL", width=120)
        self.student_table.column("CONTACT NO", width=100)
        self.student_table.column("DOB", width=100)
        self.student_table.column("ADDRESS", width=180)
        self.student_table.column("GENDER", width=100)


        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

        #DATABASE WORK
        
    
    def add_data(self):
        if self.ID.get()=="" or self.NAME.get()=="":
            messagebox.showerror("ERROR!!!","NAME AND ID MUST REQUIRED")

        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="STUDENT")
            cur= con.cursor()

            cur.execute("insert into student  values (%s,%s,%s,%s,%s,%s,%s,%s)", (self.SLNO.get(),self.ID.get(),self.NAME.get(),self.EMAIL.get(),self.CONTACT.get(),self.DOB.get(),self.txt_address.get(),self.GENDER.get()))

            con.commit()
            self.fetch_data()
            self.clear_data()
            con.close()
            messagebox.showinfo("SUCCESS","DATA ADDED SUCCESSFULL")

    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="STUDENT")
        cur= con.cursor()
        cur.execute("select * from student")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()
    
    def get_cursor(self,ev):
        cursor_row = self.student_table.focus()
        contents = self.student_table.item(cursor_row)
        row = contents['values']
        self.SLNO.set(row[0])
        self.ID.set(row[1])
        self.NAME.set(row[2])
        self.EMAIL.set(row[3])
        self.CONTACT.set(row[4])
        self.DOB.set(row[5])
        self.txt_address.insert(END, row[6])
        self.GENDER.set(row[7])

    def update_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="STUDENT")
        cur= con.cursor()

        cur.execute("update student set ID=%s,NAME=%s,EMAIL=%s,CONTACT=%s,DOB=%s,ADDRESS=%s,GENDER=%s where SL_NO=%s", (
                                                                                                      self.ID.get(),
                                                                                                      self.NAME.get(),
                                                                                                      self.EMAIL.get(),
                                                                                                      self.CONTACT.get(),
                                                                                                      self.DOB.get(),
                                                                                                      self.txt_address.get(),
                                                                                                      self.GENDER.get(),
                                                                                                      self.SLNO.get()
                                                                                                      ))

        con.commit()
        self.fetch_data()
        self.clear_data()
        con.close()
        messagebox.showinfo("SUCCESS","DATA UPDATE SUCCESSFULL")

    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="STUDENT")
        cur= con.cursor()

        cur.execute("delete from student where ID=%s",self.ID.get())

        con.commit()
        con.close()
        self.fetch_data()
        self.clear_data()


    def clear_data(self):
        self.SLNO.set("")
        self.ID.set("")
        self.NAME.set("")
        self.EMAIL.set("")
        self.CONTACT.set("")
        self.DOB.set("")
        self.txt_address.delete(0,END)
        self.comb_gender.current(0)

    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="STUDENT")
        cur= con.cursor()

        cur.execute("select * from student where "+ str(self.SEARCH_BY.get()) +" Like '%"+str(self.SEARCH_TXT.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END, values=row)
            con.commit()
        con.close()

    
    def exit(self):
        self.root.destroy()
        import DASHBOARD
        
        
                    
        



        


root=Tk()
obj=STUDENT(root)
root.mainloop()
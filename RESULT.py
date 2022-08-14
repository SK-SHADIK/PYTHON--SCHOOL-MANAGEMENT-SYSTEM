from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk  # FROM PILLOW LIBARIRY WE TAKE FOR IMAGES
import pymysql #FOR DATABASE
from tkcalendar import * #FOR CALENDAR

class  RESULT:
    def __init__(self,root):
        self.root=root
        self.root.title("RESULT") #WINDOW NAME
        self.root.geometry("2000x700+0+0") #WINDOW SIZE

        #FOR BACKGROUND IMAGE
        self.bg=ImageTk.PhotoImage(file="IMG/RESULT.jpg")
        bg=Label(self.root,image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)


        #TITLE BAR        
        title=Label(self.root, text="SCHOOL MANAGEMENT SYSTEM --- RESULT", font=("times new roman",40,"bold"), bg="orange").pack(side=TOP, fill=X)
        
        #VARIABLE
        self.ID=StringVar()
        self.NAME=StringVar()
        self.COURSE=StringVar()
        self.MARKS=StringVar()
        self.FULLMARKS=StringVar()
        self.ID_LIST=[]
        self.fetch_ID()

        select=Label(self.root, text="Select Student ID: ", font=("times new roman",20,"bold"), bg="aqua", fg="black").place(x=50, y=100)       
        name=Label(self.root, text="NAME: ", font=("times new roman",20,"bold"), bg="aqua", fg="black").place(x=50, y=160) 
        course=Label(self.root, text="COURSE: ", font=("times new roman",20,"bold"), bg="aqua", fg="black").place(x=50, y=220)       
        marks=Label(self.root, text="MARKS: ", font=("times new roman",20,"bold"), bg="aqua", fg="black").place(x=50, y=280)       
        fullmarks=Label(self.root, text="FULL MARKS: ", font=("times new roman",20,"bold"), bg="aqua", fg="black").place(x=50, y=340)  

        self.cmbo_student=ttk.Combobox(self.root, textvariable=self.ID, values=self.ID_LIST, font=("times new roman",15,"bold"), state='readonly',justify=CENTER)
        self.cmbo_student.set("Select")
        self.cmbo_student.place(x=320, y=100, width=200)
        self.cmbo_student.current(0)

        searchbtn=Button(self.root, text="SEARCH", font=("times new roman",15,"bold"), bg="salmon", fg="white",cursor="hand2", command=self.search_data).place(x=550, y=100, width=120, height=30)
        
        name=Entry(self.root, textvariable=self.NAME, font=("times new roman",15,"bold"),bg="lightgray", state='readonly').place(x=280, y=160, width=400)
        course=Entry(self.root, textvariable=self.COURSE, font=("times new roman",15,"bold"),bg="lightgray").place(x=280, y=220, width=400)
        marks=Entry(self.root, textvariable=self.MARKS, font=("times new roman",15,"bold"),bg="lightgray").place(x=280, y=280, width=400)
        fullmarks=Entry(self.root, textvariable=self.FULLMARKS, font=("times new roman",15,"bold"),bg="lightgray").place(x=280, y=340, width=400)

        #BUTTON
        add=Button(self.root, text="SAVE", font=("times new roman",15,"bold"), bg="salmon", fg="white",cursor="hand2", command=self.add_data).place(x=500, y=420, width=120, height=30)
        

        cancel=Button(self.root, text="CLEAR DATA", font=("times new roman",20,"bold"),bd=15, relief=RIDGE, bg="salmon", cursor="hand2", fg="white",command=self.clear_data)
        cancel.place(x=900,  y=180, width=300, height=100)

        vr=Button(self.root, text="VIEW RESULT", font=("times new roman",20,"bold"),bd=15, relief=RIDGE, bg="salmon", cursor="hand2", fg="white", command=self.viewresult)
        vr.place(x=900,  y=380, width=300, height=100)

        exit=Button(self.root, text="EXIT", font=("times new roman",20,"bold"),bd=15, relief=RIDGE, bg="salmon", cursor="hand2", fg="white", command=self.exit)
        exit.place(x=900,  y=500, width=300, height=100)
        
        #FOOTER
        footer=Label(self.root, text="copyright @ 2022 --- SMS", font=("times new roman",8,"bold"), bg="orange").pack(side=BOTTOM, fill=X)


    def fetch_ID(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="STUDENT")
        cur= con.cursor()

        cur.execute("select ID from student")
        rows=cur.fetchall()
        if len(rows)>0:
            for row in rows:
                self.ID_LIST.append(row[0])
    

    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="STUDENT")
        cur= con.cursor()

        
        cur.execute("select NAME from student where ID=%s",(self.ID.get()))
        row=cur.fetchone()
        if row!=None:
            self.NAME.set(row[0])
        else:
            messagebox.showerror("ERROR!!!","NO RECOARD FOUND",parent=self.root)
        
    def add_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="STUDENT")
        cur= con.cursor()

        if self.NAME.get()=="":
            messagebox.showerror("ERROR!!!","PLEASE SEARCH A ID FIRST")
        else:
            cur.execute("select * from result where ID=%s and name=%s",(self.ID.get(),self.NAME.get()))
            row=cur.fetchone()
            
            PER=(int(self.MARKS.get())*100)/int(self.FULLMARKS.get())
            cur.execute("insert into result (ID,NAME,COURSE,MARKS,FULLMARKS,PER) values(%s,%s,%s,%s,%s,%s)",(self.ID.get(),self.NAME.get(),self.COURSE.get(),self.MARKS.get(),self.FULLMARKS.get(),str(PER)))
            con.commit()
            con.close()
    
    def clear_data(self):
        self.ID.set("")
        self.NAME.set("")
        self.COURSE.set("")
        self.MARKS.set("")
        self.FULLMARKS.set("")
        self.cmbo_student.current(0)

    def exit(self):
        self.root.destroy()
        import DASHBOARD

    def viewresult(self):
        self.root.destroy()
        import VIEWRESULT



            
        
    
                

            
        

root=Tk()
obj=RESULT(root)
root.mainloop()
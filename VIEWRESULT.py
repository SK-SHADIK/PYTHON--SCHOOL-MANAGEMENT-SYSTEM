from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk  # FROM PILLOW LIBARIRY WE TAKE FOR IMAGES
import pymysql #FOR DATABASE
from tkcalendar import * #FOR CALENDAR

class  VIEWRESULT:
    def __init__(self,root):
        self.root=root
        self.root.title("VIEW RESULT") #WINDOW NAME
        self.root.geometry("2000x700+0+0") #WINDOW SIZE

        #FOR BACKGROUND IMAGE
        self.bg=ImageTk.PhotoImage(file="IMG/VIEWRESULT.jpg")
        bg=Label(self.root,image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)


        #TITLE BAR        
        title=Label(self.root, text="SCHOOL MANAGEMENT SYSTEM --- VIEW RESULT", font=("times new roman",40,"bold"), bg="orange").pack(side=TOP, fill=X)
        
        #VARIABLE
        self.ID=StringVar()
        self.ID_LIST=[]
        self.fetch_ID()


        select=Label(self.root, text="Select Student ID: ", font=("times new roman",18,"bold"), bg="aqua", fg="white").place(x=400, y=100) 

        self.cmbo_student=ttk.Combobox(self.root, textvariable=self.ID, values=self.ID_LIST, font=("times new roman",15,"bold"), state='readonly',justify=CENTER)
        self.cmbo_student.set("Select")
        self.cmbo_student.place(x=630, y=100, width=200)
        self.cmbo_student.current(0)      

        searchbtn=Button(self.root, text="SEARCH", font=("times new roman",15,"bold"), bg="salmon", fg="white",cursor="hand2", command=self.search_data).place(x=850, y=100, width=120, height=30)
        result=Button(self.root, text="RESULT", font=("times new roman",15,"bold"), bg="black", fg="white",cursor="hand2",command=self.resultpage).place(x=1000, y=100, width=120, height=30)
        
        lbl_id=Label(self.root, text="ID", font=("times new roman",15,"bold"), bg="white", fg="black", bd=3, relief=GROOVE).place(x=150, y=230, width=150, height=50)
        lbl_name=Label(self.root, text="NAME", font=("times new roman",15,"bold"), bg="white", fg="black", bd=3, relief=GROOVE).place(x=300, y=230, width=150, height=50)
        lbl_course=Label(self.root, text="COURSE", font=("times new roman",15,"bold"), bg="white", fg="black", bd=3, relief=GROOVE).place(x=450, y=230, width=150, height=50)
        lbl_marks=Label(self.root, text="MARKS", font=("times new roman",15,"bold"), bg="white", fg="black", bd=3, relief=GROOVE).place(x=600, y=230, width=150, height=50)
        lbl_fullmarks=Label(self.root, text="TOTAL MARKS", font=("times new roman",15,"bold"), bg="white", fg="black", bd=3, relief=GROOVE).place(x=750, y=230, width=150, height=50)
        lbl_per=Label(self.root, text="PERSENTAGE", font=("times new roman",15,"bold"), bg="white", fg="black", bd=3, relief=GROOVE).place(x=900, y=230, width=150, height=50)

        self.id=Label(self.root, font=("times new roman",15,"bold"), bg="white", fg="black", bd=3, relief=GROOVE)
        self.id.place(x=150, y=280, width=150, height=50)
        self.name=Label(self.root, font=("times new roman",15,"bold"), bg="white", fg="black", bd=3, relief=GROOVE)
        self.name.place(x=300, y=280, width=150, height=50)
        self.course=Label(self.root, font=("times new roman",15,"bold"), bg="white", fg="black", bd=3, relief=GROOVE)
        self.course.place(x=450, y=280, width=150, height=50)
        self.marks=Label(self.root, font=("times new roman",15,"bold"), bg="white", fg="black", bd=3, relief=GROOVE)
        self.marks.place(x=600, y=280, width=150, height=50)
        self.fullmarks=Label(self.root, font=("times new roman",15,"bold"), bg="white", fg="black", bd=3, relief=GROOVE)
        self.fullmarks.place(x=750, y=280, width=150, height=50)
        self.per=Label(self.root, font=("times new roman",15,"bold"), bg="white", fg="black", bd=3, relief=GROOVE)
        self.per.place(x=900, y=280, width=150, height=50)

        
        clearbtn=Button(self.root, text="CLEAR", font=("times new roman",15,"bold"), bg="black", fg="white",cursor="hand2", command=self.clear_data).place(x=600, y=350, width=120, height=50)
        
        exit=Button(self.root, text="EXIT", font=("times new roman",15,"bold"), bg="black", fg="white",cursor="hand2", command=self.exit).place(x=600, y=450, width=120, height=50)
        
        #FOOTER
        footer=Label(self.root, text="copyright @ 2022 --- SMS", font=("times new roman",8,"bold"), bg="orange").pack(side=BOTTOM, fill=X)

    def fetch_ID(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="STUDENT")
        cur= con.cursor()

        cur.execute("select ID from result")
        rows=cur.fetchall()
        if len(rows)>0:
            for row in rows:
                self.ID_LIST.append(row[0])
    
    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="STUDENT")
        cur= con.cursor()

        
        cur.execute("select * from result where ID=%s",(self.ID.get()))
        row=cur.fetchone()
        if row!=None:
            self.id.config(text=row[0])
            self.name.config(text=row[1])
            self.course.config(text=row[2])
            self.marks.config(text=row[3])
            self.fullmarks.config(text=row[4])
            self.per.config(text=row[5])
        else:
            messagebox.showerror("ERROR!!!","NO RECOARD FOUND",parent=self.root)

    def clear_data(self):
        self.id.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.marks.config(text="")
        self.fullmarks.config(text="")
        self.per.config(text="")

    def exit(self):
        self.root.destroy()
        import DASHBOARD

    def resultpage(self):
        self.root.destroy()
        import RESULT
        
        
    
        
        


root=Tk()
obj=VIEWRESULT(root)
root.mainloop()
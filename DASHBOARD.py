from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk  # FROM PILLOW LIBARIRY WE TAKE FOR IMAGES
import pymysql #FOR DATABASE
from tkcalendar import * #FOR CALENDAR

class  DASHBOARD:
    def __init__(self,root):
        self.root=root
        self.root.title("DASHBOARD") #WINDOW NAME
        self.root.geometry("2000x700+0+0") #WINDOW SIZE

        #FOR BACKGROUND IMAGE
        self.bg=ImageTk.PhotoImage(file="IMG/STUDENT.jpg")
        bg=Label(self.root,image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        #TITLE BAR        
        title=Label(self.root,text="WELCOME TO OUR STUDENT MANAGEMENT SYSTEM", font=("times new roman",20,"bold"), bg="orange").place(x=0, y=0, relwidth=1, height=50)

        aboutus_btn=Button(self.root, text="ABOUT US", font=("times new roman",15,"bold"), bg="orange", fg="white", cursor="hand2", command=self.aboutus).place(x=1200, y=10, width=150, height=30)

        contactus_btn=Button(self.root, text="CONTACT US", font=("times new roman",15,"bold"), bg="orange", fg="white", cursor="hand2", command=self.contactus).place(x=1370, y=10, width=150, height=30)
        
        
        #MENU BAR
        Menu=LabelFrame(self.root, text="MENU BAR", font=("times new roman",18,"bold"), bg="salmon")
        Menu.place(x=15, y=80, width=1500, height=80)

        #MENU BUTTONS
        btn_student=Button(Menu, text="STUDENT", font=("times new roman",15,"bold"),bg="salmon",fg="white", cursor="hand2", command=self.studentpage).place(x=20, y=5, width=200, height=40)

        btn_teacher=Button(Menu, text="TEACHER", font=("times new roman",15,"bold"),bg="salmon",fg="white", cursor="hand2", command=self.teacherpage).place(x=240, y=5, width=200, height=40)

        btn_result=Button(Menu, text="ADD RESULT", font=("times new roman",15,"bold"),bg="salmon",fg="white", cursor="hand2", command=self.resultpage).place(x=460, y=5, width=200, height=40)

        btn_viewresult=Button(Menu, text="VIEW RESULT", font=("times new roman",15,"bold"),bg="salmon",fg="white", cursor="hand2", command=self.viewresultpage).place(x=680, y=5, width=220, height=40)

        btn_logout=Button(Menu, text="LOGOUT", font=("times new roman",15,"bold"),bg="salmon",fg="white", cursor="hand2", command=self.logout).place(x=920, y=5, width=200, height=40)

        #CALENDER
        date=Label(self.root,text="TO DAYS DATE IS: ", font=("times new roman",12,"bold"), bg="aqua").place(x=15, y=180)

        mycalendar=Calendar(root,setmode="day",date_pattern='d/m/yy')
        mycalendar.place(x=15, y=200, width=480, height=480)


        #UPDATE DETAILS STUDENT NUMBER TEACHER NUMBER 
        self.tStudent=Label(self.root, text="TOTAL STUDENT \n [ 0 ]", font=("times new roman",20,"bold"),bd=15, relief=RIDGE, bg="seagreen", cursor="hand2", fg="white")
        self.tStudent.place(x=550,  y=180, width=300, height=100)

        self.tTeacher=Label(self.root, text="TOTAL TEACHER \n [ 0 ]", font=("times new roman",20,"bold"),bd=15, relief=RIDGE, bg="seagreen", cursor="hand2", fg="white")
        self.tTeacher.place(x=1140,  y=180, width=300, height=100)

        #FOOTER
        footer=Label(self.root,text="copyright @ 2022 --- SMS", font=("times new roman",8,"bold"), bg="orange").pack(side=BOTTOM, fill=X)
        
        self.update_details_student()
        self.update_details_teacher()

    def aboutus(self):
        messagebox.showinfo("ABOUT US","THIS IS OUR STUDENT MANAGEMENT SYSTEM", parent=self.root) 

    def contactus(self):
        messagebox.showinfo("CONTACT US","IF YOU WANT TO CONTACT US THEN HERE IS OUR INFO \n EMAIL : abc@gmail.com \n PHONE NUMBER: 01.........", parent=self.root) 
    
    def update_details_student(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="STUDENT")
        cur= con.cursor()
        cur.execute("select * from student")
        cr=cur.fetchall()
        self.tStudent.config(text=f"TOTAL STUDENT\n[{str(len(cr))}]")

    def update_details_teacher(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="TEACHER")
        cur= con.cursor()
        cur.execute("select * from teacher")
        cr=cur.fetchall()
        self.tTeacher.config(text=f"TOTAL TEACHER\n[{str(len(cr))}]")

        

    def logout(self):
        self.root.destroy()
        import LOGIN

    def studentpage(self):
        self.root.destroy()
        import STUDENT

    def teacherpage(self):
        self.root.destroy()
        import TEACHER

    def resultpage(self):
        self.root.destroy()
        import RESULT

    def viewresultpage(self):
        self.root.destroy()
        import VIEWRESULT
        
        




    

root=Tk()
obj=DASHBOARD(root)
root.mainloop()
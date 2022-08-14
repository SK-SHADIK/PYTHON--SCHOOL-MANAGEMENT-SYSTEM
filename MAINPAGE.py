from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk  # FROM PILLOW LIBARIRY WE TAKE FOR IMAGES
import pymysql #FOR DATABASE

class  MAINPAGE:
    def __init__(self,root):
        self.root=root
        self.root.title("MAIN PAGE") #WINDOW NAME
        self.root.geometry("1920x700+0+0") #WINDOW SIZE

        #FOR BACKGROUND IMAGE
        self.bg=ImageTk.PhotoImage(file="IMG/HOME.jpg")
        bg=Label(self.root,image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        #TITLE BAR        
        title=Label(self.root,text="WELCOME TO OUR STUDENT MANAGEMENT SYSTEM", font=("times new roman",20,"bold"), bg="orange").place(x=0, y=0, relwidth=1, height=50)

        aboutus_btn=Button(self.root, text="ABOUT US", font=("times new roman",15,"bold"), bg="orange", fg="white", cursor="hand2", command=self.aboutus).place(x=1200, y=10, width=150, height=30)

        contactus_btn=Button(self.root, text="CONTACT US", font=("times new roman",15,"bold"), bg="orange", fg="white", cursor="hand2", command=self.contactus).place(x=1370, y=10, width=150, height=30)
        

        btn_signup=Button(self.root, text="SIGNUP", font=("times new roman",20,"bold"),bd=15, relief=RIDGE, bg="salmon", cursor="hand2", fg="white", command=self.signuppage).place(x=150,  y=300, width=300, height=100)

        btn_login=Button(self.root, text="LOGIN", font=("times new roman",20,"bold"),bd=15, relief=RIDGE, bg="salmon", cursor="hand2", fg="white", command=self.loginpage).place(x=1100,  y=300, width=300, height=100)
        #FOOTER
        footer=Label(self.root, text="copyright @ 2022 --- SMS", font=("times new roman",8,"bold"), bg="orange").pack(side=BOTTOM, fill=X)


 

    def aboutus(self):
        messagebox.showinfo("ABOUT US","THIS IS OUR STUDENT MANAGEMENT SYSTEM", parent=self.root) 

    def contactus(self):
        messagebox.showinfo("CONTACT US","IF YOU WANT TO CONTACT US THEN HERE IS OUR INFO \n EMAIL : abc@gmail.com \n PHONE NUMBER: 01.........", parent=self.root) 

    def loginpage(self):
        self.root.destroy()
        import LOGIN

    def signuppage(self):
        self.root.destroy()
        import SIGNUP
    

root=Tk()
obj=MAINPAGE(root)
root.mainloop()
from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk  # FROM PILLOW LIBARIRY WE TAKE FOR IMAGES
import pymysql #FOR DATABASE

class  LOGIN:
    def __init__(self,root):
        self.root=root
        self.root.title("LOGIN PAGE") #WINDOW NAME
        self.root.geometry("1920x1280+0+0") #WINDOW SIZE

        #FOR BACKGROUND IMAGE
        self.bg=ImageTk.PhotoImage(file="IMG/LOGIN.jpg")
        bg=Label(self.root,image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        #IF HAVE NOT ACCOUNT LOGIN
        frame2 = Frame(self.root,bg="green")
        frame2.place(x=480,y=100, width=800, height=600)

        title=Label(frame2,text="NOT SIGNUP", font=("times new roman",20,"bold"), bg="green").place(x=500, y=30)

        title=Label(frame2,text="I DON'T HAVE ANY ACCOUNT", font=("times new roman",15,"bold"), bg="green").place(x=500, y=150)

        #BUTTON

        btn=Button(frame2,text="SIGNUP", bg="white", font=("times new roman",20,"bold"), border="0",cursor="hand2",command=self.signuppage).place(x=500, y=200, width=150)




        #login BOX
        frame1 = Frame(self.root,bg="salmon")
        frame1.place(x=80,y=100, width=800, height=600)

        title=Label(frame1,text="WELCONE BACK...", font=("times new roman",20,"bold"), bg="salmon").place(x=100, y=30)

        #LABELS
        #FIRST & LAST NAME

        u_name=Label(frame1,text="USER NAME", font=("times new roman",18,"bold"), bg="salmon").place(x=200, y=100)
        self.txt_uname=Entry(frame1, font=("times new roman",15,"bold"),bg="lightgray")
        self.txt_uname.place(x=200, y=130, width=250)

        #PASSWORD

        password=Label(frame1,text="PASSWORD", font=("times new roman",18,"bold"), bg="salmon").place(x=200, y=170)
        self.txt_password=Entry(frame1, font=("times new roman",15,"bold"),bg="lightgray")
        self.txt_password.place(x=200, y=200, width=250)


        #FORGET PASSWORD 
        fp=Button(frame1,text="forget password", bg="salmon", font=("times new roman",15), cursor="hand2").place(x=200, y=260)
        
        #BUTTON 

        btn=Button(frame1,text="LOGIN", bg="white", font=("times new roman",20,"bold"), border="0",cursor="hand2", command=self.login_data).place(x=320, y=330, width=150)
        
    def  login_data (self):
        if self.txt_uname.get()=="" or self.txt_password.get()=="":
            messagebox.showerror("ERROR!!!","PLEASE FILL THE ALL INPUT FIELD", parent=self.root) 

            
        
        else:
            try:
                con=pymysql.connect(host="localhost", user="root", password="", database="project_signup")
                cur=con.cursor()
                cur.execute("select * from signup where email=%s and password=%s", (self.txt_uname.get(), self.txt_password.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("ERROR!!!","INVALID USERNAME OR PASSWORD", parent=self.root) 
                
                
                else:
                    self.clear()



            except Exception as es:
                messagebox.showerror("ERROR!!!",f"ERROR FOR: {str(es)}", parent=self.root) 
    
    def clear(self):
        self.txt_uname.delete(0,END)
        self.txt_password.delete(0,END)
        self.root.destroy()
        import DASHBOARD

    def signuppage(self):
        self.root.destroy()
        import SIGNUP

        



    

root=Tk()
obj=LOGIN(root)
root.mainloop()
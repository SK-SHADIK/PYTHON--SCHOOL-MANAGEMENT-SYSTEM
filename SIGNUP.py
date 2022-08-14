from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk  # FROM PILLOW LIBARIRY WE TAKE FOR IMAGES
import pymysql #FOR DATABASE



class  SIGNUP:
    def __init__(self,root):
        self.root=root
        self.root.title("SIGNUP PAGE") #WINDOW NAME
        self.root.geometry("1920x1280+0+0") #WINDOW SIZE

        #FOR BACKGROUND IMAGE
        self.bg=ImageTk.PhotoImage(file="IMG/LOGIN.jpg")
        bg=Label(self.root,image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        #IF HAVE ACCOUNT LOGIN
        frame2 = Frame(self.root,bg="green")
        frame2.place(x=80,y=100, width=800, height=600)

        title=Label(frame2,text="ALREADY SIGNUP", font=("times new roman",20,"bold"), bg="green").place(x=50, y=30)

        title=Label(frame2,text="I ALREADY HAVE AN ACCOUNT", font=("times new roman",15,"bold"), bg="green").place(x=50, y=150)

        #BUTTON

        btn=Button(frame2,text="LOGIN", bg="white", font=("times new roman",20,"bold"), border="0",cursor="hand2", command=self.loginpage).place(x=80, y=200, width=150)




        #REGEESTATION BOX
        frame1 = Frame(self.root,bg="salmon")
        frame1.place(x=480,y=100, width=800, height=600)

        title=Label(frame1,text="WELCOME...", font=("times new roman",20,"bold"), bg="salmon").place(x=50, y=30)

        #LABELS
        #FIRST & LAST NAME

        f_name=Label(frame1,text="FIRST NAME", font=("times new roman",18,"bold"), bg="salmon").place(x=50, y=100)
        self.txt_fname=Entry(frame1, font=("times new roman",15,"bold"),bg="lightgray")
        self.txt_fname.place(x=50, y=130, width=250)
        

        l_name=Label(frame1,text="LAST NAME", font=("times new roman",18,"bold"), bg="salmon").place(x=370, y=100)
        self.txt_lname=Entry(frame1, font=("times new roman",15,"bold"),bg="lightgray")
        self.txt_lname.place(x=370, y=130, width=250)

        #CONTACT

        cont=Label(frame1,text="CONTACT NUMBER", font=("times new roman",18,"bold"), bg="salmon").place(x=50, y=170)
        self.txt_cont=Entry(frame1, font=("times new roman",15,"bold"),bg="lightgray")
        self.txt_cont.place(x=50, y=200, width=250)

        #EMAIL

        email=Label(frame1,text="EMAIL", font=("times new roman",18,"bold"), bg="salmon").place(x=370, y=170)
        self.txt_email=Entry(frame1, font=("times new roman",15,"bold"),bg="lightgray")
        self.txt_email.place(x=370, y=200, width=250)

        #GENDER

        gender=Label(frame1,text="GENDER", font=("times new roman",18,"bold"), bg="salmon").place(x=50, y=240)
        self.cmbo_gender=ttk.Combobox(frame1, font=("times new roman",15,"bold"), state='readonly',justify=CENTER)
        self.cmbo_gender['values']=("Select One","MALE","FEMALE","OTHER")
        self.cmbo_gender.place(x=50, y=270)
        self.cmbo_gender.current(0)

        #PASSWORD

        password=Label(frame1,text="PASSWORD", font=("times new roman",18,"bold"), bg="salmon").place(x=50, y=310)
        self.txt_password=Entry(frame1, font=("times new roman",15,"bold"),bg="lightgray")
        self.txt_password.place(x=50, y=340, width=250)

        #CONFIRM PASSWORD

        cpassword=Label(frame1,text="CONFIRM PASSWORD", font=("times new roman",18,"bold"), bg="salmon").place(x=370, y=310)
        self.txt_cpassword=Entry(frame1, font=("times new roman",15,"bold"),bg="lightgray")
        self.txt_cpassword.place(x=370, y=340, width=250)

        #TREAMS & CONDITIONS 
        self.var_cbox=IntVar()
        cbox=Checkbutton(frame1, text="I AGREE WITH ALL TREAMS & CONDITIONS",variable=self.var_cbox, onvalue=1, offvalue=0, bg="salmon", font=(12)).place(x=50, y=380)

        #BUTTON 

        self.btn=Button(frame1,text="SIGNUP", bg="white", font=("times new roman",20,"bold"), border="0",cursor="hand2", command=self.signup_data).place(x=500, y=420, width=150)

    def signup_data(self):
        if self.txt_fname.get()=="" or self.txt_lname.get()=="" or  self.txt_cont.get()=="" or self.txt_email.get()=="" or self.cmbo_gender.get()=="" or  self.txt_password.get()=="" or  self.txt_cpassword.get()=="":
            messagebox.showerror("ERROR!!!","PLEASE FILL THE ALL INPUT FIELD", parent=self.root) 

        
        elif self.txt_password.get()!=self.txt_cpassword.get():
            messagebox.showerror("ERROR!!!","PASSWORD IS NOT MATCH", parent=self.root) 
        
        elif self.var_cbox.get()==0:
            messagebox.showerror("ERROR!!!","PLEASE AGREE WITH OUR TREAMS AND CONDITION", parent=self.root)             

            
        else:
            try:
                con=pymysql.connect(host="localhost", user="root", password="", database="project_signup")
                cur=con.cursor()
                cur.execute("select * from signup where email=%s", self.txt_email.get())
                row=cur.fetchone()
                #print(row)
                if row!=None:
                    messagebox.showerror("ERROR!!!","USER ALREADY HAS EXIT, PLEASE TRY WITH ANOTHER EMAIL OR LOGIN", parent=self.root) 

                else:
                    cur.execute("insert into signup (f_name,l_name,cont,email,gender,password) values(%s,%s,%s,%s,%s,%s)",
                               (
                                   self.txt_fname.get(),
                                   self.txt_lname.get(),
                                   self.txt_cont.get(),
                                   self.txt_email.get(),
                                   self.cmbo_gender.get(),
                                   self.txt_password.get()
                               ))
                    con.commit()
                    con.close()

                    self.clear()
                    self.root.destroy()
                    import LOGIN

            except Exception as es:
                messagebox.showerror("ERROR!!!",f"ERROR FOR: {str(es)}", parent=self.root) 
    
    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_cont.delete(0,END)
        self.txt_email.delete(0,END)
        self.cmbo_gender.current(0)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)
        self.txt_fname.delete(0,END)
                

    def loginpage(self):
        self.root.destroy()
        import LOGIN
        
        
                 
        



    

root=Tk()
obj=SIGNUP(root)
root.mainloop()
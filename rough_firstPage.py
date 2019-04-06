from tkinter import *
import sqlite3
from tkinter import messagebox
import re
class Login:
    def __init__(self,root):
        #variable declaraion
        self.Lname=StringVar()
        self.Lpass=StringVar()
        self.root=root

        self.root.geometry("640x480")
        self.photo=PhotoImage(file="lpu.png")
        self.label2=Label(self.root,image=self.photo).place(x=0,y=0)
        self.label = Label(self.root, text="Welcome to LPU Cab Booking system", font="Helvetica 14 bold ",).place(x=180,y=10)
        self.canvas=Canvas(self.root,bg="green",height=250, width=300).place(x=180,y=120)
        self.label=Label(self.root,text="Log in into your account",font="Helvetica 10 bold").place(x=250,y=130)
        self.login=Label(self.root,text="Username",font="Helvetica 10 bold").place(x=210,y=180)
        self.entry1=Entry(self.root,textvar=self.Lname).place(x=290,y=180)
        self.login1 = Label(self.root, text="Password", font="Helvetica 10 bold").place(x=210, y=220)
        self.entry2 = Entry(self.root,textvar=self.Lpass,show="*").place(x=290, y=220)
        self.button1 = Button(self.root, text="Login", font="Helvetica 12 bold", bg="orange",padx=30,command=self.login_access1).place(x=280,y=280)
        self.asking=Label(self.root,text="Need An Account?",font="Helvetica 8 bold").place(x=210,y=330)
        self.signup_button=Button(self.root,text="Sign Up",font="Helvetica 9 bold",bg="red",command=self.rg_page).place(x=330,y=330)

    #calling fucnction after clicking on sign up botton
    def rg_page(self):
        top=Toplevel(self.root)
        obj=registration(top)
    def login_access1(self):
        #fething data
        self.Login_name = self.Lname.get()
        self.Login_pass = self.Lpass.get()

        if (self.Login_name == "neeraj" and self.Login_pass == "password"):
            top1=Toplevel(self.root)
            obj1=admin_page(top1)
        elif (self.Login_name=='' and self.Login_pass=='') :
            messagebox.showinfo("warning", "enter username password")
        else:
            self.Costumer_login()
    def Costumer_login(self):
        self.id = self.Lname.get()
        self.id_pass = self.Lpass.get()
        con = sqlite3.connect("Cab booking.db")
        cursur=con.cursor()
        self.find_user = ("select * from costumer_detail where uid=? and password=? ")
        cursur.execute(self.find_user,[(self.Lname.get()),(self.Lpass.get())])
        self.results=cursur.fetchall()
        if self.results:
            self.top3=Toplevel(self.root)
            self.top3.geometry("640x480")
            self.photo_c = PhotoImage(file="Taxi-Booking.png")
            self.label_c = Label(self.top3, image=self.photo_c).place(x=0, y=0)
            con = sqlite3.connect("Cab booking.db")
            self.find_user1 = ("select full_name from costumer_detail where uid=?")
            cursur = con.cursor()
            cursur.execute(self.find_user1, [(self.Lname.get())])
            self.results = cursur.fetchall()
            self.label_c1=Label(self.top3,text="Welcome", font="Helvetica 14 bold ").place(x=250,y=10)
            self.label_c2 = Label(self.top3, text=self.results, font="Helvetica 14 bold ").place(x=340, y=10)
            self.label_c3 = Label(self.top3, text="Book Your Cab With LPU Cab Booking", font="Helvetica 14 bold ",fg='red',bg='cyan').place(x=160, y=50)
            self.canvas_c = Canvas(self.top3, bg="orange", height=250, width=300).place(x=180, y=120)
            self.label_c4 = Label(self.top3, text="Book Your Cab", font="Helvetica 10 bold ").place(x=200, y=140)
            self.button_c = Button(self.top3, text="Book Now", font="Helvetica 10 bold", bg="green", padx=30,command=self.Book_now).place(x=320, y=140)
            self.label_c5 = Label(self.top3, text="Check Booking Status", font="Helvetica 10 bold ").place(x=200, y=200)
            self.button_c1= Button(self.top3, text="Status", font="Helvetica 10 bold", bg="green", padx=30,command=self.check_status).place(x=350, y=200)
            self.button_logout=Button(self.top3,text="Log Out",font="Helvetica 10 bold", bg="gold", padx=30,command=self.gotoback).place(x=350, y=330)
        else:
            messagebox.showinfo("Warning", "Check Username & Password")
        con.commit()
        con.close()
    def check_status(self):
        self.unid=int(self.Lname.get())
        con = sqlite3.connect("Cab booking.db")
        self.find_user1 = ("select status from Booking1 where unid=?")
        cursur = con.cursor()
        cursur.execute(self.find_user1, [(self.unid)])
        self.results = cursur.fetchall()
        if(self.results):
            messagebox.showinfo("Booking Status",self.results[0])
        con.commit()
        con.close()
    def gotoback(self):
        self.master=Toplevel(self.top3)
        Login(self.master)
    def Book_now(self):
        self.top3=Toplevel(self.root)
        Book(self.top3)

class registration:
    def __init__(self,top):
        self.uid=IntVar()
        self.Fname=StringVar()
        self.Email=StringVar()
        self.pswd=StringVar()
        self.rpswd=StringVar()
        self.Mob=IntVar()
        self.gender=StringVar()
        self.master=top
        self.master.geometry("640x480")
        self.photo1 = PhotoImage(file="ibsm-hero-1200.png")
        self.label_1 = Label(self.master, image=self.photo1).place(x=0, y=0)
        self.create=Label(self.master,text="Create Account",font="Helvetica 16 bold",fg="blue").place(x=250,y=30)
        self.usrn=Label(self.master,text="University Id",font='Helvetica 13 bold').place(x=100,y=100)
        self.entry3=Entry(self.master,bd=2,textvar=self.uid).place(x=300,y=100)
        self.usrn1 = Label(self.master, text="Full Name", font='Helvetica 13 bold').place(x=100, y=140)
        self.entry4 = Entry(self.master, bd=2,textvar=self.Fname).place(x=300, y=140)
        self.usrn5 = Label(self.master, text="Email", font='Helvetica 13 bold').place(x=100, y=180)
        self.entry5 = Entry(self.master, bd=2,textvar=self.Email).place(x=300, y=180)
        self.usrn2 = Label(self.master, text="Password", font='Helvetica 13 bold').place(x=100, y=220)
        self.entry6 = Entry(self.master, bd=2,textvar=self.pswd,show="*").place(x=300, y=220)
        self.usrn3 = Label(self.master, text="Re-enter Password", font='Helvetica 13 bold').place(x=100, y=260)
        self.entry7 = Entry(self.master, bd=2,textvar=self.rpswd,show="*").place(x=300, y=260)
        self.usrn4 = Label(self.master, text="Mobile No.", font='Helvetica 13 bold').place(x=100, y=300)
        self.entry8 = Entry(self.master, bd=2,textvar=self.Mob).place(x=300, y=300)
        self.usrn = Label(self.master, text="Gender", font='Helvetica 13 bold').place(x=100, y=340)
        self.radio=Radiobutton(self.master,text="male",value="male",variable=self.gender,font="Helvetica 8 bold").place(x=300,y=340)
        self.radio=Radiobutton(self.master,text="female",value="female",variable=self.gender,font="Helvetica 8 bold").place(x=380,y=340)
        self.button_reg=Button(self.master,text="Register",font="Helvetica 15 bold",padx=20,bg="green",command=self.database_registration).place(x=300,y=400)
        self.master.mainloop()
    def database_registration(self):
        #variable declaration
        self.Uid=self.uid.get()
        self.fname=self.Fname.get()
        self.email=self.Email.get()
        self.pasw=self.pswd.get()
        self.rpasw=self.rpswd.get()
        self.mob=self.Mob.get()
        self.gnd=self.gender.get()

        if(self.Uid==''or self.fname=='' or self.email==''or self.pasw=='' or self.rpasw=='' or self.mob==''):
            messagebox.showinfo("Empty", "Section cannot be empty!")
        elif(self.pasw!=self.rpasw):
            messagebox.showerror("error","make sure that password nd re-enter password must be same!")
        elif(len(self.pasw)<6):
            messagebox.showerror("paswword", "pasword should have atleaat 6 character!")
        elif(len(str((self.mob)))!=10):
            messagebox.showerror("Mobile number", "Mobile number should be atleast ten digit")
        else:
            if(re.match("\A(?P<name>[\w\-_]+)@(?P<domain>[\w\-_]+).(?P<toplevel>[\w]+)\Z",self.email,re.IGNORECASE)):
                con=sqlite3.connect("Cab booking.db")
                #con.execute("create table costumer_detail(uid int primary key, email varchar(30) unique ,full_name varchar(15) not null,"
                            #"password varchar(30),mobile int not null,gender varchar(10) not null)")
                con.execute("insert into costumer_detail(uid , email,full_name,password,mobile,gender)values(?,?,?,?,?,?)",( self.Uid,self.email,self.fname,self.pasw,self.mob,self.gnd))
                con.commit()
                con.close()
                answer=messagebox.askokcancel("Welcome","You have succesfully created your accunt")
                if(answer):
                    ob_1=Login(root)
            else:
                messagebox.showerror("Email", "Please enter valid Email Address")
class Book():
    def __init__(self,top4):
        #variable declaration
        self.time = StringVar()
        self.pickup = StringVar()
        self.drop1 = StringVar()
        self.dept = StringVar()
        self.unid=StringVar()
        self.top4 = top4
        self.top4.geometry("640x480")
        self.photo5 = PhotoImage(file="texi.png")
        self.Book_photo = Label(self.top4, image=self.photo5).pack()
        self.label_booking=Label(self.top4,text="Cab Booking Form", font="Helvetica 14 bold",padx=250,pady=20 ,bg="Thistle").place(x=0,y=0)
        self.canvas_book = Canvas(self.top4, bg="orange", height=300, width=350).place(x=180, y=120)
        self.header = Label(self.top4, text="Boook Your Cab Now", font="Helvetica 12 bold").place(x=250, y=130)
        self.lable_user=Label(self.top4,text="university id:",font="Helvetica 10 bold").place(x=190,y=170)
        self.entry_user=Entry(self.top4,textvar=self.unid).place(x=350,y=170)
        self.picup = Label(self.top4, text="Pick Up Location:", font="Helvetica 10 bold").place(x=190, y=200)
        #list for pick up and drop
        list1 = ['BH1','BH2','BH3','BH4','BH5','BH6','BH7','GH1','GH2','GH3','GH4','GH5','GH6','CAMPUS CAFE','UNI HOSPITAL','UNI MALL','DSA','LAW BLOCK','ADMISSION BLOCK','APARTMENTS','FIRE STATION']
        droplist = OptionMenu(self.top4, self.pickup, *list1)
        self.pickup.set('Current Location')  # bydefault text
        droplist.place(x=350, y=200)

        self.drop  =Label(self.top4, text="Drop Location:", font="Helvetica 10 bold").place(x=190, y=240)

        #droplist for drop
        droplist = OptionMenu(self.top4, self.drop1, *list1)
        self.drop1.set('Drop Location')  # bydefault text
        droplist.place(x=350, y=240)
        self.deprt = Label(self.top4, text="Depart:", font="Helvetica 10 bold").place(x=190, y=280)

        list2 = ['Today', 'Tomorrow', 'Day After Tomorrow']  # list data
        droplist = OptionMenu(self.top4, self.dept, *list2)
        self.dept.set('Today')  # bydefault text
        droplist.place(x=350, y=280)

        self.time1 = Label(self.top4, text="Time:", font="Helvetica 10 bold").place(x=190, y=320)
        self.time.set("12:00 PM")
        self.entry_time=Entry(self.top4,textvar=self.time).place(x=350,y=320)

        self.book1 = Button(self.top4, text="Book", font="Helvetica 10 bold",bg="Thistle",padx=155,pady=5,command=self.database_book).place(x=180, y=383)
        self.top4.mainloop()
    def database_book(self):
        self.unid1=self.unid.get()
        self.pick=self.pickup.get()
        self.drop2=self.drop1.get()
        self.time1=self.time.get()
        self.depart=self.dept.get()
        self.status="Pending"
        if (self.unid1==0 or self.time1=='' or self.pick == 'Current Location' or self.drop2 == 'Drop Location'):
            messagebox.showinfo("Empty", "Section cannot be empty!")
        else:
            con1=sqlite3.connect("Cab booking.db")
            #con1.execute("create table Booking1(unid varchar(20) not null,pickup varchar(20) not null ,drop_p varchar(25) not null,Time_p varchar(10) not null,depart varchar(25) not null,status varchar(10) not null)")
            con1.execute("insert into Booking1(unid,pickup,drop_p,Time_p,depart,status)values(?,?,?,?,?,?)",(self.unid1,self.pick,self.drop2,self.time1,self.depart,self.status))
            messagebox.showinfo("Succesfull", "Booking Processing!")
            c=con1.execute("select * from Booking1")
            for i in c:
                print(i)
            con1.commit()
            con1.close()
class admin_page:

    def __init__(self,top1):
        self.top1=top1
        self.top1.geometry("640x480")
        self.photo2 = PhotoImage(file="Taxi-Booking.png")
        self.admin_photo = Label(self.top1, image=self.photo2).place(x=0, y=0)
        self.admin1 = Label(self.top1, text="Welcome to LPU Cab Booking system", font="Helvetica 14 bold ", ).place( x=180, y=10)
        self.canvas_admin = Canvas(self.top1, bg="green", height=250, width=300).place(x=180, y=120)
        self.admin2 = Label(self.top1, text="Costumer Detail", font="Helvetica 10 bold").place(x=200, y=150)
        self.admin_button=Button(self.top1,text="Click Here",bg='blue',font="Helvetica 9 bold",command=self.costumer_detail).place(x=400,y=150)
        self.admin2 = Label(self.top1, text="Costumer Booking", font="Helvetica 10 bold").place(x=200, y=200)
        self.admin_button1 = Button(self.top1, text="Click Here", bg='blue', font="Helvetica 9 bold",command=self.costumer_booking).place(x=400, y=200)
        self.logout_button = Button(self.top1, text="Log Out", font="Helvetica 9 bold", bg="red",command=self.login).place(x=330, y=330)
        self.top1.mainloop()
    def login(self):
        Login(self.top1)
    def costumer_detail(self):
        self.top2 =Toplevel( self.top1)
        self.top2.geometry("640x480")
        self.photo_cd = PhotoImage(file="mario.png")
        self.cd_photo = Label(self.top2, image=self.photo_cd).place(x=0, y=0)
        #self.C_header=Label(self.top2,text="Costumer details",font="Helvetica 14 bold").place(x=250,y=10)
        self.C_id=Label(self.top2,text="Costumer Id",font="Helvetica 10 bold").grid(row=1,column=1)
        self.C_name=Label(self.top2,text="Costumer Name",font="Helvetica 10 bold").grid(row=1,column=2)
        self.C_Email = Label(self.top2, text="Email", font="Helvetica 10 bold").grid(row=1, column=3)
        self.C_Mobile = Label(self.top2, text="Mobile", font="Helvetica 10 bold").grid(row=1, column=4)
        con = sqlite3.connect("Cab booking.db")
        c=con.execute("select * from costumer_detail")
        self.j=0
        for i in c:
            self.entry_d=Label(self.top2,text=i[0]).grid(row=self.j+2,column=1)
            self.j=self.j+1
        c1 = con.execute("select * from costumer_detail")
        self.a = 0
        for j in c1:
            self.name = Label(self.top2, text=j[2]).grid(row=self.a + 2, column=2)
            self.a = self.a + 1
        c2 = con.execute("select * from costumer_detail")
        self.d = 0
        for k in c2:
            self.name = Label(self.top2, text=k[1]).grid(row=self.d + 2, column=3)
            self.d = self.d + 1
        c3 = con.execute("select * from costumer_detail")
        self.l = 0
        for p in c3:
            self.name = Label(self.top2, text=p[4]).grid(row=self.l + 2, column=4)
            self.l = self.l + 1

        con.commit()
        con.close()
    def costumer_booking(self):
        self.bookin_top = Toplevel(self.top1)
        self.bookin_top.geometry("640x480")
        con = sqlite3.connect("Cab booking.db")
        self.Booking_id = Label(self.bookin_top, text="Costumer Id", font="Helvetica 10 bold").grid(row=1, column=1)
        self.booking_pick = Label(self.bookin_top, text="pick up", font="Helvetica 10 bold").grid(row=1, column=2)
        self.booking_drop = Label(self.bookin_top, text="Drop", font="Helvetica 10 bold").grid(row=1, column=3)
        self.booking_depart = Label(self.bookin_top, text="depart", font="Helvetica 10 bold").grid(row=1, column=4)
        self.booking_time = Label(self.bookin_top, text="Time", font="Helvetica 10 bold").grid(row=1, column=5)
        self.booking_status = Label(self.bookin_top, text="status", font="Helvetica 10 bold").grid(row=1, column=6)
        self.booking_confirm = Label(self.bookin_top, text="Confirm", font="Helvetica 10 bold").grid(row=1, column=7)

        self.booking_info=con.execute("select unid from Booking1")
        self.g=0
        for i in self.booking_info:
            self.booking_id = Label(self.bookin_top, text=i,fg='red').grid(row=self.g + 2, column=1)
            self.book_button=Button(self.bookin_top,text="Confirm",bg='green').grid(row=self.g+2,column=7)
            self.g= self.g + 1

        self.booking_pickup = con.execute("select pickup from Booking1")
        self.w=0
        for j in self.booking_pickup:
            self.booking_pickup = Label(self.bookin_top, text=j, fg='red').grid(row=self.w + 2, column=2)
            self.w = self.w + 1

        self.booking_drop = con.execute("select drop_p from Booking1")
        self.e = 0
        for j in self.booking_drop:
            self.booking_drop = Label(self.bookin_top, text=j, fg='red').grid(row=self.e + 2, column=3)
            self.e = self.e + 1

        self.booking_depart = con.execute("select depart from Booking1")
        self.r = 0
        for j in self.booking_depart:
            self.booking_depart = Label(self.bookin_top, text=j, fg='red').grid(row=self.r + 2, column=4)
            self.r = self.r + 1

        self.booking_time = con.execute("select Time_p from Booking1")
        self.t = 0
        for j in self.booking_time:
            self.booking_time = Label(self.bookin_top, text=j, fg='red').grid(row=self.t + 2, column=5)
            self.t = self.t + 1

        self.booking_status = con.execute("select status from Booking1")
        self.y = 0
        for j in self.booking_status:
            self.booking_status = Label(self.bookin_top, text=j, fg='red').grid(row=self.y + 2, column=6)
            self.y = self.y + 1
        con.commit()
        con.close()


root=Tk()
Login(root)
root.mainloop()
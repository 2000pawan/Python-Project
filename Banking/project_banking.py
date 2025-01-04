from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from sqlite3 import *
from datetime import datetime
import csv
root=Tk()
root.title("Banking")
root.state('zoomed')
root.configure(bg='powder blue')
root.resizable(width=False,height=False)

lbl_title=Label(root,text="Noida Small Finance Bank",font=('',45,'bold','underline'),bg='powder blue')
lbl_title.pack()

photo=PhotoImage(file="bank.png")
lbl_img=Label(root,image=photo)
lbl_img.place(x=0,y=0)

def home_screen(pfrm=None):
    if(pfrm!=None):
        pfrm.destroy()
    frm=Frame(root)
    frm.configure(bg='pink')
    frm.place(x=0,y=140,relwidth=1,relheight=1)

    lbl_user=Label(frm,text="Username:",font=('',16,'bold'),bg='pink')
    entry_user=Entry(frm,font=('',16,'bold'),bd=8)

    lbl_user.place(relx=.8,rely=.20)
    entry_user.place(relx=.86,rely=.20)
    entry_user.focus()

    lbl_pass=Label(frm,text="Password:",font=('',16,'bold'),bg='pink')
    entry_pass=Entry(frm,font=('',16,'bold'),bd=8,show="*")

    lbl_pass.place(relx=.8,rely=.28)
    entry_pass.place(relx=.86,rely=.28)

    lbl_type=Label(frm,text="User Type:",font=('',16,'bold'),bg='pink')
    
    lbl_type.place(relx=.8,rely=.35)
    combo_type = ttk.Combobox(frm, 
                            values=[
                                    "---Select user---", 
                                    "Customer",
                                    "Admin",
                                    ],font=('',16,''))
    combo_type["state"] = 'readonly'
    combo_type.current()
    combo_type.place(relx=.86,rely=.35)
    
    headingFrame1 = Frame(root,bg="#800080",bd= 5)
    headingFrame1.place(relx=.04,rely=.2,relwidth=0.2,relheight=0.04)

    headingLabel = Label(headingFrame1, text="Loan", bg='white', fg='black', font=('',22))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    label_loan= Label(root, text= "Welcome to TutorialsPoint", cursor= "hand2", foreground= "green", font= ('Aerial 18'))
    label_loan.place(relx=.05,rely=.25)
    

    
    headingFrame1 = Frame(root,bg="#800080",bd= 5)
    headingFrame1.place(relx=.30,rely=.2,relwidth=0.2,relheight=0.04)

    headingLabel = Label(headingFrame1, text="Insurance", bg='white', fg='black', font=('',22))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    headingFrame1 = Frame(root,bg="#800080",bd= 5)
    headingFrame1.place(relx=.04,rely=.6,relwidth=0.2,relheight=0.04)

    headingLabel = Label(headingFrame1, text="Services", bg='white', fg='black', font=('',22))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    headingFrame1 = Frame(root,bg="#800080",bd= 5)
    headingFrame1.place(relx=.30,rely=.6,relwidth=0.2,relheight=0.04)

    headingLabel = Label(headingFrame1, text="Enquiry", bg='white', fg='black', font=('',22))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    headingFrame1 = Frame(root,bg="#800080",bd= 5)
    headingFrame1.place(relx=.80,rely=.2,relwidth=0.2,relheight=0.04)

    headingLabel = Label(headingFrame1, text="Net Banking Login", bg='white', fg='black', font=('',22))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    login_btn=Button(frm,command=lambda:welcome_screen(frm,entry_user,entry_pass,combo_type),width=8,text="Login",font=('',16,'bold'),bg='powder blue',bd=6)
    login_btn.place(relx=.88,rely=.40)

    #reset_btn=Button(frm,command=lambda:reset_home(entry_user,entry_pass,combo_type),width=10,text="reset",font=('',20,'bold'),bg='powder blue',bd=10)
    #reset_btn.place(relx=.5,rely=.45)

    open_btn=Button(frm,width=14,command=lambda:open_screen(frm),text="Open Account",font=('',20,'bold'),bg='powder blue',bd=10)
    open_btn.place(relx=.3,rely=.58)

    fp_btn=Button(frm,width=14,command=lambda:fp_screen(frm),text="Forgot Password",font=('',16,'bold'),bg='powder blue',bd=6)
    fp_btn.place(relx=.86,rely=.48)


def logout(pfrm):
    option=messagebox.askyesno(title='logout', message="Do you really want to logout?")
    if(option==True):
        home_screen(pfrm)
    else:
        pass
def welcome_screen(pfrm,entry_user,entry_pass,combo_type):
    user=entry_user.get()
    pwd=entry_pass.get()
    tp=combo_type.get()
    if(tp=="---Select user---"):
        messagebox.showwarning("warning","please select type")
        return
    elif(tp=="Customer"):
        con=connect("bank.db")
        cur=con.cursor()
        cur.execute("select name,bal,type from useraccount where acn=? and pass=?",(user,pwd))
        tup=cur.fetchone()
        if(tup==None):
            messagebox.showerror("fail","Invalid username/password")
            return
        else:
            pfrm.destroy()
            frm=Frame(root)
            frm.configure(bg='pink')
            frm.place(x=0,y=140,relwidth=1,relheight=1)

            
            
            logout_btn=Button(frm,command=lambda:logout(frm),text="logout",font=('',20,'bold'),bg='powder blue',bd=10)
            logout_btn.place(relx=.9,rely=.001)

            left_frm=Frame(frm)
            left_frm.configure(bg='pink')
            left_frm.place(x=5,y=0,relwidth=.2,relheight=1)

            Label(left_frm,text=f"Welcome,{tup[0]}",font=('',15),bg='pink').place(x=2,y=2)
            check_btn=Button(left_frm,width=12,command=lambda:checkbal_frame(),text="check bal",font=('',20,'bold'),bg='powder blue',bd=10)
            check_btn.place(relx=.001,rely=.1)

            deposit_btn=Button(left_frm,width=12,command=lambda:deposit_frame(),text="deposit",font=('',20,'bold'),bg='powder blue',bd=10)
            deposit_btn.place(relx=.001,rely=.25)

            withdraw_btn=Button(left_frm,width=12,command=lambda:withdraw_frame(),text="withdraw",font=('',20,'bold'),bg='powder blue',bd=10)
            withdraw_btn.place(relx=.001,rely=.4)

            transfer_btn=Button(left_frm,width=12,command=lambda:transfer_frame(),text="transfer",font=('',20,'bold'),bg='powder blue',bd=10)
            transfer_btn.place(relx=.001,rely=.55)

            txnhist_btn=Button(left_frm,width=12,command=lambda:txnhistory_frame(),text="txn history",font=('',20,'bold'),bg='powder blue',bd=10)
            txnhist_btn.place(relx=.001,rely=.7)
    else:
        if(user=="admin" and pwd=="admin"):
            pfrm.destroy()
            frm=Frame(root)
            frm.configure(bg='pink')
            frm.place(x=0,y=140,relwidth=1,relheight=1)

            logout_btn=Button(frm,command=lambda:logout(frm),text="logout",font=('',20,'bold'),bg='powder blue',bd=10)
            logout_btn.place(relx=.9,rely=.001)

            Label(frm,text="Welcome,Admin",font=('',15),bg='pink').place(x=2,y=2)

            view_btn=Button(frm,width=15,command=lambda:viewcustomer_frame(),text="View Customers",font=('',20,'bold'),bg='powder blue',bd=10)
            view_btn.place(relx=.4,rely=.1)

        else:
            messagebox.showerror("Invalid","Invalid username/password for admin")
            return

    def viewcustomer_frame():
        f=Frame(frm)
        f.configure(bg='pink')
        f.place(x=250,y=20,relwidth=.7,relheight=.6)
        con=connect("bank.db")
        cur=con.cursor()
        cur.execute("select name,acn,type,bal,mob,email from useraccount")
        Label(f,text="Name",font=('',15,'bold'),bg='pink',fg='black').place(x=50,y=10)
        Label(f,text="ACN",font=('',15,'bold'),bg='pink',fg='black').place(x=150,y=10)
        Label(f,text="Type",font=('',15,'bold'),bg='pink',fg='black').place(x=250,y=10)
        Label(f,text="Avl. Bal",font=('',15,'bold'),bg='pink',fg='black').place(x=350,y=10)
        Label(f,text="Mob",font=('',15,'bold'),bg='pink',fg='black').place(x=450,y=10)
        Label(f,text="Email",font=('',15,'bold'),bg='pink',fg='black').place(x=550,y=10)
        
        i=50
        for row in cur:
            Label(f,text=f"{row[0]}",font=('',12),bg='pink',fg='black').place(x=50,y=i)
            Label(f,text=f"{row[1]}",font=('',12),bg='pink',fg='black').place(x=150,y=i)
            Label(f,text=f"{row[2]}",font=('',12),bg='pink',fg='black').place(x=250,y=i)
            Label(f,text=f"{row[3]}",font=('',12),bg='pink',fg='black').place(x=350,y=i)
            Label(f,text=f"{row[4]}",font=('',12),bg='pink',fg='black').place(x=450,y=i)
            Label(f,text=f"{row[5]}",font=('',12),bg='pink',fg='black').place(x=550,y=i)
            
            i=i+40

    def checkbal_frame():
        f=Frame(frm)
        f.configure(bg='pink')
        f.place(x=250,y=20,relwidth=.7,relheight=.6)
        con=connect("bank.db")
        cur=con.cursor()
        cur.execute("select bal from useraccount where acn=?",(user,))
        tupp=cur.fetchone()
        bal=int(tupp[0])
        con.close()
        lbl_name=Label(f,text=f"Name:\t{tup[0]}",fg="green",font=('',20,'bold'),bg='pink')
        lbl_bal=Label(f,text=f"Balance:\t{bal}",fg="green",font=('',20,'bold'),bg='pink')
        lbl_type=Label(f,text=f"Type:\t{tup[2]}",fg="green",font=('',20,'bold'),bg='pink')
        lbl_name.place(x=200,y=100)
        lbl_bal.place(x=200,y=200)
        lbl_type.place(x=200,y=300)
        

    def deposit_frame():
        f=Frame(frm)
        f.configure(bg='pink')
        f.place(x=250,y=20,relwidth=.7,relheight=.6)
        lbl_amt=Label(f,text="Amount:",fg="green",font=('',20,'bold'),bg='pink')
        entry_amt=Entry(f,font=('',20,'bold'),bd=10)
        sub_btn=Button(f,command=lambda:deposit_db(entry_amt),width=10,text="deposit",font=('',20,'bold'),bd=10,bg="powder blue")
        reset_btn=Button(f,width=10,text="reset",font=('',20,'bold'),bd=10,bg="powder blue")

        lbl_amt.place(x=100,y=100)
        entry_amt.place(x=300,y=100)
        sub_btn.place(x=150,y=200)
        reset_btn.place(x=350,y=200)

    def deposit_db(entry_amt):
        amt=int(entry_amt.get())
        dt=str(datetime.now())
        con=connect("bank.db")
        cur=con.cursor()
        cur.execute("select bal from useraccount where acn=?",(user,))
        tup=cur.fetchone()
        bal=int(tup[0])
        cur.execute("update useraccount set bal=bal+? where acn=?",(amt,user))
        cur.execute("insert into txnhistory values(?,?,?,?,?)",(user,dt,amt,'Cr.',bal+amt))
        con.commit()
        messagebox.shorootfo("Updated",f"{amt} is deposited")
        con.close()


    def withdraw_db(entry_amt):
        amt=int(entry_amt.get())
        dt=str(datetime.now())
        con=connect("bank.db")
        cur=con.cursor()
        cur.execute("select bal from useraccount where acn=?",(user,))
        tup=cur.fetchone()
        bal=int(tup[0])
        cur.execute("update useraccount set bal=bal-? where acn=?",(amt,user))
        cur.execute("insert into txnhistory values(?,?,?,?,?)",(user,dt,amt,'Db.',bal-amt))
        con.commit()
        messagebox.shorootfo("Updated",f"{amt} is withdrawn")
        con.close()
        
        
    def withdraw_frame():
        f=Frame(frm)
        f.configure(bg='pink')
        f.place(x=250,y=20,relwidth=.7,relheight=.6)
        lbl_amt=Label(f,text="Amount:",fg="green",font=('',20,'bold'),bg='pink')
        entry_amt=Entry(f,font=('',20,'bold'),bd=10)
        sub_btn=Button(f,command=lambda:withdraw_db(entry_amt),width=10,text="withdraw",font=('',20,'bold'),bd=10,bg="powder blue")
        reset_btn=Button(f,width=10,text="reset",font=('',20,'bold'),bd=10,bg="powder blue")

        lbl_amt.place(x=100,y=100)
        entry_amt.place(x=300,y=100)
        sub_btn.place(x=150,y=200)
        reset_btn.place(x=350,y=200)
    def transfer_frame():
        f=Frame(frm)
        f.configure(bg='pink')
        f.place(x=250,y=20,relwidth=.7,relheight=.6)
        lbl_amt=Label(f,text="Amount:",fg="green",font=('',20,'bold'),bg='pink')
        entry_amt=Entry(f,font=('',20,'bold'),bd=10)

        lbl_to=Label(f,text="To Acn:",fg="green",font=('',20,'bold'),bg='pink')
        entry_to=Entry(f,font=('',20,'bold'),bd=10)

        sub_btn=Button(f,command=lambda:transfer_db(entry_amt,entry_to),width=10,text="transfer",font=('',20,'bold'),bd=10,bg="powder blue")
        reset_btn=Button(f,width=10,text="reset",font=('',20,'bold'),bd=10,bg="powder blue")

        lbl_amt.place(x=100,y=100)
        entry_amt.place(x=300,y=100)

        lbl_to.place(x=100,y=200)
        entry_to.place(x=300,y=200)
        sub_btn.place(x=150,y=300)
        reset_btn.place(x=350,y=300)

    def txnhistory_frame():
        f=Frame(frm)
        f.configure(bg='pink')
        f.place(x=250,y=20,relwidth=.7,relheight=.6)
        con=connect("bank.db")
        cur=con.cursor()
        cur.execute("select * from txnhistory where acn=?",(user,))
        Label(f,text="Date",font=('',15,'bold'),bg='pink',fg='black').place(x=100,y=10)
        Label(f,text="Amount",font=('',15,'bold'),bg='pink',fg='black').place(x=300,y=10)
        Label(f,text="Type",font=('',15,'bold'),bg='pink',fg='black').place(x=500,y=10)
        Label(f,text="Updated Bal",font=('',15,'bold'),bg='pink',fg='black').place(x=700,y=10)
        i=50
        for row in cur:
            Label(f,text=f"{row[1][:10]}",font=('',12),bg='pink',fg='black').place(x=100,y=i)
            Label(f,text=f"{row[2]}",font=('',12),bg='pink',fg='black').place(x=300,y=i)
            Label(f,text=f"{row[3]}",font=('',12),bg='pink',fg='black').place(x=500,y=i)
            Label(f,text=f"{row[4]}",font=('',12),bg='pink',fg='black').place(x=700,y=i)
            i=i+40
        
    def transfer_db(entry_amt,entry_to):
        amt=int(entry_amt.get())
        to=entry_to.get()
        dt=str(datetime.now())
        con=connect("bank.db")
        cur=con.cursor()
        cur.execute("select * from useraccount where acn=?",(to,))
        tup=cur.fetchone()
        if(tup==None):
            messagebox.showerror("fail","Invalid to account")
            return
        else:
            cur.execute("select bal from useraccount where acn=?",(user,))
            tup1=cur.fetchone()
            bal1=int(tup1[0])

            cur.execute("select bal from useraccount where acn=?",(to,))
            tup2=cur.fetchone()
            bal2=int(tup2[0])
            
            cur.execute("update useraccount set bal=bal-? where acn=?",(amt,user))
            cur.execute("update useraccount set bal=bal+? where acn=?",(amt,to))

            cur.execute("insert into txnhistory values(?,?,?,?,?)",(user,dt,amt,'Db.',bal1-amt))
            cur.execute("insert into txnhistory values(?,?,?,?,?)",(to,dt,amt,'Cr.',bal2+amt))
            
            con.commit()
            messagebox.shorootfo("Success","Amount transfer done..")
            con.close()

    if(user!="admin" and pwd!="admin"):        
        checkbal_frame()

def fp_screen(pfrm):
    pfrm.destroy()
    frm=Frame(root)
    frm.configure(bg='pink')
    frm.place(x=0,y=140,relwidth=1,relheight=1)

    back_btn=Button(frm,command=lambda:home_screen(frm),text="Back",font=('',20,'bold'),bg='powder blue',bd=10)
    back_btn.place(relx=.001,rely=.001)

    lbl_acn=Label(frm,text="Acno:",fg="green",font=('',20,'bold'),bg='pink')
    entry_acn=Entry(frm,font=('',20,'bold'),bd=10)

    lbl_mob=Label(frm,text="Mob:",fg="green",font=('',20,'bold'),bg='pink')
    entry_mob=Entry(frm,font=('',20,'bold'),bd=10)

    sub_btn=Button(frm,command=lambda:recover_pass(frm,entry_acn,entry_mob),width=10,text="recover",font=('',20,'bold'),bd=10,bg="powder blue")
    reset_btn=Button(frm,width=10,text="reset",font=('',20,'bold'),bd=10,bg="powder blue")

    lbl_acn.place(x=300,y=100)
    entry_acn.place(x=500,y=100)

    lbl_mob.place(x=300,y=200)
    entry_mob.place(x=500,y=200)
    sub_btn.place(x=350,y=300)
    reset_btn.place(x=550,y=300)



def open_screen(pfrm):
    pfrm.destroy()
    frm=Frame(root)
    frm.configure(bg='pink')
    frm.place(x=0,y=140,relwidth=1,relheight=1)

    back_btn=Button(frm,command=lambda:home_screen(frm),text="Back",font=('',20,'bold'),bg='powder blue',bd=10)
    back_btn.place(relx=.001,rely=.001)

    lbl_acn=Label(frm,text="Acno:",fg="green",font=('',20,'bold'),bg='pink')
    entry_acn=Entry(frm,font=('',20,'bold'),bd=10,state='disable')

    lbl_mob=Label(frm,text="Mob:",fg="green",font=('',20,'bold'),bg='pink')
    entry_mob=Entry(frm,font=('',20,'bold'),bd=10)

    lbl_email=Label(frm,text="Email:",fg="green",font=('',20,'bold'),bg='pink')
    entry_email=Entry(frm,font=('',20,'bold'),bd=10)

    lbl_name=Label(frm,text="Name:",fg="green",font=('',20,'bold'),bg='pink')
    entry_name=Entry(frm,font=('',20,'bold'),bd=10)

    lbl_pass=Label(frm,text="Password:",fg="green",font=('',20,'bold'),bg='pink')
    entry_pass=Entry(frm,font=('',20,'bold'),bd=10,show="*")

    lbl_type=Label(frm,text="Type:",fg="green",font=('',20,'bold'),bg='pink')
    combo_type = ttk.Combobox(frm, 
                            values=[
                                    "Saving", 
                                    "Current",
                                    ],font=('',20,''))
    combo_type.current(0)
    


    sub_btn=Button(frm,command=lambda:openacn_db(frm,entry_mob,entry_email,entry_name,entry_pass,combo_type),width=10,text="open",font=('',20,'bold'),bd=10,bg="powder blue")
    reset_btn=Button(frm,width=10,text="reset",font=('',20,'bold'),bd=10,bg="powder blue")


    lbl_mob.place(x=300,y=90)
    entry_mob.place(x=500,y=90)

    lbl_email.place(x=300,y=170)
    entry_email.place(x=500,y=170)

    lbl_name.place(x=300,y=250)
    entry_name.place(x=500,y=250)

    lbl_pass.place(x=300,y=330)
    entry_pass.place(x=500,y=330)

    lbl_type.place(x=300,y=410)
    combo_type.place(x=500,y=410)

    sub_btn.place(x=350,y=490)
    reset_btn.place(x=550,y=490)
    


def reset_home(entry_user,entry_pass,combo_type):
    entry_user.delete(0,END)
    entry_pass.delete(0,END)
    combo_type.current(0)
    entry_user.focus()
    


def openacn_db(pfrm,entry_mob,entry_email,entry_name,entry_pass,combo_type):
    con=connect("bank.db")
    cur=con.cursor()
    cur.execute("select max(acn) from useraccount")
    tup=cur.fetchone()
    acn=tup[0]
    acn=acn+1
    con.close()
    mob=entry_mob.get()
    email=entry_email.get()
    name=entry_name.get()
    pwd=entry_pass.get()
    tp=combo_type.get()
    status='active'
    bal=1000
    con=connect("bank.db")
    cur=con.cursor()
    cur.execute("insert into useraccount values(?,?,?,?,?,?,?,?)",(name,pwd,email,mob,bal,tp,status,acn))
    con.commit()
    con.close()
    messagebox.shorootfo("Account Opening",f"Your Account is opened with Acn:{acn}")
    home_screen(pfrm)


def recover_pass(pfrm,entry_acn,entry_mob):
    acn=int(entry_acn.get())
    mob=entry_mob.get()
    con=connect("bank.db")
    cur=con.cursor()
    cur.execute("select pass from useraccount where acn=? and mob=?",(acn,mob))
    tup=cur.fetchone()
    if(tup==None):
        messagebox.showwarning("password","Invalid Acn/Mob")
        return
    else:    
        pwd=tup[0]
        messagebox.shorootfo("password",f"Your Password:{pwd}")
    con.close()
    home_screen(pfrm)
home_screen()
root.mainloop()

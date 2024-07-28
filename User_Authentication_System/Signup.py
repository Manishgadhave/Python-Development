from tkinter import *
from tkinter import messagebox
from PIL import ImageTk #imageTk required if using jpg files
import pymysql

def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmEntry.delete(0,END)
    check.set(0)

def login_page():
    root.destroy()
    import login

def connect_database():
    if emailEntry.get()== "" or usernameEntry.get()=="" or passwordEntry.get()=="" or confirmEntry.get()=="":
        messagebox.showerror("Error", "All fields are required")
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror("Error", "Password Mismatch")
    elif check.get()==0:
        messagebox.showerror("Error", "Please Accept Terms & Conditions")
    else:
        try:
            con=pymysql.connect(host="localhost", user="root", password="9119")
            mycursor=con.cursor()
        except:
            messagebox.showerror("Error", "Database Connectivity Issue, Please Try Again")
            return
        try:
            query="create database userdata"
            mycursor.execute(query)
            query="use userdata"
            mycursor.execute(query)
            query="create table data(id int auto_increment primary key not null, email varchar(50), username varchar(100), password varchar(20))"
            mycursor.execute(query)
        except:
            mycursor.execute("use userdata")
        query="select * from data where username=%s"
        mycursor.execute(query, (usernameEntry.get()))

        row=mycursor.fetchone()
        if row != None:
            messagebox.showerror("Error", "Username Already Exists")

        else:
            query="insert into data(email, username, password) values(%s,%s,%s)"
            mycursor.execute(query,(emailEntry.get(), usernameEntry.get(), passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo("Success", "Registration is Successful")
            clear()
            root.destroy()
            import login

root = Tk()
root.title("Sign Up")
root.resizable(0,0)

background=ImageTk.PhotoImage(file='bg.jpg')

bgLabel=Label(root, image=background)
bgLabel.grid()

frame=Frame(root, bg="white")
frame.place(x=554, y=100)

Heading=Label(frame, text="CREATE AN ACCOUNT", font=("Microsoft Yahei UI Light", 18, "bold")
              , bg="white", fg="firebrick")
Heading.grid(row=0, column=0, padx=10, pady=10)

emailLabel=Label(frame, text="Email", font=("Microsoft Yahei UI Light", 10, "bold")
                , bg="white", fg="firebrick")
emailLabel.grid(row=1, column=0, sticky="w", padx=25, pady=(10,0))

emailEntry=Entry(frame, width=30, font=("Microsoft Yahei UI Light", 10, "bold")
                 , bg="firebrick1", fg="white")
emailEntry.grid(row=2, column=0, sticky="w", padx=25)

usernameLabel=Label(frame, text="Username", font=("Microsoft Yahei UI Light", 10, "bold")
                , bg="white", fg="firebrick")
usernameLabel.grid(row=3, column=0, sticky="w", padx=25, pady=(10,0))

usernameEntry=Entry(frame, width=30, font=("Microsoft Yahei UI Light", 10, "bold")
                 , bg="firebrick1", fg="white")
usernameEntry.grid(row=4, column=0, sticky="w", padx=25)

passwordLabel=Label(frame, text="Password", font=("Microsoft Yahei UI Light", 10, "bold")
                , bg="white", fg="firebrick")
passwordLabel.grid(row=5, column=0, sticky="w", padx=25, pady=(10,0))

passwordEntry=Entry(frame, width=30, font=("Microsoft Yahei UI Light", 10, "bold")
                 , bg="firebrick1", fg="white")
passwordEntry.grid(row=6, column=0, sticky="w", padx=25)

confirmLabel=Label(frame, text="Confirm Password", font=("Microsoft Yahei UI Light", 10, "bold")
                , bg="white", fg="firebrick")
confirmLabel.grid(row=7, column=0, sticky="w", padx=25, pady=(10,0))

confirmEntry=Entry(frame, width=30, font=("Microsoft Yahei UI Light", 10, "bold")
                 , bg="firebrick1", fg="white")
confirmEntry.grid(row=8, column=0, sticky="w", padx=25)

check=IntVar()
termsandconditions=Checkbutton(frame, text="I agree to the terms & conditions", font=("Microsoft Yahei UI Light", 9, "bold")
                               , fg="firebrick1", bg="white", activebackground="white", activeforeground="firebrick1"
                               , cursor="hand2", variable=check)
termsandconditions.grid(row=9, column=0, padx=15, pady=10)

signupButton=Button(frame, text="Sign Up", font=("Open Sans", 16, "bold")
                    , bd=0, bg="firebrick1", fg="white", activebackground="firebrick1", activeforeground="white", width=17, cursor="hand2", command=connect_database)
signupButton.grid(row=10, column=0, pady=10)

alreadyaccount=Label(frame, text="Have an account?", font=("Open Sans", "9", "bold"),
                     bg="white", fg="firebrick1")
alreadyaccount.grid(row=11, column=0, sticky="w", padx=25, pady=2)

loginButton=Button(frame, text="Login", font=("Open Sans", 9, "bold underline")
                   , fg="blue", bg="white", activeforeground="blue", activebackground="white", cursor="hand2", bd=0, command=login_page)
loginButton.place(x=170, y=404)

root.mainloop()
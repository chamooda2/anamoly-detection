from tkinter import *
from tkinter import messagebox
import tkinter as Tk
import mysql.connector
import gadhahumai as gd

def option():
    def fire():
        detector = gd.MugDetection(capture_index=0, model_name='firebest.pt')
        detector.run() 

    def accident():
        detector = gd.MugDetectioOn(capture_index=0, model_name='accident.pt')
        detector.run()

    def weapon():
        detector = gd.MugDetection(capture_index=0, model_name='weaponbest.pt')
        detector.run()

    window=Toplevel(root)
    window.title('XYCams Security Detection Software')
    window.geometry('925x500+300+200')
    window.configure(bg='white')
    window.resizable(False,False)

    fireimg=PhotoImage(file='v2.0/fire__img_2.png')
    Label(window,image=fireimg,bg='white').place(x=65,y=160)

    weaponimg=PhotoImage(file='v2.0/weapons_img.png')
    Label(window,image=weaponimg,bg='white').place(x=370,y=160)

    carimg=PhotoImage(file='v2.0/accident_img.png')
    Label(window,image=carimg,bg='white').place(x=620,y=160)

    heading=Label(window,text="Detection System Selection",fg="#EE4B2B",bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
    heading.place(x=250,y=25)

    Button(window,width=30,pady=7,text='Fire Detection',bg='#EE4B2B',fg='white',border=0,command=fire).place(x=35,y=350)
    Button(window,width=30,pady=7,text='Weapon Detection',bg='#EE4B2B',fg='white',border=0,command=weapon).place(x=345,y=350)
    Button(window,width=30,pady=7,text='Road Accident Detection',bg='#EE4B2B',fg='white',border=0,command=accident).place(x=620,y=350)

    window.mainloop()

flag=False

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="tiger",
    database="xycams"
)
mycursor=mydb.cursor()

table_name="security"
mycursor.execute("SELECT * FROM "+str(table_name))

myresult = mycursor.fetchall()

root=Tk.Tk()
root.title('XYCams Login System')
root.geometry('925x500+300+200')
root.configure(bg="white")
root.resizable(False,False)

def signin():
    loginflag=False
    username=user.get()
    password=key.get()

    for x in myresult:

        if username==x[1] and password==x[2]:
            loginflag=True

    if loginflag:
        option()
    else:
        messagebox.showerror("Invalid","Incorrect username and/or password")
    root.destroy()                

img=PhotoImage(file='v2.0\security_img.png')
Label(root,image=img,bg="white").place(x=50,y=50)

frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text="Sign In",fg="green",bg="white",font=('Microsoft YaHei UI Light',25,'bold'))
heading.place(x=100,y=5)

##----------
 
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')
        
user=Entry(frame,width=30,fg='green',border=0,bg="white",font=('Microsoft YaHei UI Light',10))
user.place(x=30,y=80)
user.insert(0,'Username@security/@resident')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)


Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

##-----------

def on_enter(e):
    key.delete(0,'end')

def on_leave(e):
    name=key.get()
    if name=='':
        key.insert(0,'Password')

key=Entry(frame,width=25,fg='green',border=0,bg="white",font=('Microsoft YaHei UI Light',10))
key.place(x=30,y=150)
key.insert(0,'Security Key')
key.bind('<FocusIn>',on_enter)
key.bind('<FocusOut>',on_leave) 

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

##-----------

Button(frame,width=40,pady=7,text='Sign in',bg='green',fg='white',border=0,command=signin).place(x=35,y=204)
label=Label(frame,text="New resident ?",fg='black',bg='white',font=('Microsoft YaHei UI Light',8))
label.place(x=75,y=270)
    
sign_up=Button(frame,width=20,text='Register as a Resident',border=0,bg='white',cursor='hand2',fg='green')
sign_up.place(x=160,y=270)

root.mainloop()
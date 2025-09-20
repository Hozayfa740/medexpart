import random
from tkinter import *
import PIL.Image
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from singup import SignupWin

import pyttsx3
import time
from homepage import homewin

class loginwin:
    def __init__(self,root):

        self.user_name = StringVar()
        self.password = StringVar()
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1550x800+0+0")


        img2 = Image.open(r"C:\Users\asus\Downloads\Gemini_Generated_Image_4f1zfg4f1zfg4f1z.jpg")
        img2 = img2.resize((1550, 800), PIL.Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        Lbimage = Label(self.root, image=self.photoimg2, relief=RIDGE)
        Lbimage.place(x=0, y=0, width=1550, height=800)

        login_frame=Frame(self.root, bg="white")
        login_frame.place(x=500,y=160,height=400,width=500)
        #"C:\Users\asus\OneDrive\Pictures\Feedback\photo_2024-11-15_01-40-01.jpg"

        img3= Image.open(r"C:\Users\asus\OneDrive\Pictures\Feedback\photo_2024-11-15_01-40-01.jpg")
        img3 = img3.resize((700, 700), PIL.Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        Lbimage = Label(login_frame, image=self.photoimg3, relief=RIDGE)
        Lbimage.place(x=-110, y=-110)


        title=Label(login_frame,text="Login Here",font=("Impact",20,"bold"),fg="#7AC5CD",padx=10,pady=2,bg="#000435")
        title.place(x=190,y=10)
        title2 = Label(login_frame, text="Accountant Login Area", font=("Goudy old style", 11, "bold"), fg="#53868B", padx=10, pady=2,bg="#000435")
        title2.place(x=180, y=55)

        user = Label(login_frame, text="Username", font=("times new roman", 15, "bold"),
                       fg="white" ,bg="#000435" )
        user.place(x=15,y=100)
        entry_user = ttk.Entry(login_frame, width=30,textvariable=self.user_name,
                             font=("times new roman", 15))
        entry_user.place(x=15, y=140)

        password = Label(login_frame, text="Password", font=("times new roman", 15, "bold"),
                         fg="white", bg="#000435"
                         )
        password.place(x=15, y=180)
        entry_password = ttk.Entry(login_frame, width=30,textvariable=self.password,
                               font=("times new roman", 15),show="*")
        entry_password.place(x=15, y=220)

        forget=Button(login_frame, text="Forget Password?", cursor="hand2",font=("times new roman", 10),
                       fg="white",bd=0,bg="#000435")
        forget.place(x=15, y=260)
        #==========



        img5= Image.open(r"C:\Users\asus\OneDrive\Pictures\Feedback\login.png")

        self.photoimg5= ImageTk.PhotoImage(img5)

        login = Button(self.root, image=self.photoimg5, command=self.loginf,cursor="hand2",bd=-10,bg="#000435")
        login.place(x=695, y=435)

        title3 = Label(login_frame, text="or",font=("times new roman", 15,"bold") ,fg="white",bg="#000435")
        title3.place(x=228, y=317)
        img6 = Image.open(r"C:\Users\asus\OneDrive\Pictures\Feedback\s22.png")

        self.photoimg6 = ImageTk.PhotoImage(img6)

        singup = Button(login_frame,image=self.photoimg6, command=self.singupf, cursor="hand2",bd=-10,bg="#000435")

        singup.place(x=187, y=345)


    def loginf(self):
        if self.user_name.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.user_name.get()!="hozayfa740" or self.password.get()!="123":
            messagebox.showerror("Error","Invalid Username Or Password",parent=self.root)
            self.user_name.set("")
            self.password.set("")
        elif self.user_name.get()=="hozayfa740" or self.password.get()=="123":
            ######
            ######
            ####

            self.user_name.set("")
            self.password.set("")
            self.new_window = Toplevel(self.root)
            self.app = homewin(self.new_window)
    def singupf(self):
        self.new_window = Toplevel(self.root)
        self.app = SignupWin(self.new_window)






if __name__ == '__main__':
    root=Tk()
    obj=loginwin(root)
    talk = pyttsx3.init()
    talk.say("   wellcome    in      medexpart")
    talk.runAndWait()
    root.mainloop()

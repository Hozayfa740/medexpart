import random
from tkinter import *
import PIL.Image
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import os
from PIL import Image, ImageDraw, ImageTk
from tkinter import messagebox
from profile import profilewin
from doctots import doctor_win
from ambulance import ambulance_win
from blood import blood_win
from medicin import medicin_win

import customtkinter as ctk
class homewin:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1550x800+0+0")
        head_frame = Label(self.root, text="MedXpert", font=("times new roman", 40, "bold"), bg="#303030", fg="white")
        head_frame.place(x=0, y=0, height=130, width=1550)
        image_path = r"C:\Users\asus\OneDrive\Pictures\Feedback\photo_2024-11-15_22-14-09.jpg"

        try:
            if os.path.exists(image_path):
                # Load and resize image
                image = Image.open(image_path).resize((80, 80))

                # Create a circular mask
                mask = Image.new("L", (80, 80), 0)
                draw = ImageDraw.Draw(mask)
                draw.ellipse((0, 0, 80, 80), fill=255)

                # Apply mask to create a circular image
                circular_image = Image.new("RGBA", (80, 80))
                circular_image.paste(image, (0, 0), mask=mask)

                # Convert to a format compatible with Tkinter
                ctk_image = ImageTk.PhotoImage(circular_image)

                # Place the image in the head_frame
                img_label = Label(head_frame, image=ctk_image, bg="#303030")
                img_label.image = ctk_image  # Keep reference
                img_label.place(x=10, y=20)  # Adjust coordinates as needed
            else:
                print(f"Image not found at path: {image_path}")
        except Exception as e:
            print(f"Error loading or displaying image: {e}")

        head_frameall = Frame(self.root, bg="#8D99AE")
        head_frameall.place(x=0, y=130, height=750, width=1550)
        head_framea3 = Frame(head_frameall, bg="#A7C7E7")
        head_framea3.place(x=6, y=20, height=600, width=1515)


        #===========#========#======#====1

        img7 = Image.open(r"C:\Users\asus\OneDrive\Pictures\Feedback\21564f9a-8b35-47f6-94a0-0844be7f9c75.png")
        img7 = img7.resize((270, 50), PIL.Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        Lbimage = Label(head_framea3, image=self.photoimg7, bg="#A7C7E7", bd=-10)
        Lbimage.place(x=0, y=40, width=270, height=50)
        #============1
        img8 = Image.open(r"C:\Users\asus\OneDrive\Pictures\Feedback\conceltant.jpg")
        img8 = img8.resize((80, 50), PIL.Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        conceltant = Button(head_framea3, image=self.photoimg8,command=self.doc, cursor="hand2", bd=-20)
        conceltant.place(x=270, y=40, height=50)
        # ===========#========#======#====2

        img9= Image.open(r"C:\Users\asus\OneDrive\Pictures\Feedback\961329c6-f0d8-4c99-a22f-7e469cf3d1ff.png")
        img9 = img9.resize((270, 50), PIL.Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        Lbimage = Label(head_framea3, image=self.photoimg9, bg="#A7C7E7", bd=-10)
        Lbimage.place(x=0, y=130, width=270, height=50)
        # ============2
        img10 = Image.open(r"C:\Users\asus\OneDrive\Pictures\Feedback\medicin.jpg")
        img10 = img10.resize((80, 50), PIL.Image.Resampling.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        medicin = Button(head_framea3, image=self.photoimg10,command=self.med, cursor="hand2", bd=-20)
        medicin.place(x=270, y=130, height=50)

        # ===========#=3=======#======#====

        img11 = Image.open(r"C:\Users\asus\OneDrive\Pictures\Feedback\8a5a7930-d0bd-432a-8c6d-5d7ac2398713.png")
        img11 = img11.resize((270, 50), PIL.Image.Resampling.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        Lbimage = Label(head_framea3, image=self.photoimg11, bg="#A7C7E7", bd=-10)
        Lbimage.place(x=0, y=220, width=270, height=50)
        # ============3
        img12 = Image.open(r"C:\Users\asus\OneDrive\Pictures\Feedback\ambulance.jpg")
        img12 = img12.resize((80, 50), PIL.Image.Resampling.LANCZOS)
        self.photoimg12 = ImageTk.PhotoImage(img12)
        blood = Button(head_framea3, image=self.photoimg12, command=self.amb,cursor="hand2", bd=-20)
        blood.place(x=270, y=220, height=50)

        # ===========#=4=======#======#====

        img13= Image.open(r"C:\Users\asus\OneDrive\Pictures\Feedback\feb05b0b-4526-4f1e-ad50-f85de8ba28ca.png")
        img13 = img13.resize((270, 50), PIL.Image.Resampling.LANCZOS)
        self.photoimg13 = ImageTk.PhotoImage(img13)
        Lbimage = Label(head_framea3, image=self.photoimg13, bg="#A7C7E7", bd=-10)
        Lbimage.place(x=0, y=310, width=270, height=50)
        # ============4
        img14 = Image.open(r"C:\Users\asus\OneDrive\Pictures\Feedback\blood.jpg")
        img14 = img14.resize((80, 50), PIL.Image.Resampling.LANCZOS)
        self.photoimg14= ImageTk.PhotoImage(img14)
        ambulance = Button(head_framea3, image=self.photoimg14,command=self.blo, cursor="hand2", bd=-20)
        ambulance.place(x=270, y=310, height=50)


        #==========5============

        img15 = Image.open(r"C:\Users\asus\OneDrive\Pictures\Feedback\6d7b9bc1-1f13-4b4b-9115-558db7900f47.png")
        img15 = img15.resize((180, 50), PIL.Image.Resampling.LANCZOS)
        self.photoimg15= ImageTk.PhotoImage(img15)
        details = Button(head_framea3, image=self.photoimg15,command=self.prf, cursor="hand2", bd=-90,bg="#A7C7E7")
        details.place(x=70, y=420, height=50)
        #==========write side========#A97882#1D6F58#1D6F58
        search_button = ctk.CTkButton(
            master=head_framea3,
            text="Log Out",
            width=180,  # Button width
            height=50,  # Button height
            corner_radius=200,  # Rounded corners
            fg_color="#303030",  # Background color (similar to the image)
            text_color="white",  # Text color
            font=("Helvetica", 19, "bold"), # Font styling
            command = self.out
        )
        search_button.place(x=68, y=500)


        head_fr4 = ctk.CTkFrame(head_framea3, fg_color="#1D6F58", width=1140, height=570)
        head_fr4.place(x=360, y=20)

        user = ctk.CTkLabel(head_fr4,text="We are developing a Hospital Management System (HMS) to streamline healthcare services, making them more efficient,\n "
        "accessible, and transparent. The system is designed to manage various aspects of hospital operations such as patient"
                                        " re-\ngistration, appointment scheduling, doctor availability, billing, and medical records. \n"
                                        "\n"
                                        "\n"
                                        "Benefits:\n\n"
                                        "Efficiency: The HMS will automate routine tasks like patient management, reducing manual errors and freeing up time \n"
                                        " for medical staff to focus on patient care.                                                                                                                            \n\n"
                                        "Centralized Records: Patients' medical histories, treatments, and prescriptions are securely stored in one place, which \n"
                                        "ensures that doctors have easy access to essential information.                                                                                         \n\n"
                                        "Appointment Scheduling: The system will allow patients to book appointments with available doctors online, reducing \n"
                                        "wait times and improving patient satisfaction.                                                                                                                    \n\n"
                                        "Billing Management: It will automate the billing process, generating accurate invoices and making payment tracking ea-\n"
                                        "sier for both the hospital and patients.                                                                                                                                 \n\n"
                                        "Improved Communication: The system provides real-time updates to both patients and staff, ensuring smooth communic-\nation "
                                        "and better management of hospital resources                                                                                                              \n\n\n"
                                        "Note: For any assistance, please reach out to our Helpline: 01641346362. We’re here to help with any queries or support you might need!"
                            ,
                            font=("Arial", 12), justify=LEFT)
        user.place(x=10, y=20)
    def prf(self):
        self.new_window = Toplevel(self.root)
        self.app = profilewin(self.new_window)
    def doc(self):
        self.new_window = Toplevel(self.root)
        self.app = doctor_win(self.new_window)
    def amb(self):
        self.new_window = Toplevel(self.root)
        self.app =  ambulance_win(self.new_window)
    def blo(self):
        self.new_window = Toplevel(self.root)
        self.app = blood_win(self.new_window)
    def med(self):
        self.new_window = Toplevel(self.root)
        self.app = medicin_win(self.new_window)

    def out(self):
        self.root.destroy()


if __name__ == '__main__':
    root=Tk()
    obj=homewin(root)
    root.mainloop()
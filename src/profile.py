import random
from tkinter import *
import PIL.Image
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

import os
from PIL import Image, ImageDraw, ImageTk


class profilewin:
    def __init__(self,root):


        self.root=root
        self.root.title("Login System")
        self.root.geometry("1160x568+360+180")

        head_frame = Label(self.root, text="MedXpert", font=("times new roman", 25, "bold"), bg="#303030", fg="white")
        head_frame.place(x=0, y=0, height=70, width=1160)
        # head_frame2 = Frame(head_frame, bg="#303030")
        # head_frame2.place(x=460, y=10, height=48, width=250)
        image_path = r"C:\Users\asus\OneDrive\Pictures\Feedback\photo_2024-11-15_22-14-09.jpg"

        try:
            if os.path.exists(image_path):
                # Load and resize image
                image = Image.open(image_path).resize((65, 65))

                # Create a circular mask
                mask = Image.new("L", (65, 65), 0)
                draw = ImageDraw.Draw(mask)
                draw.ellipse((0, 0, 65, 65), fill=255)

                # Apply mask to create a circular image
                circular_image = Image.new("RGBA", (65, 65))
                circular_image.paste(image, (0, 0), mask=mask)

                # Convert to a format compatible with Tkinter
                ctk_image = ImageTk.PhotoImage(circular_image)

                # Place the image in the head_frame
                img_label = Label(head_frame, image=ctk_image, bg="#303030")
                img_label.image = ctk_image  # Keep reference
                img_label.place(x=0, y=0)  # Adjust coordinates as needed
            else:
                print(f"Image not found at path: {image_path}")
        except Exception as e:
            print(f"Error loading or displaying image: {e}")

        # ========down frame r8=====

        rightframe= Frame(self.root, bg="white", relief=RIDGE, bd=-2)
        rightframe.place(x=0, y=70, height=498, width=580)

        img15 = Image.open(r"C:\Users\asus\OneDrive\Pictures\Feedback\pp.jpg")
        img15 = img15.resize((590, 198), PIL.Image.Resampling.LANCZOS)
        self.photoimg15 = ImageTk.PhotoImage(img15)
        profilep = Label(rightframe, image=self.photoimg15, bd=-90, bg="blue")
        profilep.place(x=-3, y=2)

        img5 = Image.open(r"C:\Users\asus\OneDrive\Pictures\Feedback\myp.jpg")
        img5 = img5.resize((580, 50), PIL.Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        profilep = Button(rightframe, image=self.photoimg5,command=self.personald, bd=-90, bg="white",cursor="hand2")
        profilep.place(x=0, y=202)

        img6= Image.open(r"C:\Users\asus\OneDrive\Pictures\Feedback\favorites.jpg")
        img6= img6.resize((580, 50), PIL.Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        favourite = Button(rightframe, image=self.photoimg6,cursor="hand2", bd=-90, bg="white")
        favourite.place(x=0, y=254)


        img7 = Image.open(r"C:\Users\asus\OneDrive\Pictures\Feedback\myorder.jpg")
        img7 = img7.resize((580, 50), PIL.Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        myorder = Button(rightframe, image=self.photoimg7, bd=-90, bg="white",cursor="hand2")
        myorder.place(x=0, y=306)

        img8= Image.open(r"C:\Users\asus\OneDrive\Pictures\Feedback\termsandpolicis.jpg")
        img8= img8.resize((580, 50), PIL.Image.Resampling.LANCZOS)
        self.photoimg8= ImageTk.PhotoImage(img8)
        termsandpolicis = Button(rightframe, image=self.photoimg8, bd=-90, bg="white", cursor="hand2")
        termsandpolicis.place(x=0, y=358)

        img9 = Image.open(r"C:\Users\asus\OneDrive\Pictures\Feedback\rateus.jpg")
        img9 = img9.resize((580, 50), PIL.Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        rateus = Button(rightframe, image=self.photoimg9, bd=-90, bg="white", cursor="hand2")
        rateus.place(x=0, y=410)

        # ========down frame left=====
        leftframe = Frame(self.root, bg="white", relief=RIDGE, bd=-2)
        leftframe.place(x=581, y=70, height=498, width=580)



        imga = Image.open(r"C:\Users\asus\OneDrive\Pictures\photo_2024-10-13_22-02-26.jpg")
        imga = imga.resize((580, 196), PIL.Image.Resampling.LANCZOS)
        self.photoimga = ImageTk.PhotoImage(imga)
        profilep = Label(leftframe, image=self.photoimga, bd=1, bg="blue",relief=RIDGE)
        profilep.place(x=0, y=0)

        imgb= Image.open(r"C:\Users\asus\OneDrive\Pictures\Feedback\shareapp.jpg")
        imgb= imgb.resize((580, 50), PIL.Image.Resampling.LANCZOS)
        self.photoimgb= ImageTk.PhotoImage(imgb)
        shareapp= Button(leftframe, image=self.photoimgb, bd=-90, bg="white", cursor="hand2")
        shareapp.place(x=0, y=204)

        imgc= Image.open(r"C:\Users\asus\OneDrive\Pictures\Feedback\aboutus.jpg")
        imgc= imgc.resize((580, 50), PIL.Image.Resampling.LANCZOS)
        self.photoimgc = ImageTk.PhotoImage(imgc)
        aboutus= Button(leftframe, image=self.photoimgc, cursor="hand2", bd=-90, bg="white")
        aboutus.place(x=0, y=254)

        imgd= Image.open(r"C:\Users\asus\OneDrive\Pictures\Feedback\help and support.jpg")
        imgd= imgd.resize((580, 50), PIL.Image.Resampling.LANCZOS)
        self.photoimgd = ImageTk.PhotoImage(imgd)
        support= Button(leftframe, image=self.photoimgd, bd=-90, bg="white", cursor="hand2")
        support.place(x=0, y=306)

        imge= Image.open(r"C:\Users\asus\OneDrive\Pictures\Feedback\reportaproblem.jpg")
        imge= imge.resize((580, 50), PIL.Image.Resampling.LANCZOS)
        self.photoimge = ImageTk.PhotoImage(imge)
        reportaproblem = Button(leftframe, image=self.photoimge, bd=-90, bg="white", cursor="hand2")
        reportaproblem.place(x=0, y=358)

        imgf= Image.open(r"C:\Users\asus\OneDrive\Pictures\Feedback\lastpage.jpg")
        imgf= imgf.resize((590, 60), PIL.Image.Resampling.LANCZOS)
        self.photoimgf = ImageTk.PhotoImage(imgf)
        lastpage =Label(leftframe, image=self.photoimgf, bd=-90, bg="white")
        lastpage.place(x=0, y=445,width=580, height=50)

    def personald(self):
        leftframe = Frame(self.root, bg="white", relief=RIDGE, bd=1)
        leftframe.place(x=580, y=70, height=200, width=580)
        frame = Label(self.root,text="Name                          \n"
                                     "Birth Date                  \n"
                                     "Gender                        \n"
                                     "Mail                            \n"
                                     "Blood group               \n"
                                     "Weight                       \n"
                                     "Height                        ", font=("times new roman", 15, "bold"), bg="white", bd=-2,fg="black")
        frame.place(x=581, y=70, height=198, width=200)
        frame2 =Label(self.root,text=": Md. Jaker Ali                                                     \n"
                                     ": 5th October, 1996                                              \n"
                                     ": Male                                                                  \n"
                                     ": jaker15456@gmail.com                                    \n"
                                     ": AB+                                                                  \n"
                                     ": 78 kg                                                                  \n"
                                     ": 1.34 m                                                                ", font=("times new roman", 15), bg="white", bd=-2)
        frame2.place(x=781, y=70, height=198, width=380)


if __name__ == '__main__':
    root=Tk()
    obj=profilewin(root)
    root.mainloop()
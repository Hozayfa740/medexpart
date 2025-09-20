import PIL.Image
import random
from tkinter import *
from PIL import Image
import customtkinter as ctk
import mysql.connector
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageDraw, ImageTk
import os


class ambulance_win:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1160x568+360+180")
#bg="#0077B6"
        head_frame = Label(self.root, text="MedXpert", font=("times new roman", 25, "bold"), bg="#303030", fg="white")
        head_frame.place(x=0, y=0, height=70, width=1160)
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

        #==================ambulance picture==============
        img2= Image.open(r"C:\Users\asus\OneDrive\Pictures\Feedback\ambulance.jpg")
        img2= img2.resize((450, 350), PIL.Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        Lbimage = Label(self.root, image=self.photoimg2, relief=RIDGE)
        Lbimage.place(x=0, y=70, width=450, height=350)


        head_fr4 = ctk.CTkFrame(self.root, fg_color="#303030", width=435, height=150)
        head_fr4.place(x=0, y=420)

        user = ctk.CTkLabel(head_fr4,
                            text="At MedExPart, we’re committed to bringing timely \n"
                                 "and reliable healthcare support right to your fingertips.\n"
                                 "Our ambulance service ensures that you can access emergency \n"
                                 "transportation whenever needed, with trusted professionals\n"
                                 "ready to respond 24/7. Your health and safety are our top priorities.",
                            font=("Arial", 12), justify=LEFT)
        user.place(x=10, y=20)



        # ============label frame right=========
        label_frameright = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System ",
                                      font=("times new roman", 17, "bold"),bg="#700124",
                                      fg="white")
        label_frameright.place(x=435, y=70, width=725, height=500)
        #===========================================



        lbl_sarchby = ctk.CTkLabel(label_frameright, text="Search By", font=("Arial", 12, "bold"), anchor="w", fg_color="#A97882")
        lbl_sarchby.grid(row=0, column=0, padx=5, pady=10, sticky="w")


        combo_sarch = ctk.CTkComboBox(label_frameright, width=24, values=("Location", "Contact_number"),
                                      font=("Arial", 11, "bold"))
        combo_sarch.set("Location")
        combo_sarch.grid(row=0, column=1)

        entry_src = ctk.CTkEntry(label_frameright, font=("Arial", 11, "bold"))
        entry_src.grid(row=0, column=2, padx=10, pady=10)

        # ============btn sarch========
        search_button = ctk.CTkButton(
            master=label_frameright,
            text="Search",
            width=100,  # Button width
            height=40,  # Button height
            corner_radius=20,  # Rounded corners
            fg_color="#303030",  # Background color (similar to the image)
            text_color="white",  # Text color
            font=("Helvetica", 12, "bold")  # Font styling
        )
        search_button.grid(row=0, column=5, padx=1)
        showall_button = ctk.CTkButton(
            master=label_frameright,
            text="showall",
            width=100,  # Button width
            height=40,  # Button height
            corner_radius=20,  # Rounded corners
            fg_color="#303030",  # Background color (similar to the image)
            text_color="white",  # Text color
            font=("Helvetica", 12, "bold")  # Font styling
        )
        showall_button.grid(row=0, column=6, padx=1)
        # ---------------show table----------#
        tableframeshow = Frame(label_frameright, bd=1, relief=RIDGE,bg="#C0C0C0")
        tableframeshow.place(x=0, y=50, width=710, height=410)
        style = ttk.Style()

        # Configure the style for Treeview
        style.configure("Custom.Treeview",
                        background="#f0f0f0",  # Background color for rows
                        foreground="black",  # Text color
                        rowheight=25,  # Row height
                        fieldbackground="#3b87d4",
                        relief="solid" ,
                        bd=10# Background color for empty area
                        )

        # Configure selected row color
        style.map("Custom.Treeview",
                  background=[("selected", "#a6c6ff")],  # Background color when selected
                  foreground=[("selected", "white")]  # Text color when selected
                  )

        self.Details_Table = ttk.Treeview(tableframeshow,style="Custom.Treeview", columns=(
             "Location", "Contact_number", "Service_type", "Driver_name", "Service_Time", "Booking_history","Driver_email","Feed_Back"))


        #===============================table====================================


        scroll_x = Scrollbar(tableframeshow, orient=HORIZONTAL, command=self.Details_Table.xview)
        scroll_y = Scrollbar(tableframeshow, orient=VERTICAL, command=self.Details_Table.yview)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        self.Details_Table.configure(xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        self.Details_Table.heading("Location", text="Location")
        self.Details_Table.heading("Contact_number", text="Contact Number")
        self.Details_Table.heading("Service_type", text="Service Type")
        self.Details_Table.heading("Driver_name", text="Driver Name")
        self.Details_Table.heading("Service_Time", text="Service Time")
        self.Details_Table.heading("Booking_history", text="Booking History")
        self.Details_Table.heading("Driver_email", text="Driver Email")
        self.Details_Table.heading("Feed_Back", text="Feed Back")
        self.Details_Table["show"] = "headings"
        self.Details_Table.column("Location", width=100)
        self.Details_Table.column("Contact_number", width=100)
        self.Details_Table.column("Service_type", width=100)
        self.Details_Table.column("Driver_name", width=100)
        self.Details_Table.column("Service_Time", width=100)
        self.Details_Table.column("Booking_history", width=100)
        self.Details_Table.column("Driver_email", width=100)
        self.Details_Table.column("Feed_Back", width=100)

        self.Details_Table.pack(fill=BOTH, expand=1)
        self.Details_Table.bind("<ButtonRelease-1>")
        self.fetch_data()

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="34632", database="medexpart",
                                       auth_plugin="mysql_native_password")
        my_cursor = conn.cursor(buffered=True)
        my_cursor.execute("select * from ambulance_win")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Details_Table.delete(*self.Details_Table.get_children())
            for i in rows:
                self.Details_Table.insert("", END, values=i)
        conn.commit()
        conn.close()











if __name__ == '__main__':
    root = Tk()
    obj = ambulance_win(root)
    root.mainloop()

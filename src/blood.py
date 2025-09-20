
from tkinter import *
import PIL.Image
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import customtkinter as ctk
from PIL import Image, ImageDraw, ImageTk
import os

class blood_win:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1160x568+360+180")


        self.ver_Name = StringVar()
        self.ver_Age = StringVar()
        self.ver_Gender = StringVar()
        self.ver_Blood_Group = StringVar()
        self.ver_phone_number = StringVar()
        self.ver_Email = StringVar()
        self.ver_Address = StringVar()
        self.ver_Last_Donaton_Date = StringVar()
        self.ver_search = StringVar()
        self.text_search = StringVar()

        head_frame = Label(self.root, text="MedXpert", font=("times new roman", 25, "bold"), bg="#303030", fg="white")
        head_frame.place(x=0, y=0, height=70, width=1160)

        #==========details of blood doner==========
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

        #=================================#========================

        label_frameleft = LabelFrame(self.root, bd=0, relief=RIDGE,
                                     font=("times new roman", 15, "bold"), bg="#A97882")
        label_frameleft.place(x=0, y=70, width=445, height=540)

        label_title = ctk.CTkLabel(label_frameleft, text="BLOOD DONOR DETAILS",
                                   font=("Helvetica", 17, "bold"), text_color="white")
        label_title.grid(row=0, column=0, columnspan=2, pady=10)

        # Form Entries
        labels = ["Name", "Age", "Gender", "Blood Group", "Phone Number", "Email", "Address", "Last Donation Date"]
        variables = [self.ver_Name, self.ver_Age, self.ver_Gender, self.ver_Blood_Group,
                     self.ver_phone_number, self.ver_Email, self.ver_Address, self.ver_Last_Donaton_Date]

        for i, (label_text, var) in enumerate(zip(labels, variables)):
            label = ctk.CTkLabel(label_frameleft, text=label_text, font=("Helvetica", 14, "bold"), text_color="white")
            label.grid(row=i + 1, column=0, sticky="w", padx=10, pady=5)

            if label_text == "Gender":
                entry = ctk.CTkComboBox(label_frameleft, values=["Male", "Female", "Other"],
                                        variable=self.ver_Gender, width=200)
                entry.grid(row=i + 1, column=1, padx=10, pady=5)
                entry.set("Male")  # Default selection
            else:
                entry = ctk.CTkEntry(label_frameleft, textvariable=var, width=200)
                entry.grid(row=i + 1, column=1, padx=10, pady=5)

        # ===============btn============down==
        btn_frame = Frame(label_frameleft, bd=-1,bg="#A97882")
        btn_frame.place(x=0, y=380, width=412)
        #======add========
        search_button = ctk.CTkButton(
            master=btn_frame,
            text="Add",
            width=100,  # Button width
            height=40,  # Button height
            corner_radius=20,  # Rounded corners
            fg_color="#303030",  # Background color (similar to the image)
            text_color="white",  # Text color
            font=("Helvetica", 12, "bold"),  # Font styling
            command = self.add_data
        )
        search_button.grid(row=0, column=0, padx=1)


        #=======update==================================
        update_button = ctk.CTkButton(
            master=btn_frame,
            text="Update",
            width=100,  # Button width
            height=40,  # Button height
            corner_radius=20,  # Rounded corners
            fg_color="#303030",  # Background color (similar to the image)
            text_color="white",  # Text color
            font=("Helvetica", 12, "bold"),  # Font styling

        )
        update_button.grid(row=0, column=1, padx=1)

        #=======================delete========================
        delete_button = ctk.CTkButton(
            master=btn_frame,
            text="Delete",
            width=100,  # Button width
            height=40,  # Button height
            corner_radius=20,  # Rounded corners
            fg_color="#303030",  # Background color (similar to the image)
            text_color="white",  # Text color
            font=("Helvetica", 12, "bold"),  # Font styling

        )
        delete_button.grid(row=0, column=2, padx=1)


        #==================================reset=========================
        delete_button = ctk.CTkButton(
            master=btn_frame,
            text="Reset",
            width=100,  # Button width
            height=40,  # Button height
            corner_radius=20,  # Rounded corners
            fg_color="#303030",  # Background color (similar to the image)
            text_color="white",  # Text color
            font=("Helvetica", 12, "bold"),  # Font styling

        )
        delete_button.grid(row=0, column=3, padx=1)

        # ============label frame right=========#9E4244


        label_frameright = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System ",
                                      font=("times new roman", 17, "bold"), bg="#700124",
                                      fg="white")
        label_frameright.place(x=435, y=70, width=725, height=490)
        lbl_sarchby = ctk.CTkLabel(label_frameright, text="Search By", font=("Arial", 12, "bold"), anchor="w",
                                   fg_color="#A97882")
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
            fg_color="#A97882",  # Background color (similar to the image)
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
            fg_color="#A97882",  # Background color (similar to the image)
            text_color="white",  # Text color
            font=("Helvetica", 12, "bold")  # Font styling
        )
        showall_button.grid(row=0, column=6, padx=1)

        # ---------------show table----------#
        tableframeshow = Frame(label_frameright, bd=1, relief=RIDGE)
        tableframeshow.place(x=0, y=55, width=710, height=410)
        scroll_x = ttk.Scrollbar(tableframeshow, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(tableframeshow, orient=VERTICAL)
        self.Details_Table = ttk.Treeview(tableframeshow, columns=(
             "Name", "Age", "Gender", "Blood_Group", "Phone_Number", "Email","Address","Last_Donaton_Date"))


        #===============================table====================================

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Details_Table.xview)
        scroll_y.config(command=self.Details_Table.yview)

        self.Details_Table.heading("Name", text="Name")
        self.Details_Table.heading("Age", text="Age")
        self.Details_Table.heading("Gender", text="Gender")
        self.Details_Table.heading("Blood_Group", text="Blood Group")
        self.Details_Table.heading("Phone_Number", text="Phone Number")
        self.Details_Table.heading("Email", text="Email")

        self.Details_Table.heading("Address", text="Address")
        self.Details_Table.heading("Last_Donaton_Date", text="Last Donaton Date")

        self.Details_Table["show"] = "headings"

        self.Details_Table.column("Name", width=100)
        self.Details_Table.column("Age", width=100)
        self.Details_Table.column("Gender", width=100)
        self.Details_Table.column("Blood_Group", width=100)
        self.Details_Table.column("Phone_Number", width=100)
        self.Details_Table.column("Email", width=100)
        self.Details_Table.column("Address", width=100)
        self.Details_Table.column("Last_Donaton_Date", width=100)
        self.Details_Table.pack(fill=BOTH, expand=1)
        self.Details_Table.bind("<ButtonRelease-1>")
        self.fetch_data()
    def add_data(self):
        if self.ver_Email == "" or self.ver_Blood_Group == "":
            messagebox.showerror("medexpart", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="34632", database="medexpart",
                                               auth_plugin="mysql_native_password")
                my_cursor = conn.cursor(buffered=True)
                my_cursor.execute("insert into blood_win values(%s,%s,%s,%s,%s,%s,%s,%s)", (

                    self.ver_Name.get(),
                    self.ver_Age.get(),
                    self.ver_Gender.get(),
                    self.ver_Blood_Group.get(),
                    self.ver_phone_number.get(),
                    self.ver_Email.get(),
                    self.ver_Address.get(),
                    self.ver_Last_Donaton_Date.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("medexpart", "All details has been added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning", f"some thing went wrong :{str(es)}", parent=self.root)
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="34632", database="medexpart",
                                       auth_plugin="mysql_native_password")
        my_cursor = conn.cursor(buffered=True)
        my_cursor.execute("select * from blood_win")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Details_Table.delete(*self.Details_Table.get_children())
            for i in rows:
                self.Details_Table.insert("", END, values=i)
        conn.commit()
        conn.close()











if __name__ == '__main__':
    root = Tk()
    obj = blood_win(root)
    root.mainloop()

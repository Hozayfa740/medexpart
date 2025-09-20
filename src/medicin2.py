import os
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import customtkinter as ctk
import mysql.connector
import random
from tkinter import *
import PIL.Image
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from singup import SignupWin


# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="34632",
    database="medexpart",
    auth_plugin="mysql_native_password"
)
my_cursor = conn.cursor(buffered=True)


class DoctorWin:
    def __init__(self, root):
        self.root = root
        self.root.title("MedExPart - Doctor Consultation")
        self.root.geometry("1160x568+360+180")

        # Header Frame
        head_frame = tk.Frame(self.root, bg="#303030")
        head_frame.place(x=0, y=0, height=70, width=1160)

        # Title Image
        img1 = self.load_image(r"C:\Users\asus\OneDrive\Pictures\Feedback\titlepic.jpg", (400, 110))
        if img1:
            self.photoimg1 = ImageTk.PhotoImage(img1)
            tk.Label(head_frame, image=self.photoimg1, relief=tk.RIDGE).place(x=460, y=10, width=250, height=48)

        # Doctor Image
        img2 = self.load_image(r"C:\Users\asus\OneDrive\Pictures\Feedback\conceltant.jpg", (450, 300))
        if img2:
            self.photoimg2 = ImageTk.PhotoImage(img2)
            tk.Label(self.root, image=self.photoimg2, relief=tk.RIDGE).place(x=0, y=70, width=450, height=300)

        # Description Frame
        description_frame = ctk.CTkFrame(self.root, fg_color="Black", width=435, height=200)
        description_frame.place(x=0, y=370)
        description_text = (
            "At MedExPart, our doctor consultation service connects you to expert medical advice "
            "anytime, anywhere. With access to certified professionals across specialties, we ensure "
            "that quality healthcare is only a click away."
        )
        ctk.CTkLabel(description_frame, text=description_text, font=("Arial", 12), justify="left").place(x=10, y=20)

        # Search System
        label_frame_right = tk.LabelFrame(self.root, bd=2, relief=tk.RIDGE, text="View Details And Search System",
                                          font=("times new roman", 17, "bold"), bg="black", fg="white")
        label_frame_right.place(x=435, y=70, width=725, height=500)

        tk.Label(label_frame_right, text="Search By", font=("Arial", 12, "bold"), bg="black", fg="white").grid(row=0, column=0, padx=5, pady=10)
        ctk.CTkComboBox(label_frame_right, values=["Location", "Contact_number"], font=("Arial", 11, "bold")).grid(row=0, column=1, padx=5, pady=10)
        ctk.CTkEntry(label_frame_right, font=("Arial", 11)).grid(row=0, column=2, padx=10, pady=10)

        # Display Medicines
        self.table_frame = tk.Frame(label_frame_right, bd=1, relief=tk.RIDGE, bg="#C0C0C0")
        self.table_frame.place(x=0, y=50, width=710, height=370)

        # Canvas and Scrollbar for Medicines
        canvas = tk.Canvas(self.table_frame, bg="#C0C0C0")
        scrollbar = tk.Scrollbar(self.table_frame, orient="vertical", command=canvas.yview)
        frame = tk.Frame(canvas, bg="#C0C0C0")
        canvas.create_window((0, 0), window=frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.display_medicines(frame)

    def load_image(self, image_path, size):
        """Load and resize an image."""
        try:
            if os.path.exists(image_path):
                img = Image.open(image_path)
                return img.resize(size, Image.Resampling.LANCZOS)
            else:
                print(f"Image not found: {image_path}")
                return None
        except Exception as e:
            print(f"Error loading image: {e}")
            return None

    def fetch_medicines(self):
        """Fetch all medicines from the database."""
        try:
            my_cursor.execute("SELECT * FROM medicines")
            return my_cursor.fetchall()
        except mysql.connector.Error as e:
            print(f"Database error: {e}")
            return []

    def display_medicines(self, frame):
        """Display medicines in a scrollable frame."""
        medicines = self.fetch_medicines()

        for widget in frame.winfo_children():
            widget.destroy()
        n=7

        for index, (id, name, price, quantity, description, rating, sold, image_path) in enumerate(medicines):
            index = index * n
            tk.Label(frame, text=f"Name: {name}", font=("Arial", 12)).grid(row=index+6, column=0, sticky="w")
            tk.Label(frame, text=f"Price: ${price}", font=("Arial", 12)).grid(row=index, column=1, sticky="w")
            tk.Label(frame, text=f"Quantity: {quantity}", font=("Arial", 12)).grid(row=index+1, column=1, sticky="w")
            tk.Label(frame, text=f"Rating: {rating} ★", font=("Arial", 12)).grid(row=index+3, column=1, sticky="w")
            tk.Label(frame, text=f"Sold: {sold}", font=("Arial", 12)).grid(row=index+4, column=1, sticky="w")

            # Medicine Image
            if os.path.exists(image_path):
                try:
                    img = Image.open(image_path).resize((150, 150), Image.Resampling.LANCZOS)
                    photo = ImageTk.PhotoImage(img)
                    img_label = tk.Label(frame, image=photo, bg="#C0C0C0")
                    img_label.image = photo  # Keep a reference
                    img_label.grid(row=index, column=0)
                except Exception as e:
                    print(f"Error loading image: {e}")

            n=n+1

            # Buy Button
            tk.Button(frame, text="Buy", bg="green", fg="white",
                      command=lambda med_id=id: self.buy_medicine(med_id, frame)).grid(row=index + 3, column=1, padx=10, pady=5)

    def buy_medicine(self, med_id, frame):
        """Handle medicine purchase."""
        try:
            my_cursor.execute("SELECT quantity FROM medicines WHERE id=%s", (med_id,))
            quantity = my_cursor.fetchone()[0]

            if quantity > 0:
                my_cursor.execute("UPDATE medicines SET quantity = quantity - 1, sold = sold + 1 WHERE id=%s", (med_id,))
                conn.commit()
                messagebox.showinfo("Success", "Medicine purchased successfully!")
            else:
                messagebox.showerror("Out of Stock", "This medicine is currently out of stock.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        self.display_medicines(frame)


if __name__ == "__main__":
    root = tk.Tk()
    app = DoctorWin(root)
    root.mainloop()

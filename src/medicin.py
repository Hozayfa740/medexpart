import os
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import customtkinter as ctk
import mysql.connector
import random
from tkinter import *
import PIL.Image
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageTk


# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="34632",
    database="medexpart",
    auth_plugin="mysql_native_password"
)
my_cursor = conn.cursor(buffered=True)


class medicin_win:
    def __init__(self, root):
        self.root = root
        self.root.title("MedExPart - Doctor Consultation")
        self.root.geometry("1160x568+360+180")


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

        # Doctor Image
        img2 = self.load_image(r"C:\Users\asus\OneDrive\Pictures\photo_2024-10-13_22-05-02.jpg", (450, 370))
        if img2:
            self.photoimg2 = ImageTk.PhotoImage(img2)
            tk.Label(self.root, image=self.photoimg2, relief=tk.RIDGE).place(x=0, y=70, width=450, height=370)

        # Description Frame
        description_frame = ctk.CTkFrame(self.root, fg_color="#303030", width=435, height=200)
        description_frame.place(x=0, y=440)
        description_text = (
            "At MedExPart, our doctor consultation service connects you to expert medical\n"
            " advice "
            "anytime, anywhere. With access to certified professionals across\n"
            " specialties, we ensure "
            "that quality healthcare is only a click away."
        )
        ctk.CTkLabel(description_frame, text=description_text, font=("Arial", 12), justify="left").place(x=10, y=20)

        # Search System
        label_frame_right = tk.LabelFrame(self.root, bd=2, relief=tk.RIDGE, text="View Details And Search System",
                                          font=("times new roman", 17, "bold"), fg="white", bg="#700124")
        label_frame_right.place(x=435, y=70, width=725, height=500)

        tk.Label(label_frame_right, text="Search By", font=("Arial", 12, "bold"), bg="#A97882",
                                  fg="white").grid(row=0, column=0, padx=5, pady=10)
        ctk.CTkComboBox(label_frame_right, values=["Name", "code name"], font=("Arial", 11, "bold")).grid(row=0, column=1, padx=5, pady=10)
        ctk.CTkEntry(label_frame_right, font=("Arial", 11)).grid(row=0, column=2, padx=10, pady=10)
        # ============btn sarch========
        search_button = ctk.CTkButton(
            master=label_frame_right,
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
            master=label_frame_right,
            text="showall",
            width=100,  # Button width
            height=40,  # Button height
            corner_radius=20,  # Rounded corners
            fg_color="#A97882",  # Background color (similar to the image)
            text_color="white",  # Text color
            font=("Helvetica", 12, "bold")  # Font styling
        )
        showall_button.grid(row=0, column=6, padx=1)

        # Display Medicines
        self.tableframeshow = tk.Frame(label_frame_right, bd=1, bg="#C0C0C0")
        self.tableframeshow.place(x=4, y=50, width=710, height=470)
        self.canvas = tk.Canvas(self.tableframeshow)
        scrollbar = tk.Scrollbar(self.tableframeshow, orient="vertical", command=self.canvas.yview)
        frame = tk.Frame(self.canvas, bg="#C0C0C0")

        frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.canvas.create_window((0, 0), window=frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        self.display_medicines(frame)

    def load_image(self, image_path, size):
        """Load an image from a given path with resizing."""
        try:
            if os.path.exists(image_path):
                img = Image.open(image_path)
                img = img.resize(size, Image.Resampling.LANCZOS)
                return img
            else:
                print(f"Image not found: {image_path}")
                return None
        except Exception as e:
            print(f"Error loading image: {e}")
            return None

    def buy_medicine(self, med_id, frame):
        my_cursor.execute("SELECT quantity FROM medicines WHERE id=%s", (med_id,))
        quantity = my_cursor.fetchone()[0]

        if quantity > 0:
            my_cursor.execute("UPDATE medicines SET quantity = quantity - 1, sold = sold + 1 WHERE id=%s", (med_id,))
            conn.commit()
            messagebox.showinfo("Success", "Medicine purchased successfully!")
        else:
            messagebox.showerror("Out of Stock", "This medicine is currently out of stock.")
        self.display_medicines(frame)

    def fetch_medicines(self):
        my_cursor.execute("SELECT * FROM medicines")
        rows = my_cursor.fetchall()
        return rows

    def display_medicines(self, frame):
        medicines = self.fetch_medicines()

        for widget in frame.winfo_children():
            widget.destroy()
        n = 7
        k=0

        # Displaying medicines in a layout similar to the image you provided
        # Refer to "Screenshot_2024-11-13-00-58-02-01_f9b251d62f6eb22790b83e2e3c410dd0.jpg" for design reference

        for index, (id, name, price, quantity, description, rating, sold, image_path) in enumerate(medicines):
            index =(index//2) * n
            k=k%4
            tk.Label(frame, text=name, font=("Arial", 14), bg="#C0C0C0").grid(row=index + 6, column=k+0, padx=10, pady=5)
            tk.Label(frame, text=f"Price: ৳{price}", font=("Arial", 12), bg="#C0C0C0").grid(row=index, column=k+1,
                                                                                            padx=10, pady=5)
            tk.Label(frame, text=f"Stock: {quantity}", font=("Arial", 12), bg="#C0C0C0").grid(row=index + 1, column=k+1,
                                                                                              padx=10,
                                                                                              pady=5)
            tk.Label(frame, text=f"Rating: {rating} ⭐️", font=("Arial", 12), bg="#C0C0C0").grid(row=index + 2, column=k+1,
                                                                                                padx=10,
                                                                                                pady=5)
            tk.Label(frame, text=f"Sold: {sold}", font=("Arial", 12), bg="#C0C0C0").grid(row=index + 3, column=k+1,
                                                                                         padx=10, pady=5)

            # Replace with actual path

            print("Attempting to load image from path:", image_path)

            try:
                if os.path.exists(image_path):
                    image = Image.open(image_path)
                    image = image.resize((180, 200), PIL.Image.Resampling.LANCZOS)
                    photo = ImageTk.PhotoImage(image)
                    img_label = Label(frame, image=photo)
                    img_label.image = photo
                    img_label.grid(row=index, column=k+0, rowspan=6, padx=20)



                else:
                    print(f"Image not found: {image_path}")
            except Exception as e:
                print(f"Error loading image: {e}")


            # Buy Button
            tk.Button(frame, text="Buy", bg="green", fg="white",
                      command=lambda med_id=id: self.buy_medicine(med_id, frame)).grid(row=index + 4, column=k+1, padx=10, pady=5)
            k=k+2

    def buy_medicine(self, med_id, frame):
        """Handle medicine purchase."""
        try:
            my_cursor.execute("SELECT quantity FROM medicines WHERE id=%s", (med_id,))
            quantity = my_cursor.fetchone()[0]

            if quantity > 0:
                my_cursor.execute("UPDATE medicines SET quantity = quantity - 1, sold = sold + 1 WHERE id=%s", (med_id,))
                conn.commit()
                messagebox.showinfo("Success", "Medicine purchased successfully!",parent=self.root)
            else:
                messagebox.showerror("Out of Stock", "This medicine is currently out of stock.",parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}",parent=self.root)
        self.display_medicines(frame)


if __name__ == "__main__":
    root = tk.Tk()
    app =medicin_win(root)
    root.mainloop()

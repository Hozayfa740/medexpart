import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import StringVar


class SignupWin:
    def __init__(self, root):
        self.root = root
        self.root.title("Signup System")
        self.root.geometry("1550x800+0+0")
        self.root.config(bg="#f7f7f7")

        # Variables for form entries
        self.v_first_name = StringVar()
        self.v_last_name = StringVar()
        self.v_gender = StringVar()
        self.v_blood = StringVar()
        self.v_mobile = StringVar()
        self.v_email = StringVar()
        self.v_address = StringVar()
        self.v_p_password = StringVar()
        self.v_s_password = StringVar()
        self.v_birthdate = StringVar()
        self.v_height = StringVar()
        self.v_weight = StringVar()
        self.v_age = StringVar()

        # Title
        title = tk.Label(self.root, text="Sign Up", font=("Helvetica", 30, "bold"), fg="#ffffff", bg="#1D6F58")
        title.pack(pady=20, fill="x")

        # Signup Frame
        signup_frame = tk.Frame(self.root, bg="#ffffff", bd=2, relief="groove")
        signup_frame.place(x=50, y=100, width=1450, height=600)

        # Left part of the form (personal information)
        left_frame = tk.Frame(signup_frame, bg="#f7f7f7")
        left_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nw")

        self.create_entry(left_frame, "First Name", 0, self.v_first_name)
        self.create_entry(left_frame, "Last Name", 1, self.v_last_name)
        self.create_entry(left_frame, "Date of Birth", 2, self.v_birthdate)
        self.create_combo(left_frame, "Gender", 3, self.v_gender, ["Male", "Female", "Other"])
        self.create_entry(left_frame, "Mobile", 4, self.v_mobile)
        self.create_entry(left_frame, "Email", 5, self.v_email)
        self.create_entry(left_frame, "Age", 6, self.v_age)

        # Right part of the form (physical information)
        right_frame = tk.Frame(signup_frame, bg="#f7f7f7")
        right_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nw")

        self.create_entry(right_frame, "Blood Group", 0, self.v_blood)
        self.create_entry(right_frame, "Height", 1, self.v_height)
        self.create_entry(right_frame, "Weight", 2, self.v_weight)
        self.create_entry(right_frame, "Address", 3, self.v_address)
        self.create_entry(right_frame, "Password", 4, self.v_p_password, show="*")
        self.create_entry(right_frame, "Confirm Password", 5, self.v_s_password, show="*")

        # Buttons
        button_frame = tk.Frame(self.root, bg="#f7f7f7")
        button_frame.place(x=50, y=460, width=1450)

        cancel_button = tk.Button(button_frame, text="Cancel", command=self.cancel, bg="#A97882", fg="white",
                                  font=("Helvetica", 12), width=20, relief="flat", bd=0)
        cancel_button.grid(row=0, column=0, padx=10, pady=10)

        confirm_button = tk.Button(button_frame, text="Sign Up", command=self.signup, bg="#1D6F58", fg="white",
                                   font=("Helvetica", 12), width=20, relief="flat", bd=0)
        confirm_button.grid(row=0, column=1, padx=10, pady=10)

    def create_entry(self, parent, label_text, row, variable, show=None):
        """Create a label and entry widget for the form"""
        label = tk.Label(parent, text=label_text, font=("Helvetica", 12), bg="#f7f7f7", anchor="w")
        label.grid(row=row, column=0, sticky="w", pady=5)

        entry = ttk.Entry(parent, textvariable=variable, font=("Helvetica", 12), width=30, show=show)
        entry.grid(row=row, column=1, pady=5)

    def create_combo(self, parent, label_text, row, variable, options):
        """Create a label and combo box for the form"""
        label = tk.Label(parent, text=label_text, font=("Helvetica", 12), bg="#f7f7f7", anchor="w")
        label.grid(row=row, column=0, sticky="w", pady=5)

        combo = ttk.Combobox(parent, textvariable=variable, values=options, state="readonly", font=("Helvetica", 12),
                             width=28)
        combo.grid(row=row, column=1, pady=5)
        combo.current(0)

    def signup(self):
        """Validate the form and submit the data"""
        if not all([self.v_first_name.get(), self.v_last_name.get(), self.v_birthdate.get(),
                    self.v_gender.get(), self.v_mobile.get(), self.v_email.get(), self.v_age.get(),
                    self.v_blood.get(), self.v_height.get(), self.v_weight.get(), self.v_address.get(),
                    self.v_p_password.get(), self.v_s_password.get()]):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return

        if self.v_p_password.get() != self.v_s_password.get():
            messagebox.showerror("Error", "Passwords do not match", parent=self.root)
            return

        # Here you would connect to your database to store the user info (if needed)
        # For now, just show a success message
        messagebox.showinfo("Success", "Account created successfully", parent=self.root)

    def cancel(self):
        self.root.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    obj = SignupWin(root)
    root.mainloop()

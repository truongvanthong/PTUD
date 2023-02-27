import tkinter as tk
from tkinter import font
from datetime import date
from datetime import datetime
from tkcalendar import DateEntry

class Window:

    def __init__(self, root):
        self.root = root
        self.root.title("Age Calculator")
        self.root.geometry("500x400")

        self.ui_components() # gọi hàm tạo các thành phần giao diện

        # bind "Return" key to calculate button
        self.first.bind("<Return>", lambda event: self.find_age())
        self.second.bind("<Return>", lambda event: self.find_age())

    def ui_components(self):
        # creating head label
        head = tk.Label(self.root, text="Age Calculator")
        head.pack(pady=20)

        # font
        font_style = font.Font(family="Times", size=20, weight="bold", slant="italic", underline=True)

        # setting font to the head
        head.config(font=font_style, fg="green")

        # setting geometry to the head
        head.place(x=100, y=10,width=300, height=60)

        # D.O.B label
        dob = tk.Label(self.root, text="Date of Birth", font=("Times", 14))
        dob.place(x=0, y=80, width=250, height=50)

        # given date label
        given = tk.Label(self.root, text="Given Date", font=("Times", 14))
        given.place(x=300, y=80, width=250, height=50)

        # creating a DateEntry widget to get the d.o.b
        self.first = DateEntry(self.root, 
                                font=("Times", 14, "bold"), 
                                justify="center", width=12,
                                background='darkgreen', foreground='white', borderwidth=2, 
                                date_pattern='dd-mm-yyyy', 
                                year=2002, month=7, day=23)
        self.first.place(x=20, y=130, width=200, height=50)

        # creating a DateEntry widget to get the given date
        current_date = datetime.now()
        self.second = DateEntry(self.root, 
                                font=("Times", 14, "bold"), 
                                justify="center", width=20, 
                                background='darkgreen', foreground='white', borderwidth=2, 
                                date_pattern='dd-mm-yyyy', 
                                year=current_date.year, month=current_date.month, day=current_date.day)
        self.second.place(x=275, y=130, width=200, height=50)

        # create a button for calculate
        calculate = tk.Button(self.root, 
                            text="Calculate", 
                            font=("Times", 14),
                            fg="darkGreen", 
                            command=self.find_age)
        calculate.place(x=200, y=210, width=100, height=40)

        # creating a result label to show the ans
        self.result = tk.Label(self.root,
                                font=("Times", 14),
                                bg="lightgrey", 
                                relief="solid",
                                bd=2,  
                                wraplength=400)
        self.result.place(x=50, y=280, width=400, height=80)

        # bind "Return" key to calculate button
        self.first.bind("<Return>", lambda event: self.find_age())
        self.second.bind("<Return>", lambda event: self.find_age())

    # Hàm tính tuổi bằng cách
    # lấy ngày hiện tại trừ ngày sinh
    # sau đó chia cho 365 để ra số năm
    # chia số ngày còn lại cho 30 để ra số tháng
    # số ngày còn lại là số ngày
    def find_age(self):
        # get the first age and second age
        try:
            dob = datetime.strptime(self.first.get(), "%d-%m-%Y").date()

            given_date = datetime.strptime(self.second.get(), "%d-%m-%Y").date()

            delta = given_date - dob

            years = delta.days // 365
            months = (delta.days % 365) // 30
            days = (delta.days % 365) % 30

            result_text = f"{days} Day(s), {months} Month(s), {years} Year(s)"
            self.result.config(text=result_text) 
        except ValueError:  

            self.result.config(text="Invalid Date Format (DD-MM-YYYY)")

if __name__ == "__main__":
    root = tk.Tk()
    window = Window(root)
    root.mainloop()

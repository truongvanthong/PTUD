import tkinter as tk


class Calculator:
    def __init__(self, master):  # master là cửa sổ chính
        self.master = master
        master.title("Calculator")
        master.configure(bg="#F0F0F0")  # thêm màu nền cho cửa sổ chính

        # create screen widget # tạo màn hình hiển thị
        self.screen = tk.Entry(
            master, width=35, justify="left", font=("Roboto", 20))

        self.screen.grid(row=0, column=0, columnspan=4, padx=5, pady=10)


        # # # create buttons
        buttons = [
            "C", "Del", "%", "/",
            "7", "8", "9", "*",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "0", ".", "√", "="
        ]
        # create and add buttons to grid
        row = 1
        col = 0
        for button in buttons:
            tk.Button(
                master,
                text=button,
                bg="#C5E1A5",  # thêm màu nền cho nút bấm
                fg="#212121",  # thêm màu chữ cho nút bấm
                width=10,
                height=3,
                font=("Roboto", 15),  # thêm font chữ cho nút bấm
                command=lambda x=button: self.handle_click(x) # xử lý khi nhấn nút bấm (xem hàm handle_click) 
            ).grid(row=row, column=col, padx=8, pady=8)
            col += 1
            if col > 3:  # mỗi hàng có 4 cột
                col = 0  # reset cột
                row += 1  # tăng hàng

        # bind keyboard
        master.bind("<Return>", lambda event: self.handle_click("=", "equal"))
        master.bind("<KP_Enter>", lambda event: self.handle_click("=", "equal"))
        master.bind("<BackSpace>", lambda event: self.handle_clear(event, key="\x08"))
        master.bind("<Delete>", lambda event: self.handle_clear(event, key="\x7f"))

    # Hàm xử lý khi nhấn nút bấm hoặc phím Enter:
    def handle_click(self, key, enter_type=None):
        if key == "C":  # xóa toàn bộ khi nhấn Clear
            self.screen.delete(0, tk.END)
        elif key == "Del":  # xóa 1 ký tự khi nhấn Delete
            current_text = self.screen.get()
            if current_text:
                self.screen.delete(len(current_text) - 1)
        elif key == "%":  # chuyển đổi % sang phần trăm
            try:
                result = float(self.screen.get()) / 100
                self.screen.delete(0, tk.END)
                self.screen.insert(0, str(result))
            except:
                self.screen.delete(0, tk.END)
                self.screen.insert(0, "Error")
        elif key == "√":  # tính căn bậc 2
            try:
                result = float(self.screen.get()) ** 0.5
                self.screen.delete(0, tk.END)
                self.screen.insert(0, str(result))
            except:
                self.screen.delete(0, tk.END)
                self.screen.insert(0, "Error")
        elif key == "=" or enter_type == "equal":  # tính toán kết quả
            try:
                result = eval(self.screen.get())
                self.screen.delete(0, tk.END)
                self.screen.insert(0, str(result))
            except:
                self.screen.delete(0, tk.END)
                self.screen.insert(0, "Error")
        else:
            # add key to screen
            self.screen.insert(tk.END, key)

    def handle_clear(self, event=None, key=None):
        if key in ("\x08", "\x7f"):  # xóa khi nhấn Backspace hoặc Delete
            current_text = self.screen.get()
            if current_text:
                self.screen.delete(len(current_text) - 1)
        else:
            self.screen.delete(0, tk.END)  # xóa toàn bộ khi nhấn Clear


root = tk.Tk()
calc = Calculator(root)
root.mainloop()

import tkinter as tk
from tkinter import filedialog

# Hàm lưu file
def save_file(event = None):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text.get('1.0', 'end'))

# Hàm mở file
def open_file(event = None):
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            text.delete('1.0', 'end')
            text.insert('1.0', file.read())

# Hàm xử lý sự kiện khi đóng cửa sổ
def on_closing():
    if tk.messagebox.askyesnocancel("Quit", "Do you want to save the changes?"):
        save_file()
        root.destroy()
    else:
        root.destroy()

root = tk.Tk() # Tạo cửa sổ chính
root.title("Text Editor") # Đặt tiêu đề cho cửa sổ chính

menu = tk.Menu(root) # Tạo menu
file_menu = tk.Menu(menu, tearoff=0) # Tạo menu File
file_menu.add_command(label="Open", command=open_file, accelerator="Ctrl+O") # Thêm nút Open vào menu File
file_menu.add_command(label="Save", command=save_file,  accelerator="Ctrl+S") # Thêm nút Save vào menu File
menu.add_cascade(label="File", menu=file_menu) # Thêm menu File vào menu chính

text = tk.Text(root, bg="black", fg="#00ff00", insertbackground="green") # Tạo text box
text.pack(expand=True, fill='both') # Đặt text box vào cửa sổ chính
text.config(font=("Roboto", 12))  # Đặt font cho text box

root.config(menu=menu) # Đặt menu vào cửa sổ chính

# Đăng ký sự kiện cho phím tắt Ctrl+S và Ctrl+O
root.bind("<Control-s>", save_file)
root.bind("<Control-S>", save_file)
root.bind("<Control-o>", open_file)
root.bind("<Control-O>", open_file)

# Đăng ký sự kiện khi đóng cửa sổ
root.protocol("WM_DELETE_WINDOW", on_closing)

# Chạy cửa sổ chính
root.mainloop()
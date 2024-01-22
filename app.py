import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

def on_button_click():
    label.config(text="Hello, " + entry.get())

# 创建窗口
root = tk.Tk()
root.title("简单程序")

# 创建样式
style = Style(theme="minty")

# 创建框架
frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# 创建输入框和按钮
entry = ttk.Entry(frame, width=15)
entry.grid(row=0, column=0, padx=5, pady=5)
button = ttk.Button(frame, text="点击我", command=on_button_click)
button.grid(row=0, column=1, padx=5, pady=5)

# 创建标签
label = ttk.Label(frame, text="")
label.grid(row=1, column=0, columnspan=2)

# 运行程序
root.mainloop()

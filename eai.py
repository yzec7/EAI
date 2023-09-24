import tkinter as tk
from tkinter import ttk
import webbrowser

def open_website():
    url = "https://eai.art.blog/"
    webbrowser.open_new(url)

# 创建主窗口
root = tk.Tk()
root.title("嵌入网页示例")

# 创建按钮
button = ttk.Button(root, text="打开网页", command=open_website)
button.pack(pady=10)

# 创建嵌入网页的Frame
frame = ttk.Frame(root)
frame.pack()

# 创建WebView
webview = tk.Label(frame, text="Loading...", width=50, height=20)
webview.pack()

# 启动Tkinter事件循环
root.mainloop()

import tkinter as tk
import subprocess
import os
import time

URL = "file://" + os.path.abspath("index.html")

def kill_firefox_tabs():
    subprocess.run(["wmctrl", "-c", "Firefox"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def open_kiosk():
    kill_firefox_tabs()
    time.sleep(0.5)

    subprocess.Popen([
        "firefox",
        "--kiosk",
        URL,
        "--new-instance"
    ])

def on_click(event=None):
    open_kiosk()

root = tk.Tk()
root.overrideredirect(True)
root.attributes("-topmost", True)
root.config(bg="black")


screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()

size = 50
x = (screen_w // 2) - (size // 2)
y = screen_h - size - 20

root.geometry(f"{size}x{size}+{x}+{y}")

canvas = tk.Canvas(root, width=size, height=size, bg="black", highlightthickness=0)
canvas.pack()

circle = canvas.create_oval(5,5,size-5,size-5, fill="#00cc66", outline="")

canvas.tag_bind(circle, "<Button-1>", on_click)


def hover(e):
    canvas.itemconfig(circle, fill="#00ff88")
def leave(e):
    canvas.itemconfig(circle, fill="#00cc66")

canvas.tag_bind(circle, "<Enter>", hover)
canvas.tag_bind(circle, "<Leave>", leave)

root.mainloop()

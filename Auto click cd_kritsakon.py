import time
import threading
import tkinter as tk
from tkinter import ttk
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

# -----------------------------
# 🖱️ ตัวแปรหลัก
clicking = False
mouse = Controller()
TOGGLE_KEY = KeyCode(char="x")  # ปุ่ม toggle
click_speed = 0.01  # ความเร็วเริ่มต้น

# -----------------------------
# ⚙️ ฟังก์ชันการคลิก
def clicker():
    global clicking
    while True:
        if clicking:
            mouse.click(Button.left, 1)
            time.sleep(click_speed)
        else:
            time.sleep(0.05)

# -----------------------------
# 🧠 ฟังก์ชัน toggle (เปิด/ปิดคลิก)
def toggle_event(key):
    global clicking
    if key == TOGGLE_KEY:
        clicking = not clicking
        status_label.config(text=f"Status: {'ON' if clicking else 'OFF'}", fg=("green" if clicking else "red"))

# -----------------------------
# 🪟 สร้าง GUI
root = tk.Tk()
root.title("Auto Clicker by kritsakon")
root.geometry("350x260")
root.resizable(False, False)

# -----------------------------
# 🧩 ส่วนแสดงผลใน GUI
title = tk.Label(root, text="⚡ AUTO CLICKER ⚡", font=("Segoe UI", 14, "bold"))
title.pack(pady=10)

status_label = tk.Label(root, text="Status: OFF", fg="red", font=("Segoe UI", 12, "bold"))
status_label.pack(pady=5)

speed_label = tk.Label(root, text="Click Speed (seconds):", font=("Segoe UI", 10))
speed_label.pack()

speed_var = tk.DoubleVar(value=click_speed)
speed_slider = ttk.Scale(root, from_=0.001, to=0.1, value=click_speed, orient="horizontal", variable=speed_var)
speed_slider.pack(fill="x", padx=40, pady=5)

# -----------------------------
# 🔘 ปุ่มควบคุม
def start_click():
    global clicking
    clicking = True
    status_label.config(text="Status: ON", fg="green")

def stop_click():
    global clicking
    clicking = False
    status_label.config(text="Status: OFF", fg="red")

def apply_speed():
    global click_speed
    click_speed = float(speed_var.get())

start_btn = ttk.Button(root, text="Start (ON)", command=start_click)
start_btn.pack(pady=5)

stop_btn = ttk.Button(root, text="Stop (OFF)", command=stop_click)
stop_btn.pack(pady=5)

apply_btn = ttk.Button(root, text="Apply Speed", command=apply_speed)
apply_btn.pack(pady=5)

info = tk.Label(root, text="Press 'X' to toggle ON/OFF\nAdjust speed as needed", font=("Segoe UI", 9))
info.pack(pady=10)

# -----------------------------
# 🔁 Thread จัดการคลิก
click_thread = threading.Thread(target=clicker, daemon=True)
click_thread.start()

# -----------------------------
# 🎧 Keyboard Listener
listener = Listener(on_press=toggle_event)
listener.start()

root.mainloop()

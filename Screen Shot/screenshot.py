import pyautogui
import tkinter as tk
from tkinter.filedialog import *

root = tk.Tk()
window = tk.Canvas(root, width=200, height=200)
window.pack()


def take_screenshot():
    screen_shot = pyautogui.screenshot()
    path_save = asksaveasfilename()
    screen_shot.save(path_save+"_screenshot.png")

screenshot_button = tk.Button(text="Screenshot", command=take_screenshot, font=16)
window.create_window(100,100,window=screenshot_button)

root.mainloop()

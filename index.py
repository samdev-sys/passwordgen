import time
import pyautogui
import tkinter as tk


def screenshot():

    img =pyautogui.screenshot()
    img.save('test.png')
    img.show()
    print("Captura guardada como 'test.png'")


root = tk.Tk()
frame =tk.Frame(root)
frame.pack()

button =tk.Button(
    frame,
    text="Take a ScreenShot",
    command= screenshot)

button.pack(side=tk.LEFT)
close =tk.Button(
    frame,
    text="Quit",
    command=quit
)
close.pack(side=tk.LEFT)
root.mainloop()
import webbrowser as wb
import tkinter as tk
from tkinter import messagebox

def Webauto():

    chrome_path='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
    URLS=(

        "web.telegram.org",
        "https://console.anthropic.com/login",
        "www.workana.com"
    )
    url=tk.StringVar()


    wb.register('chrome',None,wb.BackgroundBrowser(chrome_path))

    for url in URLS:
        print("opening: "+ url)
        wb.get('chrome').open(url)

Webauto()


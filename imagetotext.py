import pytesseract
import os
from PIL import Image
import tkinter as tk
from tkinter import filedialog,messagebox

pytesseract.pytesseract.tesseract_cmd =r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def convertir():
    
    file_path=filedialog.askopenfilename(
    title="selecciona una imagen",
    filetypes=[("Archivos de imagen", "*.png *.jpg *.jpeg *.bmp *.tiff")]
    )
    if not file_path:
        return
    
    try:
        img=Image.open(file_path)
        text=pytesseract.image_to_string(img, lang="spa")
        result_label.config(text=text) 
    except Exception as e:
        messagebox.showerror("Error",f"No se pudo procesar al imagen:{e}")



root = tk.Tk()
root.title("Convertidor de imagen a Texto")

frame=tk.Frame(root)
frame.pack(pady=10)



btn_convertir = tk.Button(frame, text="Seleccionar imagen y extraer texto", command=convertir)
btn_convertir.pack(side=tk.LEFT, padx=5)

btn_salir = tk.Button(frame, text="Salir", command=root.quit)
btn_salir.pack(side=tk.LEFT)

result_label = tk.Label(root, text="", wraplength=400, justify="left")
result_label.pack(pady=10)

root.mainloop()


# def convertir():
# #     img=Image.open('images.jpg')
# #     text=pytesseract.image_to_string(img)
# #     print(text)

# # convertir()
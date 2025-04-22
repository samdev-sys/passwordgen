import string
import random
import tkinter as tk


def gen():
    s1 =string.ascii_uppercase
    
    s2 =string.ascii_lowercase
    
    s3 =string.digits
    
    s4=string.punctuation

    passlen=int(entry.get())

    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
   

    random.shuffle(s)
    pas=("".join(s[0:passlen]))
    result_label.config(text=f"Contraseña:{pas}")

root = tk.Tk()
root.title("Generador de contraseñas")

frame=tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="longitud :").pack(side=tk.LEFT)
entry =tk.Entry(frame,width =5)
entry.pack(side=tk.LEFT)

button = tk.Button(frame, text="Generar", command=gen)
button.pack(side=tk.LEFT, padx=5)

close = tk.Button(frame, text="Salir", command=root.quit)
close.pack(side=tk.LEFT)

result_label = tk.Label(root, text="Contraseña: ")
result_label.pack(pady=10)

root.mainloop()
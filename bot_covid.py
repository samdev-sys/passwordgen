import requests
from win10toast import ToastNotifier
import urllib.parse  # para codificar la URL
import time
import tkinter as tk
from tkinter import messagebox

def update():
    site_url = entry.get()

    if not site_url.strip():
        messagebox.showwarning("Advertencia", "Por favor, ingresa una URL.")
        return

    # Codificamos la URL para que sea válida en la API
    encoded_url = urllib.parse.quote(site_url)

    try:
        while True:
            # Hacemos la petición con la URL codificada
            r = requests.get(f'https://api.websitecarbon.com/site?url={encoded_url}')
            data = r.json()

            # Armamos el texto del mensaje
            text = (
                f"Sitio: {data['url']}\n"
                f"Tamaño de carga: {data['bytes']} bytes\n"
                f"Energía consumida: {data['statistics']['energy']:.10f} kWh\n"
                f"Rating: {data['rating']}"
            )

            # Mostramos notificación
            toast = ToastNotifier()
            toast.show_toast("🌿 Huella de Carbono del Sitio", text, duration=20)

            # Esperamos 1 minuto antes de repetir
            time.sleep(60)

    except Exception as e:
     messagebox.showerror(f"Error al obtener los datos: {e}")

root = tk.Tk()
root.title("Analizador de Sitios Web (Huella de Carbono)")
root.geometry("400x150")
root.resizable(False, False)

label = tk.Label(root, text="Ingresa la URL del sitio web:", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

btn = tk.Button(root, text="Analizar", command=update, bg="#4CAF50", fg="white")
btn.pack(pady=10)

root.mainloop()
# import requests
# import re

# def obtener_direccion_m3u8(url):
#     # Realiza una solicitud HTTP GET a la URL proporcionada
#     response = requests.get(url)
#     # Busca la dirección m3u8 en el contenido de la página usando expresiones regulares
#     pattern = r'(https?://[^\s]+\.m3u8)'
#     match = re.search(pattern, response.text)
    
#     if match:
#         return match.group(0)
#     else:
#         return None

# url_pagina_web = input('Ingrese la URL del video ')

# # Obtén la dirección m3u8 del video
# direccion_m3u8 = obtener_direccion_m3u8(url_pagina_web)

# if direccion_m3u8:
#     print('Dirección m3u8 del video:', direccion_m3u8)
# else:
#     print('No se encontró la dirección m3u8 del video.')

# import requests
# import re
# import threading
# import tkinter as tk
# from tkinter import messagebox
# from tkinter import ttk
# import pyperclip

# def obtener_direccion_m3u8(url):
#     response = requests.get(url)
#     pattern = r'(https?://[^\s]+\.m3u8)'
#     match = re.search(pattern, response.text)
#     if match:
#         return match.group(0)
#     else:
#         return None

# def buscar_direccion():
#     url = entry_url.get()
#     if not url:
#         messagebox.showerror('Error', 'Por favor ingrese una URL válida.')
#         return

#     progress_bar.start()

#     # Crear un hilo aparte para realizar la búsqueda
#     threading.Thread(target=lambda: buscar_en_hilo(url)).start()

# def buscar_en_hilo(url):
#     direccion_m3u8 = obtener_direccion_m3u8(url)

#     # Actualizar la interfaz gráfica desde el hilo principal
#     window.after(0, lambda: mostrar_resultado(direccion_m3u8))

# def mostrar_resultado(direccion_m3u8):
#     progress_bar.stop()

#     if direccion_m3u8:
#         label_direccion['text'] = f'Dirección m3u8 del video:\n{direccion_m3u8}'
#     else:
#         label_direccion['text'] = 'No se encontró la dirección m3u8 del video.'

# def copiar_portapapeles():
#     direccion_m3u8 = label_direccion['text'].split('\n')[1]
#     pyperclip.copy(direccion_m3u8)
#     messagebox.showinfo('Copiado', 'Dirección m3u8 copiada al portapapeles.')

# # Crear la ventana principal
# window = tk.Tk()
# window.title('Obtener dirección m3u8')
# window.geometry('400x200')

# # Crear etiqueta y entrada de texto para la URL
# label_url = tk.Label(window, text='URL de la página web:')
# label_url.pack()
# entry_url = tk.Entry(window, width=50)
# entry_url.pack()

# # Crear botón para buscar la dirección m3u8
# btn_buscar = tk.Button(window, text='Buscar dirección m3u8', command=buscar_direccion)
# btn_buscar.pack()

# # Crear ProgressBar indefinido
# progress_bar = ttk.Progressbar(window, mode='indeterminate')
# progress_bar.pack()

# # Crear etiqueta para mostrar la dirección m3u8
# label_direccion = tk.Label(window, text='')
# label_direccion.pack()

# # Crear botón para copiar al portapapeles
# btn_copiar = tk.Button(window, text='Copiar al portapapeles', command=copiar_portapapeles)
# btn_copiar.pack()

# # Iniciar el bucle principal de la interfaz
# window.mainloop()


import requests
import re
import threading
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pyperclip

def obtener_direccion_m3u8(url):
    response = requests.get(url)
    pattern = r'(https?://[^\s]+\.m3u8)'
    match = re.search(pattern, response.text)
    if match:
        return match.group(0)
    else:
        return None

def buscar_direccion():
    url = entry_url.get()
    if not url:
        messagebox.showerror('Error', 'Por favor ingrese una URL válida.')
        return

    progress_bar.start(10)  # Velocidad de movimiento del ProgressBar

    # Crear un hilo aparte para realizar la búsqueda
    threading.Thread(target=lambda: buscar_en_hilo(url)).start()

def buscar_en_hilo(url):
    direccion_m3u8 = obtener_direccion_m3u8(url)

    # Actualizar la interfaz gráfica desde el hilo principal
    window.after(0, lambda: mostrar_resultado(direccion_m3u8))

def mostrar_resultado(direccion_m3u8):
    progress_bar.stop()

    if direccion_m3u8:
        label_direccion['text'] = f'Dirección m3u8 del video:\n{direccion_m3u8}'
    else:
        label_direccion['text'] = 'No se encontró la dirección m3u8 del video.'

def copiar_portapapeles():
    direccion_m3u8 = label_direccion['text'].split('\n')[1]
    pyperclip.copy(direccion_m3u8)
    messagebox.showinfo('Copiado', 'Dirección m3u8 copiada al portapapeles.')

# Crear la ventana principal
window = tk.Tk()
window.title('Obtener dirección m3u8')
window.geometry('400x200')
window.configure(bg='black')
# Crear etiqueta y entrada de texto para la URL
label_url = tk.Label(window, text='URL de la página web:')
label_url.pack()
label_url.configure(bg='black',fg='white')
entry_url = tk.Entry(window, width=50)
entry_url.configure(bg='grey',fg='white')
entry_url.pack()

# Crear botón para buscar la dirección m3u8

s = ttk.Style()
s.configure("Search.TButton", foreground="grey",background="#42413f")
s.map("Search.TButton", foreground=[("active", "cyan")],background=[("pressed", "#525151")])
# boton = ttk.Button(text="¡Hola, mundo!", style="Search.TButton")

btn_buscar = ttk.Button(window, text='Buscar dirección m3u8', style="Search.TButton",command=buscar_direccion)
# btn_buscar.configure(bg='grey',fg='white')
btn_buscar.pack()

# Crear ProgressBar indefinido
progress_bar = ttk.Progressbar(window, mode='indeterminate', length=300)
progress_bar.pack()

# Crear etiqueta para mostrar la dirección m3u8
label_direccion = tk.Label(window, text='', justify='left', wraplength=380)
label_direccion.configure(bg ='grey',fg ='white')
label_direccion.pack()

# Crear botón para copiar al portapapeles
btn_copiar = ttk.Button(window, text='Copiar al portapapeles', command=copiar_portapapeles, style="Search.TButton")
btn_copiar.pack()

# Iniciar el bucle principal de la interfaz
window.mainloop()

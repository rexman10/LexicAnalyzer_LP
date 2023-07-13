import tkinter as tk
import lexico
import sintactico
import os
from tkinter import filedialog


def analizar_sintactico():
    contenido_texto = espacioTexto.get("1.0", tk.END)  # Obtener el contenido

    result = sintactico.analizar_sintactico_string(contenido_texto)  # Realizar el análisis sintáctico con el contenido

    if result:
        mensaje = "Análisis sintáctico exitoso"
    else:
        mensaje = "Error de sintaxis"

    espacioTextoSupDer.delete("1.0", tk.END)
    espacioTextoSupDer.insert(tk.END, mensaje)

def analizar_lexico():
    contenido_texto = espacioTexto.get("1.0", tk.END)  # Obtener el contenido
    numero_linea_inicial = lexico.obtener_numero_linea()
    result = lexico.analyze_lexical_string(contenido_texto, numero_linea_inicial)  # Realizar el análisis léxico con el contenido

    print(result)

    espacioTextoSupIzq.delete("1.0", tk.END)
    for token in result:
        linea = str(token.lineno) + ": " + str(token.value) + " - " + str(token.type)
        print(linea)
        espacioTextoSupIzq.insert(tk.END, linea + "\n")

# Función para cargar y mostrar el contenido del archivo de texto

def cargar_contenido():
    lexico.reseteo_numero_linea()
    global contenido_archivo

    archivo = filedialog.askopenfilename(initialdir=os.path.dirname(__file__), title="Seleccionar archivo",
                                         filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")))
    if archivo:
        with open(archivo, "r") as f:
            contenido_archivo = f.read()

        espacioTexto.delete("1.0", tk.END)  # Limpiar el contenido existente en el widget
        espacioTexto.insert(tk.END, contenido_archivo)  # Insertar el contenido del archivo en el widget
        print(contenido_archivo)

def limpiar_contenido():
    espacioTexto.delete("1.0", tk.END)
    espacioTextoSupIzq.delete("1.0", tk.END)
    espacioTextoSupDer.delete("1.0", tk.END)
    espacioTextoInf.delete("1.0", tk.END)

#ventana principal
ventana = tk.Tk()
ventana.geometry("1200x800")

contenedorIzq = tk.Frame(ventana, bg="red")
contenedorIzq.pack(side="left", fill="both", expand=True)

ancho_ventana = ventana.winfo_width()
alto_ventana = ventana.winfo_height()

ancho_espacio = ancho_ventana // 2
alto_espacio = alto_ventana

contenedorTexto = tk.Frame(contenedorIzq, padx=20, pady=20)
contenedorTexto.pack(fill="both", expand=True)

espacioTexto = tk.Text(contenedorTexto, bg="black", fg="white", width=ancho_espacio, height=alto_espacio)
espacioTexto.pack(fill="both", expand=True)

contenedorBotones = tk.Frame(contenedorIzq, padx=20)
contenedorBotones.pack()

boton1 = tk.Button(contenedorBotones, text="Subir", padx=10, command=cargar_contenido)
boton1.pack(side="left", padx=(0, 10))

boton2 = tk.Button(contenedorBotones, text="Limpiar", padx=10, command=limpiar_contenido)
boton2.pack(side="left")

contenedorDer = tk.Frame(ventana, bg="blue")
contenedorDer.pack(side="right", fill="both", expand=True)

contenedorDerSup = tk.Frame(contenedorDer, bg="green")
contenedorDerSup.pack(side="top", fill="both", expand=True)

contenedorDerInf = tk.Frame(contenedorDer, bg="yellow")
contenedorDerInf.pack(side="bottom", fill="both", expand=True)

contenedorTextoInf = tk.Frame(contenedorDerInf, padx=20, pady=20)
contenedorTextoInf.pack(fill="both", expand=True)

espacioTextoInf = tk.Text(contenedorTextoInf, bg="black", fg="white", width=ancho_espacio, height=alto_espacio)
espacioTextoInf.pack(fill="both", expand=True)

contenedorDerSupDer = tk.Frame(contenedorDerSup, bg="purple")
contenedorDerSupDer.pack(side="right", fill="both", expand=True)

contenedorTextoSupDer = tk.Frame(contenedorDerSupDer, padx=20, pady=20)
contenedorTextoSupDer.pack(fill="both", expand=True)

espacioTextoSupDer = tk.Text(contenedorTextoSupDer, bg="black", fg="white", width=ancho_espacio, height=alto_espacio)
espacioTextoSupDer.pack(fill="both", expand=True)

contenedorDerSupIzq = tk.Frame(contenedorDerSup, bg="orange")
contenedorDerSupIzq.pack(side="left", fill="both", expand=True)

contenedorTextoSupIzq = tk.Frame(contenedorDerSupIzq, padx=20, pady=20)
contenedorTextoSupIzq.pack(fill="both", expand=True)

espacioTextoSupIzq = tk.Text(contenedorTextoSupIzq, bg="black", fg="white", width=ancho_espacio, height=alto_espacio)
espacioTextoSupIzq.pack(fill="both", expand=True)

boton = tk.Button(contenedorDerSupDer, text="Sintactico", command=analizar_sintactico)
boton.pack(side="bottom")

boton = tk.Button(contenedorDerSupIzq, text="Lexico", command=analizar_lexico)
boton.pack(side="bottom")

boton = tk.Button(contenedorDerInf, text="Semantico")
boton.pack(side="bottom")

ventana.mainloop()

import tkinter as tk
import lexico
import sintactico2
import os
from tkinter import filedialog



def analizar_sintactico():
    contenido_texto = espacioTexto.get("1.0", tk.END)

    sintactico2.analizar_sintactico(contenido_texto)
    errores = sintactico2.mensajes_error
    sintactico2.resetear_errores()

    if len(errores) > 0:
        mensaje = "\n".join(errores)
    else:
        mensaje = "Análisis sintáctico exitoso"

    espacioTextoDerInf.delete("1.0", tk.END)
    espacioTextoDerInf.insert(tk.END, mensaje)

def analizar_lexico():
    contenido_texto = espacioTexto.get("1.0", tk.END)
    lexico.resetear_numero_linea()
    numero_linea_inicial = lexico.obtener_numero_linea()
    result = lexico.analyze_lexical_string(contenido_texto, numero_linea_inicial)

    print(result)

    espacioTextoDerSup.delete("1.0", tk.END)
    for token in result:
        linea = str(token.lineno) + ": " + str(token.value) + " - " + str(token.type)
        print(linea)
        espacioTextoDerSup.insert(tk.END, linea + "\n")


def cargar_contenido():

    global contenido_archivo

    archivo = filedialog.askopenfilename(initialdir=os.path.dirname(__file__), title="Seleccionar archivo",
                                         filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")))
    if archivo:
        with open(archivo, "r") as f:
            contenido_archivo = f.read()

        sintactico2.resetear_linea()  # Reinicia el conteo de línea
        espacioTexto.delete("1.0", tk.END)
        espacioTexto.insert(tk.END, contenido_archivo)
        print(contenido_archivo)


def limpiar_contenido():
    espacioTexto.delete("1.0", tk.END)
    espacioTextoDerSup.delete("1.0", tk.END)
    espacioTextoDerInf.delete("1.0", tk.END)

#ventana principal
ventana = tk.Tk()
ventana.geometry("1200x800")
ventana.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
ventana.grid_rowconfigure(0, weight=1)

ancho_ventana = ventana.winfo_width()
alto_ventana = ventana.winfo_height()

contenedorIzq = tk.Frame(ventana)
contenedorIzq.grid(row=0, column=0, columnspan=2, sticky="nsew")

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
contenedorDer.grid(row=0, column=2, columnspan=3, sticky="nsew")

#Contenedores mitad derecho
contenedorDerSup = tk.Frame(contenedorDer)
contenedorDerSup.pack(side="top", fill="both", expand=True)

contenedorDerInf = tk.Frame(contenedorDer)
contenedorDerInf.pack(side="bottom", fill="both", expand=True)

contenedorTextoDerSup = tk.Frame(contenedorDerSup, padx=20, pady=20)
contenedorTextoDerSup.pack(fill="both", expand=True)

contenedorTextoDerInf = tk.Frame(contenedorDerInf, padx=20, pady=20)
contenedorTextoDerInf.pack(fill="both", expand=True)

espacioTextoDerSup = tk.Text(contenedorTextoDerSup, bg="black", fg="white", width=ancho_espacio, height=alto_espacio)
espacioTextoDerSup.pack(fill="both", expand=True)

espacioTextoDerInf = tk.Text(contenedorTextoDerInf, bg="black", fg="white", width=ancho_espacio, height=alto_espacio)
espacioTextoDerInf.pack(fill="both", expand=True)

boton = tk.Button(contenedorDerInf, text="Sintactico", command=analizar_sintactico)
boton.pack(side="bottom")

boton = tk.Button(contenedorDerSup, text="Lexico", command=analizar_lexico)
boton.pack(side="bottom")

ventana.mainloop()
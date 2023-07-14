import tkinter as tk
import lexico
import sintactico
import os
from tkinter import filedialog



def analizar_sintactico():
    contenido_texto = espacioTexto.get("1.0", tk.END)
    result = sintactico.analizar_sintactico_string(contenido_texto)

    if result is not None:
        mensaje = "Análisis sintáctico exitoso"
    else:
        mensaje = sintactico.p_error_message

    espacioTextoDerDer.delete("1.0", tk.END)
    espacioTextoDerDer.insert(tk.END, mensaje)

def analizar_lexico():
    contenido_texto = espacioTexto.get("1.0", tk.END)
    numero_linea_inicial = lexico.obtener_numero_linea()
    result = lexico.analyze_lexical_string(contenido_texto, numero_linea_inicial)

    print(result)

    espacioTextoDerIzq.delete("1.0", tk.END)
    for token in result:
        linea = str(token.lineno) + ": " + str(token.value) + " - " + str(token.type)
        print(linea)
        espacioTextoDerIzq.insert(tk.END, linea + "\n")


def cargar_contenido():
    lexico.reseteo_numero_linea()
    global contenido_archivo

    archivo = filedialog.askopenfilename(initialdir=os.path.dirname(__file__), title="Seleccionar archivo",
                                         filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")))
    if archivo:
        with open(archivo, "r") as f:
            contenido_archivo = f.read()

        espacioTexto.delete("1.0", tk.END)
        espacioTexto.insert(tk.END, contenido_archivo)
        print(contenido_archivo)

def limpiar_contenido():
    espacioTexto.delete("1.0", tk.END)
    espacioTextoDerIzq.delete("1.0", tk.END)
    espacioTextoDerDer.delete("1.0", tk.END)

#ventana principal
ventana = tk.Tk()
ventana.geometry("1200x800")

contenedorIzq = tk.Frame(ventana)
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

#Contenedores mitad derecho
contenedorDerIzq = tk.Frame(contenedorDer)
contenedorDerIzq.pack(side="left", fill="both", expand=True)

contenedorDerDer = tk.Frame(contenedorDer)
contenedorDerDer.pack(side="right", fill="both", expand=True)

contenedorTextoDerIzq = tk.Frame(contenedorDerIzq, padx=20, pady=20)
contenedorTextoDerIzq.pack(fill="both", expand=True)

contenedorTextoDerDer = tk.Frame(contenedorDerDer, padx=20, pady=20)
contenedorTextoDerDer.pack(fill="both", expand=True)

espacioTextoDerIzq = tk.Text(contenedorTextoDerIzq, bg="black", fg="white", width=ancho_espacio, height=alto_espacio)
espacioTextoDerIzq.pack(fill="both", expand=True)

espacioTextoDerDer = tk.Text(contenedorTextoDerDer, bg="black", fg="white", width=ancho_espacio, height=alto_espacio)
espacioTextoDerDer.pack(fill="both", expand=True)

boton = tk.Button(contenedorDerDer, text="Sintactico", command=analizar_sintactico)
boton.pack(side="bottom")

boton = tk.Button(contenedorDerIzq, text="Lexico", command=analizar_lexico)
boton.pack(side="bottom")

ventana.mainloop()
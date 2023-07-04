import tkinter as tk
import lexico
import sintactico
import os

def analizar_sintactico():
    file_path = os.path.join(os.path.dirname(__file__), "algoritmo3.txt")  # Ruta del archivo de texto
    sintactico.analizar_sintactico(file_path)  # Llamar a la función de análisis sintáctico
def analizar_lexico():
    file_path = os.path.join(os.path.dirname(__file__), "algoritmo3.txt")  # Ruta del archivo de texto
    result = lexico.analyze_lexical(file_path)  # Realizar el análisis léxico

    espacioTextoSupIzq.delete(1.0, tk.END)  # Borrar el contenido existente
    for token in result:
        linea = str(token.lineno) + ": " + str(token.value) + " - " + str(token.type)
        print(linea)
        espacioTextoSupIzq.insert(tk.END, linea + "\n")

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

boton1 = tk.Button(contenedorBotones, text="Subir", padx=10)
boton1.pack(side="left", padx=(0, 10))

boton2 = tk.Button(contenedorBotones, text="Limpiar", padx=10)
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

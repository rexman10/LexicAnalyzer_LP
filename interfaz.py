import tkinter as tk
import lexico
import os

def analizar_lexico():
    file_path = os.path.join(os.path.dirname(__file__), "algoritmo3.txt")  # Ruta del archivo de texto
    result = lexico.analyze_lexical(file_path)  # Realizar el análisis léxico

    resultado_lexico.delete(1.0, tk.END)  # Borrar el contenido existente en el widget de texto
    for token in result:
        linea = str(token.lineno) + ": " + str(token.value) + " - " + str(token.type)
        print(linea)
        resultado_lexico.insert(tk.END, linea + "\n")

ventana = tk.Tk()
ventana.configure(bg="blue")
ventana.geometry("1000x800")

ventana.rowconfigure(0, weight=1)
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)

ventana.resizable(1, 1)

# Contenedor Izquierdo de la ventana que servirá para los INPUTS
contenedorIzq = tk.Frame(ventana)
contenedorIzq.grid(row=0, column=0, sticky="nswe")
contenedorIzq.configure(padx=20, pady=20)

cuadroIzqInput = tk.Frame(contenedorIzq, bg="black")
cuadroIzqInput.pack(fill="both", expand=True)

# Espacio para insertar texto en el contenedor cuadroIzqInput
labelIzqInput = tk.Label(cuadroIzqInput, text="Texto de ejemplo")
labelIzqInput.pack()

# Botón dentro de contenedorIzq
botonIzqUpload = tk.Button(contenedorIzq, text="Subir Archivo")
botonIzqUpload.pack(pady=10)

# Botón dentro de contenedorIzq
botonIzqClean = tk.Button(contenedorIzq, text="Limpiar")
botonIzqClean.pack(pady=10)

# Contenedor derecho de la ventana
contenedorDer = tk.Frame(ventana)
contenedorDer.grid(row=0, column=1, sticky="nswe")
contenedorDer.configure(padx=10, pady=10)

contenedorDer.grid_rowconfigure(0, weight=1)
contenedorDer.grid_rowconfigure(1, weight=1)
contenedorDer.grid_columnconfigure(0, weight=1)

# Contenedor que será para la parte léxica y sintáctica
contenedorDerSup = tk.Frame(contenedorDer)
contenedorDerSup.grid(row=0, column=0, sticky="nswe")
contenedorDerSup.configure(padx=10, pady=10)

contenedorDerSup.grid_rowconfigure(0, weight=1)
contenedorDerSup.grid_columnconfigure(0, weight=1)
contenedorDerSup.grid_columnconfigure(1, weight=1)
contenedorDerSup.grid_columnconfigure(2, weight=1)

# Contenedor que será para la parte sintáctica
contenedorDerSupIzq = tk.Frame(contenedorDerSup)
contenedorDerSupIzq.grid(row=0, column=0, sticky="nswe")

# Contenedor negro dentro de contenedorDerSupIzq
contenedorNegroDerSupIzq = tk.Frame(contenedorDerSupIzq, bg="black")
contenedorNegroDerSupIzq.pack(fill="both", expand=True)

# Espacio para insertar texto en el contenedor contenedorNegroDerSupIzq
resultado_lexico = tk.Text(contenedorNegroDerSupIzq, bg="black", fg="white")
resultado_lexico.pack(fill="both", expand=True)

# Botón dentro de contenedorDerSupIzq
botonDerSupIzq = tk.Button(contenedorDerSupIzq, text="Lexico", command=analizar_lexico)
botonDerSupIzq.pack(pady=10)

# Separación entre contenedorDerSupIzq y contenedorDerSupDer
separador = tk.Frame(contenedorDerSup, width=2, bg="white")
separador.grid(row=0, column=1, sticky="ns")

# Contenedor que será para la parte léxica
contenedorDerSupDer = tk.Frame(contenedorDerSup)
contenedorDerSupDer.grid(row=0, column=2, sticky="nswe")

# Contenedor negro dentro de contenedorDerSupDer
contenedorNegroDerSupDer = tk.Frame(contenedorDerSupDer, bg="black")
contenedorNegroDerSupDer.pack(fill="both", expand=True)

# Botón dentro de contenedorDerSupDer
botonDerSupDer = tk.Button(contenedorDerSupDer, text="Sintatico")
botonDerSupDer.pack(pady=10)

# Espacio para insertar texto en el contenedor contenedorNegroDerSupDer
labelDerSupDer = tk.Label(contenedorNegroDerSupDer, text="Texto de ejemplo")
labelDerSupDer.pack()

# Contenedor que será para la parte semántica
contenedorDerInf = tk.Frame(contenedorDer)
contenedorDerInf.grid(row=1, column=0, sticky="nswe")
contenedorDerInf.configure(padx=10, pady=10)

cuadroDerInf = tk.Frame(contenedorDerInf, bg="black")
cuadroDerInf.pack(fill="both", expand=True)

# Espacio para insertar texto en el contenedor cuadroDerInf
labelDerInf = tk.Label(cuadroDerInf, text="Texto de ejemplo")
labelDerInf.pack()

# Botón dentro de contenedorDerInf
botonDerInf = tk.Button(contenedorDerInf, text="Semantico")
botonDerInf.pack(pady=10)

# Función para realizar el análisis léxico y actualizar la etiqueta



ventana.mainloop()

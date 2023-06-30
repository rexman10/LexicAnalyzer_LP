import tkinter as tk

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

# Agregar relleno interno y externo al contenedorIzq
contenedorIzq.configure(padx=10, pady=10)

cuadroInput = tk.Frame(contenedorIzq, bg="black")
cuadroInput.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

# Contenedor de contenido dentro de cuadroInput
contenidoInput = tk.Label(cuadroInput, text="Contenido del cuadroInput", fg="white", bg="black")
contenidoInput.pack()


# Contenedor derecho de la ventana
contenedorDer = tk.Frame(ventana)
contenedorDer.grid(row=0, column=1, sticky="nswe")

# Establecer el peso de las filas en el contenedorDer
contenedorDer.grid_rowconfigure(0, weight=1)
contenedorDer.grid_rowconfigure(1, weight=1)

# Contenedor que será para la parte léxica y sintáctica
contenedorDerSup = tk.Frame(contenedorDer)
contenedorDerSup.grid(row=0, column=0, sticky="nswe")

# Establecer el peso de las columnas en el contenedorDerSup
contenedorDerSup.grid_columnconfigure(0, weight=1)
contenedorDerSup.grid_columnconfigure(1, weight=1)

# Contenedor que será para la parte sintáctica
contenedorDerSupIzq = tk.Frame(contenedorDerSup, bg="black")
contenedorDerSupIzq.grid(row=0, column=0, sticky="nswe")

# Contenedor de contenido dentro de contenedorDerSupIzq
contenidoDerSupIzq = tk.Label(contenedorDerSupIzq, text="Contenido del cuadroDerSupIzq", fg="white", bg="black")
contenidoDerSupIzq.pack()

# Contenedor que será para la parte léxica
contenedorDerSupDer = tk.Frame(contenedorDerSup, bg="black")
contenedorDerSupDer.grid(row=0, column=1, sticky="nswe")

# Contenedor de contenido dentro de contenedorDerSupDer
contenidoDerSupDer = tk.Label(contenedorDerSupDer, text="Contenido del cuadroDerSupDer", fg="white", bg="black")
contenidoDerSupDer.pack()

# Contenedor que será para la parte semántica
contenedorDerInf = tk.Frame(contenedorDer)
contenedorDerInf.grid(row=1, column=0, sticky="nswe")

# Agregar relleno interno y externo al contenedorIzq
contenedorDerInf.configure(padx=10, pady=10)

cuadroDerInf = tk.Frame(contenedorDerInf, bg="black")
cuadroDerInf.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

# Contenedor de contenido dentro de cuadroInput
contenidoDerInf = tk.Label(cuadroDerInf, text="Contenido del cuadroDerInf", fg="white", bg="black")
contenidoDerInf.pack()



ventana.mainloop()

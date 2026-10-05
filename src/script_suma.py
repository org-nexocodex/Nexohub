import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        suma = num1 + num2
        resultado_texto = f"Número 1: {num1} + Número 2: {num2} = Suma total: {suma}\n"
        
        with open("resultado.txt", "a") as f:
            f.write(resultado_texto)

        messagebox.showinfo("Resultado", f"¡Suma realizada con éxito!\nSuma total: {suma}")
        ventana.destroy()
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")

ventana = tk.Tk()
ventana.title("Suma Interactiva")
ventana.geometry("300x220")
ventana.eval('tk::PlaceWindow . center')

tk.Label(ventana, text="Ingrese el primer valor:", font=("Arial", 10)).pack(pady=5)
entry1 = tk.Entry(ventana, font=("Arial", 12), justify="center")
entry1.pack(pady=5)
entry1.focus()

tk.Label(ventana, text="Ingrese el segundo valor:", font=("Arial", 10)).pack(pady=5)
entry2 = tk.Entry(ventana, font=("Arial", 12), justify="center")
entry2.pack(pady=5)

btn = tk.Button(ventana, text="Sumar y Guardar", command=calcular, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
btn.pack(pady=15)

ventana.mainloop()
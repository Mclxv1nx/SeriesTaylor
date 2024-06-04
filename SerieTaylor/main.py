import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from math import factorial
from solver import Polinomio
import re

# Crear la ventana principal
root = tk.Tk()
root.title("Series Taylor Solver")
root.geometry("500x400")

# Función que se llama cuando se hace clic en el botón
def Grafico():
    # Obtener la función del Entry
    func_str = entry.get()
    func_str = func_str.replace("^", "**")  # Reemplazar ^ con ** para exponentes
    func_str = re.sub(r'(\d)(x)', r'\1*\2', func_str)  # Insertar * entre número y x

    # Definir la función original a partir del string ingresado
    def f(x):
        try:
            return eval(func_str)
        except Exception as e:
            print(f"Error al evaluar la función: {e}")
            return np.zeros_like(x)  # Devuelve una matriz de ceros si hay un error

    # Definir la serie de Taylor utilizando una lista de coeficientes
    def taylor_series(x, coef_list):
        series = 0
        for n, coef in enumerate(coef_list):
            series += (coef / factorial(n)) * (x - 1) ** n
        return series

    # Crear el rango de valores de x
    x = np.linspace(-3, 3, 400)

    # Aplicar las funciones a x
    y = f(x)

    # Lista de coeficientes para la serie de Taylor
    polinomio = Polinomio(func_str)

    derivadas = [polinomio.Reemplazar(1)]
    derivada = polinomio.Derivar()

    while str(derivada) != '0':
        derivadas.append(derivada.Reemplazar(1))
        derivada = derivada.Derivar()

    taylor_y = taylor_series(x, derivadas)

    # Configurar el gráfico
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f'$y={func_str}$', color='green', linewidth=0.4)
    plt.plot(x, taylor_y, label='Serie de Taylor', color='blue', linestyle='--', linewidth=0.8)

    # Agregar cuadrícula
    plt.grid(True, which='both', linestyle='--', linewidth=0.2)

    # Configurar los ejes
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)

    # Configurar límites y ticks del eje y
    plt.ylim(-10, 30)
    plt.yticks(np.arange(-3, 31, 1))

    # Agregar etiquetas y título
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Gráfico de la función $y={func_str}$ y su Serie de Taylor')
    plt.legend()

    # Mostrar el gráfico
    plt.show()

# Crear una etiqueta
label = tk.Label(root, text="Por: Puentestar Carlos, Hernandez Ángelo, Urresta Adrián")
label.pack(pady=20)
entry = tk.Entry(root)
entry.pack(pady=30)

# Crear un botón
button = tk.Button(root, text="Resolver", command=Grafico)
button.pack(pady=10)

# Iniciar el bucle principal
root.mainloop()





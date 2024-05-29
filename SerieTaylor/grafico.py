import numpy as np
import matplotlib.pyplot as plt

# Definir la función
def f(x):
    return x**4 - 3*x**2 + 1

# Crear el rango de valores de x
x = np.linspace(-3, 3, 400)

# Aplicar la función a x
y = f(x)

# Configurar el gráfico
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='$y=x^4 - 3x^2 + 1$', color='green', linewidth=0.4)

# Agregar cuadrícula
plt.grid(True, which='both', linestyle='--', linewidth=0.2)

# Configurar los ejes
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)

# Configurar límites y ticks del eje y
plt.ylim(-3, 30)
plt.yticks(np.arange(-3, 31, 1))

# Agregar etiquetas y título
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico de la función $y=x^4 - 3x^2 + 1$')
plt.legend()

# Mostrar el gráfico
plt.show()
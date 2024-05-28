import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y, label='y=sin(x)')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico de una función')
plt.legend()

plt.show()
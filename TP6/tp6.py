import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from PIL import Image


def func(x, a, b, c):
    return a * np.exp(-b * x) + c


# question 1

tableau = np.random.randint(2, size=(4, 3, 2))
print("ndim :")
print(np.ndim(tableau))
print("shape :")
print(np.shape(tableau))
print("size :")
print(np.size(tableau))
print("type :")
print(np.result_type(tableau))
print("data :")
print(tableau)

# question 2

tableau = np.arange(9).reshape((3, 3))
tableau2 = np.arange(2, 11).reshape((3, 3))
print("tableau 1 :")
print(tableau)
print("tableau 2 :")
print(tableau2)
print("multiplication :")
print(np.multiply(tableau, tableau2))
print("produit scalaire :")
print(np.dot(tableau, tableau2))
print("transposé :")
print(np.transpose(tableau))

# question 3

tableau = [[2, 2, 1], [1, 3, 1], [6, 2, 1]]
print("tableau :")
print(tableau)
print("determinant :")
print(np.linalg.det(tableau))
print("inverse :")
print(np.linalg.inv(tableau))
print("solution equation :")
print(np.linalg.solve(tableau, np.arange(1, 4)))
print("vecteur propres :")
print(np.linalg.eig(tableau))
print("valeurs propres :")
print(np.linalg.eigvals(tableau))

# question 4

xdata = np.linspace(0, 4, 50)
y = func(xdata, 2.5, 1.3, 0.5)
np.random.seed(1729)
y_noise = 0.2 * np.random.normal(size=xdata.size)
ydata = y + y_noise
plt.plot(xdata, ydata, 'b-', label='data')

popt, pcov = curve_fit(func, xdata, ydata)
plt.plot(xdata, func(xdata, *popt), 'r-', label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))

popt, _ = curve_fit(func, xdata, ydata, bounds=(0, [3., 1., 0.5]))

plt.plot(xdata, func(xdata, *popt), 'g--', label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

# question 5
im = Image.open("raclette.jpg")
im2 = Image.open("raclette.jpg")
im.show()
size = 128, 128
im2.thumbnail(size)
im2.show()
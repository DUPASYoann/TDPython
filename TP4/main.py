from random import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.tri as mtri


def generer_nombre_random(borne_inf=0, borne_sup=100, nombre=10):
    liste = []
    for i in range(nombre):
        liste.append(randint(borne_inf, borne_sup))
    return liste


if __name__ == "__main__":

    # question 1
    _liste = generer_nombre_random()

    # question 2
    plt.plot(generer_nombre_random())
    plt.show()

    # question 3
    plt.plot(generer_nombre_random(), "r--", linewidth=5)
    plt.plot(generer_nombre_random(), "b", linewidth=3)
    plt.plot(generer_nombre_random(), "g", linewidth=10)
    plt.show()

    # question 4
    plt.plot(generer_nombre_random(), "r--", linewidth=5, label="hmmm", marker="+")
    plt.plot(generer_nombre_random(), "b", linewidth=3, label="hmmmmmm")
    plt.plot(generer_nombre_random(), "g", linewidth=7, label="ah")
    plt.title("Ouah un titre")
    plt.xlabel('Ouah un axe x')
    plt.ylabel('Ouah un autre axe y')
    plt.annotate('ne regardez pas là', xy=(7, 80), xytext=(8, 70),
                 arrowprops={'facecolor': 'black', 'shrink': 0.05})
    plt.legend()
    plt.show()

    # question 5

    # # histogramme
    x = generer_nombre_random(nombre=1000)
    n, bins, patches = plt.hist(x, 50, density=1, facecolor='b', alpha=0.5)

    plt.xlabel('Mise')
    plt.ylabel(u'Probabilité')
    plt.axis([0, 100, 0, 0.03])
    plt.grid(True)
    plt.show()

    # # camembert
    name = ['-18', '18-25', '25-50', '50+']
    data = [5000, 26000, 21400, 12000]

    explode = (0, 0.15, 0, 0)
    plt.pie(data, explode=explode, labels=name, autopct='%1.1f%%', startangle=90, shadow=True)
    plt.axis('equal')
    plt.show()

    # question 6
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # # données
    u = np.linspace(0, 2.0 * np.pi, endpoint=True, num=50)
    v = np.linspace(-0.5, 0.5, endpoint=True, num=10)
    u, v = np.meshgrid(u, v)
    u, v = u.flatten(), v.flatten()
    x = (1 + 0.5 * v * np.cos(u / 2.0)) * np.cos(u)
    y = (1 + 0.5 * v * np.cos(u / 2.0)) * np.sin(u)
    z = 0.5 * v * np.sin(u / 2.0)
    tri = mtri.Triangulation(u, v)

    # # Plot
    surf = ax.plot_trisurf(x, y, z, triangles=tri.triangles, cmap='cool')

    # # Customize the z axis.
    ax.set_zlim(-1.01, 1.01)
    ax.zaxis.set_major_locator(LinearLocator(5))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()

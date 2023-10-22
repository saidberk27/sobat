import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

harita_genislik = 20
harita_yukseklik = 20

fig, ax = plt.subplots()
ax.set_aspect('equal')

ax.set_xlim(0, harita_genislik)
ax.set_ylim(0, harita_yukseklik)

ax.grid(True, markevery=0.5)

ax.set_xlabel('X (metre)')
ax.set_ylabel('Y (metre)')

plt.title('Sobat Havuz Haritası')

x_grid = np.arange(0, harita_genislik, 1)  # Her 1 metrede bir x koordinatı
y_grid = np.arange(0, harita_yukseklik, 1)  # Her 1 metrede bir y koordinatı
ax.set_xticks(x_grid)
ax.set_yticks(y_grid)


img = mpimg.imread('submarine.png')
ax.imshow(img, extent=[9, 11, 9, 11])

plt.show()

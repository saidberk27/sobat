import sys
import random
import time
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class RealTimePlot(QMainWindow):
    map_height = 20
    map_width = 20

    def __init__(self):
        super().__init__()

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.setCentralWidget(self.canvas)

        self.ax = self.figure.add_subplot(111)
        self.ax.set_xlim(0, self.map_height)
        self.ax.set_ylim(0, self.map_width)
        self.ax.set_xlabel('X (metre)')
        self.ax.set_ylabel('Y (metre)')

        self.ax.grid(True, linestyle='-', linewidth=0.5, which='both')

        self.timer = self.canvas.new_timer(100, [(self.update_plot, [], {})])
        self.timer.start()

        self.show()

        # Harita üzerine resmi ekleyin
        self.add_image_to_center("submarine.png")

    def add_image_to_center(self, image_path):
        # Resmi harita ortasına eklemek için extent parametresini hesaplayın
        image = plt.imread(image_path)
        image_height, image_width = [1, 1]
        extent = [(self.map_width - image_width) / 2, (self.map_width + image_width) / 2,
                  (self.map_height - image_height) / 2, (self.map_height + image_height) / 2]
        self.ax.imshow(image, extent=extent)

    def update_plot(self):
        x = random.uniform(0, self.map_height)
        y = random.uniform(0, self.map_width)
        self.ax.scatter(x, y, color='red', s=10)
        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RealTimePlot()
    sys.exit(app.exec_())

import sys
from PyQt6 import QtCore, QtGui, QtWidgets
import lib

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(800, 600)
        canvas.fill(QtCore.Qt.GlobalColor.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_something()

    def draw_something(self):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)

        # Círculo sin relleno
        circulo1 = lib.Circulo(100, 100, 50, False)
        circulo1.dibujar(painter)

        # Círculo con relleno
        circulo2 = lib.Circulo(600, 10, 100, True, "magenta")
        circulo2.dibujar(painter)

        # Rectángulo con relleno
        rec1 = lib.Rectangulo(200, 200, 100, 100, True, "amarillo")
        rec1.dibujar(painter)

        # Rectángulo sin relleno
        rec2 = lib.Rectangulo(400, 400, 100, 100, False)
        rec2.dibujar(painter)

        # Triangulo con relleno
        tri1 = lib.Triangulo(80, 200, 100, 100, True, "orange")
        tri1.dibujar(painter)

        # Triangulo sin relleno
        tri2 = lib.Triangulo(50, 300, 50, 50, False)
        tri2.dibujar(painter)

        # Pentagono con relleno
        pent1 = lib.Pentagono(500, 250, 50, True, "cyan")
        pent1.dibujar(painter)

        # Pentagono sin relleno
        pent1 = lib.Pentagono(500, 500, 50, False)
        pent1.dibujar(painter)

        painter.end()
        self.label.setPixmap(canvas)

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()


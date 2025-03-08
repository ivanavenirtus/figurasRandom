import sys
import json
from PyQt6 import QtCore, QtGui, QtWidgets
import lib

# JSON de ejemplo
json_data = '''{
    "geometricas": [
        {"circulo": {"radio": 50, "color": "rojo", "x": 50, "y": 45}},
        {"trianguloEquilatero": {"lado": 50, "x": 200, "y": 5}},
        {"pentagono": {"lado": 10, "color": "verde", "x": 50, "y": 45}},
        {"circulo": {"radio": 60, "x": 0, "y": 0}}
    ]
}'''

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(800, 600)
        canvas.fill(QtCore.Qt.GlobalColor.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_from_json(json_data)

    def draw_from_json(self, json_data):
        data = json.loads(json_data)
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)

        for item in data["geometricas"]:
            for figura, atributos in item.items():
                color_nombre = atributos.get("color")
                color_qt = lib.COLOR_MAP.get(color_nombre, QtCore.Qt.BrushStyle.NoBrush)

                if figura == "circulo":
                    lib.Circulo(atributos["x"], atributos["y"], atributos["radio"], bool(color_nombre), color_qt).dibujar(painter)
                elif figura == "trianguloEquilatero":
                    lib.Triangulo(atributos["x"], atributos["y"], atributos["lado"], atributos["lado"], bool(color_nombre), color_qt).dibujar(painter)
                elif figura == "pentagono":
                    lib.Pentagono(atributos["x"], atributos["y"], atributos["lado"], bool(color_nombre), color_qt).dibujar(painter)

        painter.end()
        self.label.setPixmap(canvas)

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

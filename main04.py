import sys
import json
import requests
from PyQt6 import QtCore, QtGui, QtWidgets
import lib

URL = "http://localhost:8000/figuras_random"

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(800, 600)
        canvas.fill(QtCore.Qt.GlobalColor.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)

        # Obtener JSON desde localhost
        json_data = self.get_json_data()
        if json_data:
            self.draw_from_json(json_data)

    def get_json_data(self):
        try:
            response = requests.get(URL)
            response.raise_for_status()
            print("Respuesta cruda del servidor:", response.text)  # Imprime la respuesta sin procesar
            return response.json()  
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener JSON: {e}")
            return None

    def draw_from_json(self, json_data):
        # Si el JSON es una lista, iteramos directamente
        if not isinstance(json_data, list):
            print("Error: El JSON no es una lista como se esperaba.")
            return

        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)

        for item in json_data:
            figura = item["nombre"]
            x = item["x"]
            y = item["y"]
            medida = item["medida"]

            color_nombre = item.get("color")  # Extraer el color
            color_qt = lib.COLOR_MAP.get(color_nombre, QtCore.Qt.GlobalColor.black)  # Buscar en el mapa de colores

            if figura == "circulo":
                lib.Circulo(x, y, medida, True, color_qt).dibujar(painter)
            elif figura == "triangulo":
                lib.Triangulo(x, y, medida, medida, True, color_qt).dibujar(painter)
            elif figura == "cuadrado":
                lib.Cuadrado(x, y, medida, medida, True, color_qt).dibujar(painter)
            elif figura == "pentagono":
                lib.Pentagono(x, y, medida, True, color_qt).dibujar(painter) 

        painter.end()
        self.label.setPixmap(canvas)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()


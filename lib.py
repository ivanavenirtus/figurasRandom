from PyQt6.QtGui import QPolygonF, QPainter, QBrush, QColor
from PyQt6.QtCore import QPointF, Qt
import math

# Colores
COLOR_MAP = {
    "azul": Qt.GlobalColor.blue,
    "rojo": Qt.GlobalColor.red,
    "verde": Qt.GlobalColor.green,
    "amarillo": Qt.GlobalColor.yellow,  
    "negro": Qt.GlobalColor.black,
    "blanco": Qt.GlobalColor.white,
    "cyan": Qt.GlobalColor.cyan,
    "magenta": Qt.GlobalColor.magenta,
    "gris": Qt.GlobalColor.gray,
    "grisOscuro": Qt.GlobalColor.darkGray,
    "grisClaro": Qt.GlobalColor.lightGray,
}


def aplicar_color(func):
    def wrapper(self, painter: QPainter):
        # Aplica el color antes de dibujar
        if self.color:
            painter.setBrush(QBrush(self.color_personalizado))  # Aplica color
        else:
            painter.setBrush(Qt.BrushStyle.NoBrush)  # Sin relleno

        return func(self, painter)  

    return wrapper

class Figura:
    def __init__(self, x, y, color=True, color_personalizado=Qt.GlobalColor.green):
        self.x = x
        self.y = y
        self.color = color
        # Aseguramos que el color sea un objeto QColor
        self.color_personalizado = QColor(color_personalizado) if isinstance(color_personalizado, str) else color_personalizado

    def dibujar(self, painter: QPainter):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

class Circulo(Figura):
    def __init__(self, x, y, radio, color=True, color_personalizado=Qt.GlobalColor.green):
        super().__init__(x, y, color, color_personalizado)
        self.radio = radio
        print(f"Se ha creado un círculo en ({self.x}, {self.y}) con radio {self.radio}")

    @aplicar_color
    def dibujar(self, painter: QPainter):
        painter.drawEllipse(self.x - self.radio, self.y - self.radio, self.radio * 2, self.radio * 2)

class Cuadrado(Figura):
    def __init__(self, x, y, ancho, alto, color=True, color_personalizado=Qt.GlobalColor.green):
        super().__init__(x, y, color, color_personalizado)
        self.ancho = ancho
        self.alto = alto
        print(f"Se ha creado un cuadrado en ({self.x}, {self.y}) con ancho {self.ancho} y alto {self.alto}")

    @aplicar_color
    def dibujar(self, painter: QPainter):
        painter.drawRect(self.x, self.y, self.ancho, self.alto)

class Triangulo(Figura):
    def __init__(self, x, y, base, altura, color=True, color_personalizado=Qt.GlobalColor.green):
        super().__init__(x, y, color, color_personalizado)
        self.base = base
        self.altura = altura
        print(f"Se ha creado un triángulo en ({self.x}, {self.y}) con base {self.base} y altura {self.altura}")

    @aplicar_color
    def dibujar(self, painter: QPainter):
        puntos = QPolygonF([
            QPointF(self.x, self.y),
            QPointF(self.x + self.base, self.y),
            QPointF(self.x + self.base / 2, self.y - self.altura)
        ])
        painter.drawPolygon(puntos)

class Pentagono:
    def __init__(self, x, y, radio, color=True, color_personalizado=QColor("black")):
        self.x = x
        self.y = y
        self.radio = radio
        self.color = color
        self.color_personalizado = QColor(color_personalizado) if isinstance(color_personalizado, str) else color_personalizado

    def dibujar(self, painter: QPainter):
        painter.setBrush(self.color_personalizado if self.color else Qt.BrushStyle.NoBrush)

        puntos = QPolygonF()
        angulo_offset = math.radians(90)  
        
        for i in range(5):
            angulo = angulo_offset + (2 * math.pi * i) / 5
            x_punto = self.x + self.radio * math.cos(angulo)
            y_punto = self.y - self.radio * math.sin(angulo)
            puntos.append(QPointF(x_punto, y_punto))

        painter.drawPolygon(puntos)













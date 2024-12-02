import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsEllipseItem
from PyQt6 import uic
from PyQt6.QtGui import QBrush, QColor
from PyQt6.QtCore import Qt, QRectF

class CircleWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Загрузка UI из файла
        uic.loadUi("untitled.ui", self)

        # Инициализация QGraphicsScene
        self.scene = QGraphicsScene(self)
        self.graphicsView.setScene(self.scene)  # Предполагается, что у вашего QGraphicsView имя graphicsView

        # Подключение кнопки к методу
        self.create_btn.clicked.connect(self.add_circle)  # Предполагается, что у вашей кнопки имя pushButton

    def add_circle(self):
        # Генерация случайного радиуса и положения
        radius = random.randint(10, 100)
        x = random.randint(0, self.graphicsView.width() - radius * 2)
        y = random.randint(0, self.graphicsView.height() - radius * 2)

        # Создание окружности
        circle = QGraphicsEllipseItem(QRectF(x, y, radius * 2, radius * 2))
        circle.setBrush(QBrush(QColor("yellow")))
        self.scene.addItem(circle)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CircleWindow()
    window.show()
    sys.exit(app.exec())
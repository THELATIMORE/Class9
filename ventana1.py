import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QApplication
from PyQt5 import QtGui


class ventana1(QMainWindow):
    def  __init__(self, parent=None):
        super(ventana1, self).__init__(parent)
        self.setWindowTitle("Formulario de registro")
        self.setWindowIcon(QtGui.QIcon("imagenes/Gauss.webp"))
        self.ancho = 800
        self.alto = 700
        self.resize(self.alto, self.ancho)
        self.panalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.panalla.moveCenter(self.centro)
        self.move(self.panalla.topLeft())
        self.setFixedHeight(self.alto)
        self.setFixedWidth(self.ancho)
        self.fondo = QLabel(self)
        self.imagenFondo = QPixmap("imagenes/Jerarquia.jpeg")
        self.fondo.setPixmap(self.imagenFondo)
        self.fondo.setScaledContents(True)
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())
        self.setCentralWidget(self.fondo)
        self.horizontal = QHBoxLayout()
        self.horizontal.setContentsMargins(30 ,30, 30,30)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana1 = ventana1()
    ventana1.show()
    sys.exit(app.exec())

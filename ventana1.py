import sys

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QApplication, QFormLayout, QLineEdit, \
    QPushButton
from PyQt5 import QtGui


class ventana1(QMainWindow):
    def  __init__(self, parent=None):
        super(ventana1, self).__init__(parent)
        self.setWindowTitle("Formulario de registro")
        self.setWindowIcon(QtGui.QIcon("imagenes/Gauss.webp"))
        self.ancho = 800
        self.alto = 600
        self.resize(self.alto, self.ancho)
        self.panalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.panalla.moveCenter(self.centro)
        self.move(self.panalla.topLeft())
        self.setFixedHeight(self.alto)
        self.setFixedWidth(self.ancho)
        self.fondo = QLabel(self)
        self.imagenFondo = QPixmap("imagenes/casco mt.jpg")
        self.fondo.setPixmap(self.imagenFondo)
        self.fondo.setScaledContents(True)
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())
        self.setCentralWidget(self.fondo)
        self.horizontal = QHBoxLayout()
        self.horizontal.setContentsMargins(30 ,30, 30,30)
        #parte izquierda
        self.ladoIzquierdo = QFormLayout()
        self.letrero1 = QLabel()
        self.letrero1.setText("Indormacion del cliente")
        self.letrero1.setFont(QFont("Andale Mono", 20))
        self.letrero1.setStyleSheet("color: red;")
        self.ladoIzquierdo.addRow(self.letrero1)

        self.letrero2 = QLabel()
        self.letrero2.setFixedWidth(340)
        self.letrero2.setText("por favor ingrese la informacion del cliente"
                              "\nen el formulario de abajo.los campos marcados"
                              "\ncon asterisco son obligatorios")
        self.letrero2.setFont(QFont("Andale Mono", 10))
        self.letrero2.setStyleSheet("color: red; margin-bottom: 40px;"
                                    "margin-top: 20px;"
                                    "padding-bottom: 10px;"
                                    "border: 2px solid red;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")
        self.ladoIzquierdo.addRow(self.letrero2)
        self.nombreCompleto = QLineEdit()
        self.nombreCompleto.setFixedWidth(250)
        self.ladoIzquierdo.addRow("Nombre Completo", self.nombreCompleto)
        self.usuario = QLineEdit()
        self.usuario.setFixedWidth(250)
        self.ladoIzquierdo.addRow("Usuario", self.usuario)
        self.password = QLineEdit()
        self.password.setFixedWidth(250)
        self.password.setEchoMode(QLineEdit.Password)
        self.ladoIzquierdo.addRow("Ingrese contraseña", self.password)
        self.password2 = QLineEdit()
        self.password2.setFixedWidth(250)
        self.password2.setEchoMode(QLineEdit.Password)
        self.ladoIzquierdo.addRow("Ingrese contraseña", self.password2)
        self.documento = QLineEdit()
        self.documento.setFixedWidth(250)
        self.ladoIzquierdo.addRow("ingrese documento", self.documento)
        self.correo = QLineEdit()
        self.correo.setFixedWidth(250)
        self.ladoIzquierdo.addRow("Ingrese Correo electronico", self.correo)
        self.botonRegistrar = QPushButton("Registrar")
        self.botonRegistrar.setFixedWidth(90)
        self.botonRegistrar.setStyleSheet("background-color:grey;"
                                          "color:red;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")
        self.botonRegistrar.clicked.connect(self.accion_botonRegistrar)
        self.botonLimpiar = QPushButton("Limpiar")
        self.botonLimpiar.setFixedWidth(90)
        self.botonLimpiar.setStyleSheet("background-color:grey;"
                                        "color:red;"
                                        "padding: 10px;"
                                        "margin-top: 40px;")
        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)
        self.ladoIzquierdo.addRow(self.botonRegistrar,self.botonLimpiar)








        #importante al final
        self.horizontal.addLayout(self.ladoIzquierdo)


        #esto al final
        self.fondo.setLayout(self.horizontal)


    def accion_botonLimpiar(self):
        pass

    def accion_botonRegistrar(self):
        pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana1 = ventana1()
    ventana1.show()
    sys.exit(app.exec())

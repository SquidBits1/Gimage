import sys
from PyQt6.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QPushButton, QSpinBox, QVBoxLayout, QWidget, \
    QFileDialog, QLabel, QErrorMessage
from PyQt6.QtGui import QImage, QPixmap


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.label: QPushButton = None
        self.setWindowTitle('Gilad GIMP')
        self.setGeometry(500, 200, 600, 600)
        self.count = 2

        self.create_widgets()

    def create_widgets(self):
        button = QPushButton('Click me', self)
        button.setGeometry(100,200, 200, 200)
        button.clicked.connect(self.clicked_button)

        self.label = QLabel('My Label', self)
        self.label.move(100,100)

    def clicked_button(self):
        self.count += self.count
        self.label.setText(str(self.count))


app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())

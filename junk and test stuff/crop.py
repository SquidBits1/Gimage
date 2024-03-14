from PyQt6.QtWidgets import QRubberBand, QLabel, QApplication
from PyQt6 import QtCore
from PyQt6.QtGui import QPixmap
import sys


class ImageGUI(QLabel):

    def __init__(self):
        super().__init__()
        self.rect = None
        self.rubber_band: None | QRubberBand = None
        self.origin = None
        self.setGeometry(200, 200, 200, 200)

    def mousePressEvent(self, ev) -> None:
        self.origin = ev.pos()
        self.rubber_band = QRubberBand(QRubberBand.Shape.Rectangle, self)
        self.rubber_band.setGeometry(QtCore.QRect(self.origin, QtCore.QSize()))
        self.rubber_band.show()

    def mouseMoveEvent(self, ev) -> None:
        self.rubber_band.setGeometry(QtCore.QRect(self.origin, ev.pos()).normalized())

    def mouseReleaseEvent(self, ev) -> None:
        self.rubber_band.hide()
        self.rect = self.rubber_band.geometry()
        self.rubber_band.deleteLater()
        print(self.rect)


if __name__ == "__main__":
    a = QApplication(sys.argv)
    b = ImageGUI()
    b.show()
    sys.exit(a.exec())
 
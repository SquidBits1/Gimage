from . import GUI
from PyQt6.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)


def create_test_gui():
    return GUI.MainWindow()


def test_open_file():
    test_gui = create_test_gui()
    test_gui.open_file()
    image = test_gui.image_data
    assert image.source_image_data is not None


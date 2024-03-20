# from core.GUI.GUI import MainWindow
# from PyQt6.QtWidgets import QApplication
# import sys
#
# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
from . import image_data


def create_test_image():
    return image_data.ImageData()


def test_deque():
    test_image = create_test_image()
    test_image.add_image("Filler0")
    test_image.add_image("Filler1")
    assert test_image.image_queue[-1] == "Filler1" and test_image.image_queue[-2] == "Filler0"


def test_deleting_old():
    test_image = create_test_image()
    for i in range(test_image.maxlength + 1):
        test_image.add_image(f"Filler{i}")
    assert "Filler0" not in test_image.image_queue

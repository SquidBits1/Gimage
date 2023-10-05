import sys
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QPushButton, QSpinBox, QVBoxLayout, QWidget, \
    QFileDialog, QLabel, QErrorMessage, QMenu, QAction
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt
from PIL import Image
import numpy as np
import helper


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        # The title of the window
        self.setWindowTitle('Gilad GIMP')
        self.setGeometry(200, 200, 800, 600)

        # Defines the layouts of the window
        main_layout = QVBoxLayout()
        image_bar_layout = QHBoxLayout()
        top_bar_layout = QHBoxLayout()
        bottom_bar_layout = QHBoxLayout()

        # Important variables
        self.source_filename = None
        self.source_image_data = None
        self.processed_source_image_data = None
        self.max_img_height = 400
        self.max_img_width = 600
        self.threshold = 127

        # Loads in functions
        self.functions = helper.functions

        # Menu Bar and actions initialised
        self.function_actions = dict()
        self._create_actions()
        self._connect_actions()
        self._create_menu()

        # Adds labels to layout
        main_layout.addLayout(top_bar_layout)
        main_layout.addLayout(image_bar_layout)
        main_layout.addLayout(bottom_bar_layout)
        self._create_labels()

        # image bar labels
        image_bar_layout.addWidget(self.image_label)
        image_bar_layout.addWidget(self.processed_image_label)

        # Finalise
        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

    # Handles creating menu bar
    # TODO Add icons to menu options
    def _create_menu(self):
        menu_bar = self.menuBar()

        # File Menu
        file_menu = QMenu('&File', self)
        menu_bar.addMenu(file_menu)
        file_menu.addAction(self.open_action)
        file_menu.addAction(self.save_action)
        file_menu.addSeparator()
        file_menu.addAction(self.exit_action)

        # Edit Menu
        edit_menu = QMenu('&Edit', self)
        menu_bar.addMenu(edit_menu)

        for action in self.function_actions:
            edit_menu.addAction(action)

        # Help Menu
        help_menu = QMenu('&Help', self)
        menu_bar.addMenu(help_menu)
        help_menu.addAction(self.about_action)

    # Handles creating actions for the menu bar
    def _create_actions(self):
        self.open_action = QAction("&Open...", self)
        self.save_action = QAction("&Save...", self)
        self.exit_action = QAction("&Exit", self)

        self.about_action = QAction("&About", self)

        for function in self.functions:
            self.function_actions[QAction(function, self)] = self.functions[function]

    def _create_labels(self):
        self.image_label = QLabel()
        self.processed_image_label = QLabel()

    def _connect_actions(self):
        self.open_action.triggered.connect(self.open_file)

        # Connects all the actions to functions
        for action in self.function_actions:
            # TODO work out  how to pass paramaters to these functions
            action.triggered.connect(self.function_actions[action])

    def _process_image(self):
        # TODO convert to Qpixmap from numpy array
        processed_image = QImage(self.processed_source_image_data)

    # Opens a file and converts it into a pixmap to show a picture with correct aspect ratio
    def open_file(self):
        self.source_filename, file_type = QFileDialog.getOpenFileName(self, "Open Image File",
                                                                      r"C:\\Users\\Gilad\\Pictures",
                                                                      "All files (*.*);;BMP (*.bmp);;CUR ("
                                                                      "*.cur);;GIF (*.gif);;ICNS (*.icns);;ICO "
                                                                      "(*.ico);;JPEG (*.jpeg);;JPG (*.jpg);;PBM "
                                                                      "(*.pbm);;PGM (*.pgm);;PNG (*.png);;PPM ("
                                                                      "*.ppm);;SVG (*.svg);;SVGZ (*.svgz);;TGA "
                                                                      "(*.tga);;TIF (*.tif);;TIFF ("
                                                                      "*.tiff);;WBMP (*.wbmp);;WEBP ("
                                                                      "*.webp);;XBM (*.xbm);;XPM (*.xpm)"
                                                                      )
        pixmap_image = QPixmap(self.source_filename)
        pixmap_image = pixmap_image.scaled(800, 600, Qt.KeepAspectRatio)

        self.source_image_data = np.array(Image.open(self.source_filename))

        self.image_label.setPixmap(pixmap_image)
        self.processed_image_label.setPixmap(pixmap_image)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())

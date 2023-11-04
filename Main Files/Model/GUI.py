import sys
from PyQt6.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QVBoxLayout, QWidget, \
    QFileDialog, QLabel, QMenu
from PyQt6.QtGui import QPixmap, QAction
from PyQt6.QtCore import Qt
from PIL import Image
from PIL.ImageQt import ImageQt
import numpy as np
from . import plugin_processor
from . import helper


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
        self.file_type = None
        self.source_image_data = None
        self.processed_source_image_data = None
        self.max_img_height = 400
        self.max_img_width = 600
        self.threshold = 127
        self.current_function = None

        # Loads in plugins
        self.plugins = plugin_processor.plugins
        for plugin in self.plugins.values():
            plugin.parent = self

        # Menu Bar and actions initialised
        self.plugin_actions = dict()
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

        for action in self.plugin_actions:
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

        for plugin in self.plugins:
            self.plugin_actions[QAction(plugin, self)] = self.plugins[plugin]

    def _create_labels(self):
        self.image_label = QLabel()
        self.processed_image_label = QLabel()

    def _connect_actions(self):
        self.open_action.triggered.connect(self.open_file)

        # Connects all the actions to functions
        for action in self.plugin_actions:
            action.triggered.connect(self.plugin_actions[action].run_function)

    def process_image(self):

        image = Image.fromarray(self.processed_source_image_data).convert('RGBA')
        qimg = ImageQt(image)
        processed_image = QPixmap.fromImage(qimg)
        processed_image = processed_image.scaled(800, 600, Qt.AspectRatioMode.KeepAspectRatio)
        self.processed_image_label.setPixmap(processed_image)

    # Opens a file and converts it into a pixmap to show a picture with correct aspect ratio
    def open_file(self):
        self.source_filename, self.file_type = QFileDialog.getOpenFileName(self, "Open Image File",
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

        # Handles checking if file has been picked/valid file
        if not helper.is_valid_image_file(self.source_filename):
            return
        else:
            pixmap_image = QPixmap(self.source_filename)
            pixmap_image = pixmap_image.scaled(800, 600, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)

            self.source_image_data = np.array(Image.open(self.source_filename))
            self.image_label.setPixmap(pixmap_image)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())

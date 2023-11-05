import sys
from PyQt6.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QVBoxLayout, QWidget, \
    QFileDialog, QLabel, QMenu
from PyQt6.QtGui import QPixmap, QAction
from PyQt6.QtCore import Qt
from PIL import Image
from PIL.ImageQt import ImageQt
import numpy as np
from .Classes import plugin_processor, ImageData
from . import helper


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        # The title of the window
        self.setWindowTitle('Gilad GIMP')
        self.setGeometry(200, 200, 800, 600)

        # stores the image class
        self.image: ImageData.ImageData | None = None

        # Function attributes
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

        # Create Layouts
        self._create_layout()

        # Finalise
        widget = QWidget()
        widget.setLayout(self.main_layout)
        self.setCentralWidget(widget)

    # Creates layouts
    def _create_layout(self):
        # Defines the layouts of the window
        self.main_layout = QVBoxLayout()
        self.image_bar_layout = QHBoxLayout()
        self.image_layout = QVBoxLayout()
        self.processed_image_layout = QVBoxLayout()
        self.top_bar_layout = QHBoxLayout()
        self.bottom_bar_layout = QHBoxLayout()


        # Adds labels to layout
        self.main_layout.addLayout(self.top_bar_layout)
        self.main_layout.addLayout(self.image_bar_layout)
        self.image_bar_layout.addLayout(self.image_layout)
        self.image_bar_layout.addLayout(self.processed_image_layout)
        self.main_layout.addLayout(self.bottom_bar_layout)
        self._create_labels()

        # image bar labels
        self.image_layout.addWidget(self.textbox)
        self.image_layout.addWidget(self.image_label)

        self.processed_image_layout.addWidget(self.edit_textbox)
        self.processed_image_layout.addWidget(self.processed_image_label)


    def _create_labels(self):
        self.image_label = QLabel()
        self.processed_image_label = QLabel()

        self.textbox = QLabel()
        self.edit_textbox = QLabel()

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



    def _connect_actions(self):
        self.open_action.triggered.connect(self.open_file)

        # Connects all the actions to functions
        for action in self.plugin_actions:
            action.triggered.connect(self.plugin_actions[action].run_function)

    def process_image(self):
        image = Image.fromarray(self.image.processed_image_datas[0]).convert('RGBA')
        qimg = ImageQt(image)
        processed_image = QPixmap.fromImage(qimg)
        processed_image = processed_image.scaled(800, 600, Qt.AspectRatioMode.KeepAspectRatio)
        self.processed_image_label.setPixmap(processed_image)
        self.edit_textbox.setText(self.current_function)

    # Opens a file and converts it into a pixmap to show a picture with correct aspect ratio
    def open_file(self):
        source_filename, file_type = QFileDialog.getOpenFileName(self, "Open Image File",
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
        valid, filetype = helper.is_valid_image_file(source_filename)
        if not valid:
            self.textbox.setText('Image not valid')
            return
        else:
            # Creates image object with image data
            self.image = ImageData.ImageData(source_filename, np.array(Image.open(source_filename)))

            # Shows image on window
            pixmap_image = QPixmap(self.image.source_filename)
            pixmap_image = pixmap_image.scaled(800, 600, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
            self.image_label.setPixmap(pixmap_image)
            self.textbox.setText(f'{self.image}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())

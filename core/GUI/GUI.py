import sys
import os
from PyQt6.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QVBoxLayout, QWidget, QLabel, QMenu
from PyQt6.QtGui import QAction, QIcon, QFont
from PIL import Image
from core.plugin_manager import discover
from core.plugin_manager.util import image_data
from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import numpy as np
from core.GUI.helpers import helper
from core.plugin_manager.util import image_data
from sys import exit
from os import path, mkdir


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        print(self.dir)
        # The title of the window
        self.setWindowTitle('Gimage')
        self.setWindowIcon(QIcon(self.dir + '\\resources\\letter_g.png'))
        self.setGeometry(200, 200, 800, 600)

        # stores the image class
        self.image: None | image_data.ImageData = None

        # Function attributes
        self.current_function = None
        self.pillow_image: Image.Image | None = None

        # Loads in plugin_manager
        self._handle_plugins()

        # Menu Bar and actions initialised
        self.plugin_actions = dict()
        self._create_actions()
        self._create_menu()

        # Create Layouts
        self._create_layout()

        # Finalise
        widget = QWidget()
        widget.setLayout(self.main_layout)
        self.setCentralWidget(widget)

        self.result_label = None
        self._connect_actions()

    def _handle_plugins(self):
        self.plugin_dict = discover.setup_configuration(discover.discover_plugins())

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
        self.top_bar_layout.addWidget(self.textbox)
        self.image_layout.addWidget(self.image_label)

        self.bottom_bar_layout.addWidget(self.edit_textbox)
        self.processed_image_layout.addWidget(self.processed_image_label)

    def _create_labels(self):
        self.image_label = QLabel()
        self.processed_image_label = QLabel()

        self.textbox = QLabel()
        self.edit_textbox = QLabel()
        self.edit_textbox.setFont(QFont("Helvetica", 20))

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
        edit_menu.addAction(self.undo_action)
        edit_menu.addSeparator()
        for package in self.plugin_dict.items():
            package_name, plugin_list = package
            menu = QMenu(package_name, self)
            edit_menu.addMenu(menu)
            for plugin in plugin_list:
                # Creates an instance of the plugin
                plugin_instance = plugin()
                # Gets the name of the class
                # TODO name plugin_action better
                plugin_action = QAction(plugin_instance.__class__.__name__)
                self.plugin_actions[plugin_action] = plugin_instance.invoke
                # Tells the plugin instance that the GUI is its parent
                plugin_instance.parent = self
                # This adds a button to the menu to invoke the plugin
                menu.addAction(plugin_action)

        # Help Menu
        help_menu = QMenu('&Help', self)
        menu_bar.addMenu(help_menu)
        help_menu.addAction(self.about_action)

    # Handles creating actions for the menu bar
    def _create_actions(self):
        self.open_action = QAction("&Open...", self)
        self.save_action = QAction("&Save...", self)
        self.exit_action = QAction("&Exit", self)

        self.undo_action = QAction("&Undo", self)

        self.about_action = QAction("&About", self)  #

    def _connect_actions(self):
        self.open_action.triggered.connect(self.open_file)
        self.save_action.triggered.connect(self.save_file)

        self.undo_action.triggered.connect(self.undo_edit)
        self.exit_action.triggered.connect(exit)

        # Connects all the actions to functions
        for action in self.plugin_actions:
            action.triggered.connect(self.plugin_actions[action])

    def process_image(self):
        image_data = self.image.processed_image_data[-1]
        if image_data is not None:
            self.pillow_image = Image.fromarray(image_data).convert('RGBA')
            qimg = ImageQt(self.pillow_image)
            processed_image = QPixmap.fromImage(qimg)
            processed_image = processed_image.scaled(800, 600, Qt.AspectRatioMode.KeepAspectRatio)
            self.processed_image_label.setPixmap(processed_image)
        self.edit_textbox.setText(repr(self.current_function))

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

            self.image = image_data.ImageData(source_filename, np.array(Image.open(source_filename)))
            self.image.filetype = filetype

            # Shows image on window
            pixmap_image = QPixmap(self.image.source_filename)
            pixmap_image = pixmap_image.scaled(800, 600, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
            self.image_label.setPixmap(pixmap_image)
            self.textbox.setText(f'{self.image}')

    def save_file(self):
        if not self.pillow_image:
            self.edit_textbox.setText('Image not edited yet')
            return

        saved_path = f'{self.dir}\\Saved Images'
        # if there is no saved_image path, it creates one
        if not path.isdir(saved_path):
            mkdir(saved_path)

        self.pillow_image.save(saved_path + f"\\{self.image.no_extension}_edited.png", format='PNG')

        self.edit_textbox.setText('Saved Image')

    def undo_edit(self):
        try:
            self.image.undo_change()
            self.process_image()
        except IndexError as error:
            self.edit_textbox.setText(str(error))

    def change_label(self, value):
        self.result_label.setText(f"Current Value: {value}")

    # Adds an options layout when needed
    def add_options(self, widget):
        self.top_bar_layout.addWidget(widget)

    def clear_option(self):
        # TODO it is more efficient to use a QStackedWindow, but this would mean refactoring how plugins create option-
        #  -widgets (they would need to check if there is already a widget in the QStackedWindow
        for i in reversed(range(self.top_bar_layout.count())):
            self.top_bar_layout.itemAt(i).widget().setParent(None)
        self.top_bar_layout.addWidget(self.textbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())

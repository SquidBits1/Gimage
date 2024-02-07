from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import numpy as np
from core.GUI.GUI import MainWindow
from core.GUI.helpers import helper
from core.plugin_manager.util import image_data
from sys import exit
from os import path, mkdir


class ProcessWindow(MainWindow):

    def __init__(self):
        super().__init__()
        self.result_label = None
        self._connect_actions()

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

        self.pillow_image.save(saved_path+ f"\\{self.image.no_extension}_edited.png", format='PNG')

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

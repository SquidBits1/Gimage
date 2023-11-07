from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import numpy as np
from core.GUI import MainWindow
from core.helpers import helper
from core.helpers.classes import ImageData


class ProcessWindow(MainWindow):

    def __init__(self):
        super().__init__()
        self._connect_actions()

    def _connect_actions(self):
        self.open_action.triggered.connect(self.open_file)
        self.save_action.triggered.connect(self.save_file)

        # Connects all the actions to functions
        for action in self.plugin_actions:
            action.triggered.connect(self.plugin_actions[action].run_function)

    def process_image(self):
        self.pillow_image = Image.fromarray(self.image.processed_image_datas[0]).convert('RGBA')
        qimg = ImageQt(self.pillow_image)
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
            self.image.filetype = filetype

            # Shows image on window
            try:
                pixmap_image = QPixmap(self.image.source_filename)
                pixmap_image = pixmap_image.scaled(800, 600, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
                self.image_label.setPixmap(pixmap_image)
                self.textbox.setText(f'{self.image}')
            except Exception as error:
                print(error)

    def save_file(self):
        if not self.pillow_image:
            self.edit_textbox.setText('Image not edited yet')
            return

        self.pillow_image.save(f'{self.dir}\Saved Images\{self.image.no_extension}_edited.png', format='PNG')

        self.edit_textbox.setText('Saved Image')

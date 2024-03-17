import sys
import os
from PyQt6.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QVBoxLayout, QWidget, QLabel, QMenu, QFileDialog
from PyQt6.QtGui import QAction, QIcon, QFont, QPixmap
from core.plugin_manager import discover
from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt6.QtCore import Qt
import numpy as np
from core.GUI.helpers import helper
from core.plugin_manager.util import image_data
from sys import exit
from os import path, mkdir


class MainWindow(QMainWindow):
    """
    A class to represent the main window. All widgets will be contained within this
    """

    def __init__(self):
        """
        This runs before the window is created and initialises many things. It sets up the properties of the window and
        creates widgets to be put in the window. It also configures the menu bar to contain all the relevant
         buttons needed.
        """

        super(MainWindow, self).__init__()

        # gets the path to the root directory of the project
        self.dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        # Sets title, icon and geometry of the window
        self.setWindowTitle('Gimage')
        self.setWindowIcon(QIcon(self.dir + '\\resources\\letter_g.png'))
        self.setGeometry(200, 200, 800, 600)

        # Declares the image_data variable
        self.image_data: None | image_data.ImageData = image_data.ImageData()

        # plugin function attributes
        self.current_function = None
        # self.pillow image contains the pillow image representation of an image. This is with NumPy to get array image
        # data
        self.pillow_image: Image.Image | None = None

        # Discovers and sets up plugins using the plugin manager
        self.plugin_dict = discover.setup_configuration(discover.discover_plugins())

        # This dictionary will be of the form [plugin action: invoke method of plugin].
        # The plugin action is the pyqt way of connecting buttons and functions,  a button will be associated
        # with a certain action which in turn is associated with a written function.
        self.plugin_actions = dict()
        # Menu Bar and actions initialised
        self._create_actions()
        self._create_menu()

        # Create Layouts
        self._create_layout()

        # Adds the whole layout structure to the window using a central widget
        widget = QWidget()
        widget.setLayout(self.main_layout)
        self.setCentralWidget(widget)

        # Connects actions (pressing buttons) to the functions that they should result in
        self._connect_actions()

    def _create_layout(self):
        """
        A method that creates the overall layout of the window by specifying different layouts and
         adding widgets to them.
        :return:
        """
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
        """
        Creates the label widgets that go in the layout
        :return:
        """
        # This label shows the image before edits and is on the left of the screen
        self.image_label = QLabel()
        # This label shows how the currently edited image looks and is on the right of the screen
        self.processed_image_label = QLabel()

        # Creates some text-boxes to show things on screen
        self.textbox = QLabel()
        self.edit_textbox = QLabel()
        self.edit_textbox.setFont(QFont("Helvetica", 20))

    def _create_menu(self):
        """
        Creates a menu bar that sits on the top of the window. This menu bar has a file and edit dropdown.
        The file dropdown contains buttons to open, save and exit.
        The edit dropdown contains the buttons that let the user edit the image.
        :return:
        """
        # TODO Add icons to menu options

        # creates a menu bar
        menu_bar = self.menuBar()

        # File Menu
        file_menu = QMenu('&File', self)
        menu_bar.addMenu(file_menu)
        file_menu.addAction(self.open_action)
        file_menu.addAction(self.save_action)
        # This adds a visual bar separating buttons to differentiate sections
        file_menu.addSeparator()
        file_menu.addAction(self.exit_action)

        # Edit Menu
        edit_menu = QMenu('&Edit', self)
        menu_bar.addMenu(edit_menu)
        edit_menu.addAction(self.undo_action)
        edit_menu.addSeparator()

        # Loops through every item in the plugin dictionary which is of the form [package name: plugin_list]
        for package in self.plugin_dict.items():
            package_name, plugin_list = package
            # In the dropdown menu, new menus are created for each plugin package
            menu = QMenu(package_name, self)
            edit_menu.addMenu(menu)
            for plugin in plugin_list:
                # Creates an instance of the plugin
                plugin_instance = plugin()
                # Creates an action for the plugin
                plugin_action = QAction(plugin_instance.__class__.__name__)
                # Adds all the plugin actions and their respective functions to a dictionary
                self.plugin_actions[plugin_action] = plugin_instance.invoke
                # Tells the plugin instance that the GUI is its parent
                plugin_instance.parent = self
                # This adds a button to the menu to invoke the plugin
                menu.addAction(plugin_action)

    def _create_actions(self):
        """
        Creates actions for the menu bar
        :return:
        """
        self.open_action = QAction("&Open...", self)
        self.save_action = QAction("&Save...", self)
        self.exit_action = QAction("&Exit", self)

        self.undo_action = QAction("&Undo", self)

    def _connect_actions(self):
        """
        Connects the actions to their respective functions
        :return:
        """
        self.open_action.triggered.connect(self.open_file)
        self.save_action.triggered.connect(self.save_file)

        self.undo_action.triggered.connect(self.undo_edit)
        self.exit_action.triggered.connect(exit)

        # This loop connects the plugin actions to their invoke methods
        for action in self.plugin_actions:
            action.triggered.connect(self.plugin_actions[action])

    def process_image(self):
        """
        Shows the current image in index [-1] of the image queue on screen.
        :return:
        """

        # Gets the image data of the end image
        current_image_data = self.image_data.image_queue[-1]
        if current_image_data is not None:
            # Three representations of the image are used here!
            # First a pillow image is created from the image data
            # Then a QImage is created using the pillow image. This is only done to conserve some image formatting
            # Finally the QImage is used to create a QPixmap, this is the representation optimised for showing on screen
            self.pillow_image = Image.fromarray(current_image_data).convert('RGBA')
            qimg = ImageQt(self.pillow_image)
            processed_image = QPixmap.fromImage(qimg)
            # Scales the image
            processed_image = processed_image.scaled(800, 600, Qt.AspectRatioMode.KeepAspectRatio)
            # Shows it on screen
            self.processed_image_label.setPixmap(processed_image)

    def open_file(self):
        """
        Opens a file dialog to select an image to be opened.
        This image is turned into two representations:
        One is a QPixmap optimised for showing on screen
        One is eventually stored as a NumPy array in my container class ImageData
        :return:
        """

        # Creates file dialog to select a file
        source_filename, file_type = QFileDialog.getOpenFileName(self, "Open Image File",
                                                                 r"C:\\Users\\Gilad\\Pictures",
                                                                 "All files (*.*);;BMP (*.bmp);;CUR ("
                                                                 "*.cur);;GIF (*.gif);;ICNS (*.icns);;ICO "
                                                                 "(*.ico);;JPEG (*.jpeg);;JPG (*.jpg);;PBM "
                                                                 "(*.pbm);;PGM (*.pgm);;PNG (*.png);;PPM ("
                                                                 "*.ppm);;TGA "
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

            # Creates NumPy array from the image and stores it in the ImageData class
            self.image_data = image_data.ImageData(source_filename, np.array(Image.open(source_filename)))
            self.image_data.filetype = filetype

            # Creates QPixmap representation of image and displays it on window (as the image on the left)
            pixmap_image = QPixmap(self.image_data.source_filepath)
            pixmap_image = pixmap_image.scaled(800, 600, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
            self.image_label.setPixmap(pixmap_image)
            # Displays file name above image
            self.textbox.setText(f'{self.image_data}')

    def save_file(self):
        """
        Saves a file in the Saved Images directory in the project.
        :return:
        """

        # Checks if image has been edited yet
        if not self.pillow_image:
            self.edit_textbox.setText('Image not edited yet')
            return

        saved_path = f'{self.dir}\\Saved Images'
        # if there is no Saved Images path, it creates one
        if not path.isdir(saved_path):
            mkdir(saved_path)

        # Uses the pillow representation of the image to save the image
        self.pillow_image.save(saved_path + f"\\{self.image_data.extensionless}_edited.png", format='PNG')

        self.edit_textbox.setText('Saved Image')

    def undo_edit(self):
        """
        Undoes last edit using the ImageData Class
        :return:
        """

        # attempts to call the image_data undo method
        try:
            self.image_data.undo_change()
            self.process_image()
        except IndexError as error:
            self.edit_textbox.setText(str(error))

    def add_options(self, widget):
        """
        Helper function that adds a widget to the space where an options widget should go.
        :param widget: options widget to be added
        :return:
        """
        self.top_bar_layout.addWidget(widget)

    def clear_option(self):
        """
        Clears the space where an options widget should go.
        :return:
        """

        # This provides a way to remove every widget from a layout
        for i in reversed(range(self.top_bar_layout.count())):
            self.top_bar_layout.itemAt(i).widget().setParent(None)
        # adds back in the textbox usually in this layout
        self.top_bar_layout.addWidget(self.textbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())

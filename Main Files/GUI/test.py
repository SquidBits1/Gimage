import sys
from PyQt6.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QPushButton, QSpinBox, QVBoxLayout, QWidget, \
    QFileDialog, QLabel, QErrorMessage, QMenu
from PyQt6.QtGui import QImage, QPixmap, QAction


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        # The title of the window
        self.setWindowTitle('Gilad GIMP')
        self.setGeometry(200, 200, 800, 600)

        # Defines the layouts of the window
        main_layout = QVBoxLayout()

        # Menu Bar and actions initialised
        self._create_actions()
        self._connect_actions()
        self._create_menu()

        # Important variables
        self.source_filename = None
        self.max_img_height = 400
        self.max_img_width = 600

        # Adds labels to layout
        self._create_labels()
        main_layout.addWidget(self.image_label)

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
        # TODO add all edit image options here
        edit_menu = QMenu('&Edit', self)
        menu_bar.addMenu(edit_menu)

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
        # TODO add all edit actions here

    def _create_labels(self):
        self.image_label = QLabel()

    def _connect_actions(self):
        self.open_action.triggered.connect(self.open_file)

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image File", r"C:\\Users\\Gilad\\Pictures",
                                                                            "All files (*.*);;BMP (*.bmp);;CUR ("
                                                                            "*.cur);;GIF (*.gif);;ICNS (*.icns);;ICO "
                                                                            "(*.ico);;JPEG (*.jpeg);;JPG (*.jpg);;PBM "
                                                                            "(*.pbm);;PGM (*.pgm);;PNG (*.png);;PPM ("
                                                                            "*.ppm);;SVG (*.svg);;SVGZ (*.svgz);;TGA "
                                                                            "(*.tga);;TIF (*.tif);;TIFF ("
                                                                            "*.tiff);;WBMP (*.wbmp);;WEBP ("
                                                                            "*.webp);;XBM (*.xbm);;XPM (*.xpm)"
)
        print(file_name)
        self.image_label.setPixmap(QPixmap(file_name))


app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())

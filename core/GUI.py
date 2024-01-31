import sys
import os
from PyQt6.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QVBoxLayout, QWidget, QLabel, QMenu
from PyQt6.QtGui import QAction, QIcon, QFont
from PIL import Image
from core.helpers import image_data
from core.plugin_manager import plugin_manager
from core.plugin_manager import discover


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.dir = os.path.dirname(os.path.dirname(__file__))
        # The title of the window
        self.setWindowTitle('Gimage')
        self.setWindowIcon(QIcon(self.dir + '\\resources\\letter_g.png'))
        self.setGeometry(200, 200, 800, 600)

        # stores the image class
        self.image: image_data.ImageData = image_data.ImageData()

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
        for package in self.plugin_dict.items():
            package_name, plugin_list = package
            menu = QMenu(package_name, self)
            edit_menu.addMenu(menu)
            for plugin in plugin_list:
                plugin_instance = plugin()
                plugin_action = QAction(plugin_instance.__class__.__name__)
                self.plugin_actions[plugin_action] = plugin_instance.invoke
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

        self.about_action = QAction("&About", self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())

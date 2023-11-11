import sys
import os
from PyQt6.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QVBoxLayout, QWidget, QLabel, QMenu
from PyQt6.QtGui import QAction
from PIL import Image
from core.helpers import image_data
from core.plugin_manager import plugin_manager


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.dir = os.path.dirname(os.path.dirname(__file__))
        # The title of the window
        self.setWindowTitle('Gilad GIMP')
        self.setGeometry(200, 200, 800, 600)

        # stores the image class
        self.image: image_data.ImageData = image_data.ImageData()

        # Function attributes
        self.current_function = None
        self.pillow_image: Image.Image | None = None

        # Loads in plugin_manager
        self.plugin_manager = plugin_manager.PluginManager(self.dir+'\\core\\plugin_manager\\plugins')
        self.plugin_manager.load_plugins()

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
        edit_menu.addAction(self.undo_action)
        for manager in self.plugin_manager.manager_list:
            for plugin_name, methods in manager.method_dict.items():
                menu = QMenu(plugin_name, self)
                edit_menu.addMenu(menu)
                for method_name, method in methods.items():
                    method_action = QAction(method_name, self)
                    self.plugin_actions[method_action] = method
                    method.parent = self
                    menu.addAction(method_action)


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
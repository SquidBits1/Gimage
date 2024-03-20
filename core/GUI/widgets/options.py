"""
options.py -
This file contains the classes Options and it's subclasses. They are widgets that plugins can put on screen to adjust
arguments to pass to the plugin's functions.
"""

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt


class Options(QtWidgets.QWidget):
    """
    A widget that allows the user to customise the editing functions by picking arguments.
    """

    def __init__(self, *args):
        super().__init__()
        self.value = None

        # Creates a widget to be pressed. Defaults to a ComboBox but can be overridden
        self.interactor = self.create_interactor(*args)

        # Defines the layout for the interactor
        self.interactor_layout = QtWidgets.QHBoxLayout()
        self.interactor_layout.addWidget(self.interactor)

        # Creates Accept Button
        self.accept_button = QtWidgets.QPushButton(text="Accept")
        self.accept_button.setFixedSize(100, 25)

        overall = QtWidgets.QVBoxLayout()
        overall.addLayout(self.interactor_layout)
        overall.addWidget(self.accept_button)

        self.setLayout(overall)

    def create_interactor(self, *args):
        return QtWidgets.QLabel()

    def get_value(self):
        """
        Obtains current value of buttons
        :return:
        """
        pass

    def connect(self, func):
        self.accept_button.clicked.connect(func)


class SliderOptions(Options):
    """
    An options bar with a slider.
    """

    def __init__(self, minimum=0, maximum=255, start_value=127):
        self.interactor: None | QtWidgets.QSlider = None
        super().__init__(minimum, maximum, start_value)
        self.interactor_layout.addWidget(self.interactor)
        # Creates a label to show the current value
        self.value_display = QtWidgets.QLabel(str(start_value))
        self.value_display.setStyleSheet("border: 1px solid black;")
        self.interactor_layout.addWidget(self.value_display)

    def create_interactor(self, minimum, maximum, start_value):
        interactor = QtWidgets.QSlider(Qt.Orientation.Horizontal)
        interactor.setMinimum(minimum)
        interactor.setMaximum(maximum)
        interactor.setValue(start_value)
        interactor.valueChanged.connect(self.show_value)
        return interactor

    def show_value(self):
        self.value_display.setText(str(self.interactor.value()))

    def get_value(self):
        self.value = self.interactor.value()
        return self.value


class ComboBoxOptions(Options):
    """
    An options bar with a combo box
    """

    def __init__(self, values=None):
        if values is None:
            values = ["option1", "option2", "option3"]
        self.interactor: None | QtWidgets.QComboBox = None
        super().__init__(values)

    def create_interactor(self, values):
        interactor = QtWidgets.QComboBox()
        interactor.addItems(values)
        return interactor

    def get_value(self):
        self.value = self.interactor.currentText()
        return self.value

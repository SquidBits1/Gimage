from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt


class Options(QtWidgets.QWidget):

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

    def __init__(self, minimum=0, maximum=255, start_value=127):
        self.interactor: None | QtWidgets.QSlider = None
        super().__init__(minimum, maximum, start_value)
        self.interactor_layout.addWidget(self.interactor)
        self.display_button = QtWidgets.QLabel(str(start_value))
        self.display_button.setStyleSheet("border: 1px solid black;")
        self.interactor_layout.addWidget(self.display_button)

    def create_interactor(self, minimum, maximum, start_value):
        interactor = QtWidgets.QSlider(Qt.Orientation.Horizontal)
        interactor.setMinimum(minimum)
        interactor.setMaximum(maximum)
        interactor.setValue(start_value)
        interactor.valueChanged.connect(self.show_value)
        return interactor

    def show_value(self):
        self.display_button.setText(str(self.interactor.value()))

    def get_value(self):
        self.value = self.interactor.value()
        return self.value


class ComboBoxOptions(Options):

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
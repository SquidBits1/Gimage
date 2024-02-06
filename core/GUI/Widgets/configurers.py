from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt


class Options(QtWidgets.QWidget):

    def __init__(self, values=None):
        super().__init__()
        self.value = None

        if values is None:
            values = ["option1", "option2", "option3"]

        # Creates a widget to be pressed. Defaults to a ComboBox but can be overridden
        self.interactor = self.create_interactor(values)

        # Defines the layout for the interactor
        self.interactor_layout = QtWidgets.QHBoxLayout()
        self.interactor_layout.addWidget(self.interactor)

        # Creates Accept Button
        accept_button = QtWidgets.QPushButton(text="Accept")
        accept_button.setFixedSize(100, 25)
        accept_button.clicked.connect(self.get_value)

        overall = QtWidgets.QVBoxLayout()
        overall.addLayout(self.interactor_layout)
        overall.addWidget(accept_button)

        self.setLayout(overall)

    def create_interactor(self, values):
        interactor = QtWidgets.QComboBox()
        interactor.addItems(values)
        return interactor

    def get_value(self):
        self.value = self.interactor.currentText()


class SliderOptions(Options):

    def __init__(self, *args):
        self.interactor: QtWidgets.QSlider | None = None
        if args:
            self.minimum = args[0]
            self.maximum = args[1]
            self.start_value = args[2]
        else:
            self.minimum, self.maximum, self.start_value = (0, 256, 127)
        super().__init__()
        self.display_button = QtWidgets.QLabel(str(self.start_value))
        self.display_button.setStyleSheet("border: 1px solid black;")
        self.interactor_layout.addWidget(self.display_button)

    def create_interactor(self, values):
        interactor = QtWidgets.QSlider(Qt.Orientation.Horizontal)
        interactor.setMinimum(self.minimum)
        interactor.setMaximum(self.maximum)
        interactor.setValue(self.start_value)
        interactor.valueChanged.connect(self.show_value)
        return interactor

    def show_value(self):
        self.display_button.setText(str(self.interactor.value()))

    def get_value(self):
        self.value = self.interactor.value()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    button = SliderOptions()
    button.show()
    app.exec()

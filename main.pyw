"""
main.pyw -
This file is what is run to start the application. It creates an application and MainWindow instantiation
and shows the window to the user.
"""

import sys
from core.GUI import GUI


def initialise():
    """
    Initialises the application
    :return:
    """
    # Creates an application object and set's it's style
    app = GUI.QApplication(sys.argv)
    app.setStyle("Fusion")

    # creates a MainWindow object and shows it
    window = GUI.MainWindow()
    window.show()

    # After the window is closed, the program ends
    sys.exit(app.exec())


if __name__ == '__main__':
    initialise()

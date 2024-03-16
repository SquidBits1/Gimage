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
    

def main():
    """
    Starts the program
    :return:
    """
    initialise()
    # test


if __name__ == '__main__':
    main()

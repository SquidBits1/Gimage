import sys
from Model import GUI
from Model.Thresholding import simple_threshold


# links model functions to the GUI
def link_functions(window):
    # TODO is there a way to automate this?
    window.simple_threshold = simple_threshold.binary_threshold


def initialise():
    app = GUI.QApplication(sys.argv)
    window = GUI.MainWindow()
    link_functions(window)
    window.show()

    sys.exit(app.exec())


def main():
    initialise()
    # test


if __name__ == '__main__':
    main()

import sys
from GUI import GUI
from Thresholding import simple_threshold


def initialise():
    app = GUI.QApplication(sys.argv)
    window = GUI.MainWindow()
    # window.button_press.action_function = model.function
    window.show()

    sys.exit(app.exec())


def main():
    initialise()


if __name__ == '__main__':
    main()

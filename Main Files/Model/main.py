import sys
import GUI


def initialise():
    app = GUI.QApplication(sys.argv)
    window = GUI.MainWindow()
    window.show()

    sys.exit(app.exec())


def main():
    initialise()
    # test


if __name__ == '__main__':
    main()

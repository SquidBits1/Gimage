import sys
from core import GUI, processes


def initialise():
    app = GUI.QApplication(sys.argv)
    app.setStyle("Fusion")
    window = processes.ProcessWindow()
    window.show()

    sys.exit(app.exec())
    

def main():
    initialise()
    # test


if __name__ == '__main__':
    main()

import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from gui.ui_main_window import Ui_MainWindow
from core.controller import init_theme


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # == External Initializers
    init_theme(app)

    # == Running
    MainWindow.show()
    sys.exit(app.exec())

import sys

from PySide6.QtWidgets import QApplication

from gui.ui_main_window import Ui_MainWindow
from core.controller import init_theme


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui = Ui_MainWindow()
    ui.setupUi(ui)

    # == External Initializers
    init_theme(app)

    # == Running
    ui.show()
    sys.exit(app.exec())

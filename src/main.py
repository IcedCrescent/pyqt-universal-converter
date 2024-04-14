import sys
from PyQt6.QtWidgets import QApplication

from app_window import AppWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_window = AppWindow()
    main_window.show()
    sys.exit(app.exec())
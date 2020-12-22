from ui.login_window import LoginWindow
from PyQt5 import QtWidgets, QtCore, QtGui
import sys


def main():
	app = QtWidgets.QApplication([])
	login_window = LoginWindow()
	login_window.show()
	sys.exit(app.exec())


if __name__ == "__main__":
	main()

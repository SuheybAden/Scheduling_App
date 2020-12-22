import hashlib
import requests
import os
from PyQt5 import QtGui, QtWidgets, QtCore, uic
from .main_window import MainWindow

url = "https://myapp.org"


class LoginWindow(QtWidgets.QWidget):
	def __init__(self) -> None:
		super().__init__()
		self.load_ui()

	def load_ui(self):
		cwd = os.getcwd()
		filename = os.path.splitext(os.path.basename(__file__))[0]
		uic.loadUi(cwd + "\\ui_files\\" + filename + ".ui", self)
		self.connect_all()

	def connect_all(self):
		self.login_btn.clicked.connect(self.loginClicked_Handler)

	def loginClicked_Handler(self):
		username = self.username_line.text
		password = hashlib.sha512((self.password_line.text()).encode("utf-8"))
		print(password.hexdigest())
		payload = {"user": username, "pass": password.hexdigest()}

		response = requests.post(url+"/login", data=payload)

		if(response.status_code == 200):
			main_window = MainWindow()
			main_window.show()
			self.close()
		else:
			self.close()

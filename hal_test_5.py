#!/usr/bin/env python3

import sys, os, subprocess
# disable cache usage must be before any local imports
sys.dont_write_bytecode = True

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic

import startup

class main(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi(os.path.join(os. getcwd(), 'hal_test_5.ui'), self)
		self.setGeometry(50, 50, 500, 300)
		self.setWindowTitle("HAL Test")
		cp = subprocess.run(['pgrep', '-l', 'linuxcnc'], text=True, capture_output=True)
		if 'linuxcnc' not in cp.stdout:
			print('emc not running')
			sys.exit()

		startup.setup_hal(self)
		self.show()

app = QApplication(sys.argv)
gui = main()
sys.exit(app.exec())

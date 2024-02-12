#!/usr/bin/env python3

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt6.QtWidgets import QSpinBox
import hal, linuxcnc

'''
HAL_BIT
HAL_FLOAT
HAL_U32
HAL_S32
HAL_U64
HAL_S64
'''

class TestWidget(QWidget):
	def __init__(self):
		super().__init__()
		self.halcomp = hal.component('mytest')
		self.halcomp.newpin('out', hal.HAL_BIT, hal.HAL_OUT)
		self.halcomp.newpin('out2', hal.HAL_BIT, hal.HAL_OUT)
		self.halcomp.newpin('in', hal.HAL_BIT, hal.HAL_IN)
		self.halcomp.newpin('value', hal.HAL_U32, hal.HAL_IN)
		self.halcomp.newpin('set_value', hal.HAL_U32, hal.HAL_IN)
		self.halcomp.ready()

		self.setWindowTitle('Test Widget')
		self.setGeometry(300, 300, 250, 150)

		self.layout = QVBoxLayout()
		self.setLayout(self.layout)

		self.test_out = QPushButton('Test Out')
		self.test_out.setCheckable(True)
		self.test_out.clicked.connect(self.set_out_pin)

		self.test_in = QPushButton('Test In')
		self.test_in.setCheckable(True)
		self.test_in.clicked.connect(self.set_in_pin)

		self.number_in = QSpinBox()
		self.number_in.valueChanged.connect(lambda: hal.set_p('mytest.value', f'{self.number_in.value()}'))

		self.set_value = QPushButton('Set Value')
		self.set_value.setCheckable(True)
		self.set_value.clicked.connect(self.set_pin)

		self.layout.addWidget(self.test_out)
		self.layout.addWidget(self.test_in)
		self.layout.addWidget(self.number_in)
		self.layout.addWidget(self.set_value)

		self.test_hal = QPushButton('Test HAL')
		self.test_hal.clicked.connect(lambda: hal.set_p('halui.mode.teleop', "true"))
		self.layout.addWidget(self.test_hal)
		self.show()

		'''
		usually something like this:
		button.clicked.connect(my_function)

		def my_function(state):
		print(state)
		if state:
		parent.hal_test.out.set(10)
		else:
		parent.hal_test.out.set(0)
		'''

	def set_pin(self, state):
		print(state)
		if state:
			self.halcomp.out2.set(10)
		else:
			self.halcomp.out2.set(0)

	def set_out_pin(self, data):
		self.halcomp['out'] = data

	def set_in_pin(self, data):
		self.halcomp['in'] = data

	def closeEvent(self, event):
		event.accept()
		self.halcomp.exit()

app = QApplication([])
w = TestWidget()
app.exec()

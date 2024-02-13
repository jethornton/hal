
from PyQt6.QtWidgets import QPushButton

import hal

'''
This works!
self.halcomp = hal.component('mytest')
self.out2 = self.halcomp.newpin('out2', hal.HAL_BIT, hal.HAL_OUT)
self.test_hal = QPushButton('Test HAL')
self.test_hal.setCheckable(True)
self.test_hal.toggled.connect(lambda: self.out2.set(self.test_hal.isChecked()))

'''

def setup_hal(parent):
	for button in parent.findChildren(QPushButton):
		if button.property('function') == 'hal_pin':
			#print(f'{button.objectName()} {button.property("function")}')
			props = button.dynamicPropertyNames()
			for prop in props:
				prop = str(prop, 'utf-8')
				if prop.startswith('pin_'):
					print(f'prop {prop}')
					pin_settings = button.property(prop).split(',')
					name = button.objectName()
					print(f'name {name}')
					pin_name = pin_settings[0]
					print(f'pin_name {pin_name}')
					pin_type = getattr(hal, f'{pin_settings[1].upper().strip()}')
					print(f'pin_type {pin_type}')
					pin_dir = getattr(hal, f'{pin_settings[2].upper().strip()}')
					print(f'pin_dir {pin_dir}')
					parent.hal_comp = hal.component('jet')
					print(f'{parent.hal_comp.getprefix()}')
					setattr(parent, f'{prop}', parent.hal_comp.newpin(pin_name, pin_type, pin_dir))
					print(getattr(parent, f'{prop}').name)
					print(parent.hal_comp[pin_name])
					print(parent.hal_comp.getpins())
					#print(dir(parent.hal_comp))
					#print(f'parent.{prop}')
					#pin = parent.hal_comp.newpin(pin_name, pin_type, pin_dir)
					#print(f'{parent.hal_comp.getpins()}')
					#self.test_hal.toggled.connect(lambda: self.out2.set(self.test_hal.isChecked()))
					#button.clicked.connect(lambda: getattr(parent, f'{prop}').name.set(True))
					#button.pressed.connect(lambda: hal.set_p(f'parent.{prop}', "True"))
					#button.toggled.connect(lambda: parent.hal_comp[pin_name], button.isChecked())


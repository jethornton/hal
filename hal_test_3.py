#!/usr/bin/env python3

import hal
h = hal.component("test")
pin = h.newpin("out", hal.HAL_U32, hal.HAL_OUT)

print(pin.get_dir() == hal.HAL_OUT)
print(pin.get_dir() == hal.HAL_IN)
print(f'{hal.get_info_pins()}')
print(f'{hal.get_info_signals()}')
print(f'{hal.get_info_params()}')
print(f'{pin.dir}')
print(f'{pin.get()}')
print(f'{pin.get_dir()}')
print(f'{pin.get_name()}')
print(f'{pin.get_type()}')
print(f'{pin.is_pin()}')
print(f'{pin.name}')
print(f'{pin.type}')
print(f'{pin.value}')

#print(f'{dir(h)}')
#print(f'{pin.pin_has_writer()}')
#print(f'{}')
h.exit()

'''
dir(pin)
dir
get
get_dir
get_name
get_type
is_pin
name
set
type
value
'''


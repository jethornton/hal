#!/usr/bin/env python3

import hal
h = hal.component("test")
u32_pin = h.newpin("value", hal.HAL_U32, hal.HAL_OUT)
bit_pin = h.newpin("out", hal.HAL_BIT, hal.HAL_OUT)

print(u32_pin.get_dir() == hal.HAL_OUT)
print(u32_pin.get_dir() == hal.HAL_IN)
print(f'{hal.get_info_pins()}')
print(f'{hal.get_info_signals()}')
print(f'{hal.get_info_params()}')
print(f'{u32_pin.dir}')
print(f'{u32_pin.get()}')
print(f'{u32_pin.get_dir()}')
print(f'{u32_pin.get_name()}')
print(f'{u32_pin.get_type()}')
print(f'{u32_pin.is_pin()}')
print(f'{u32_pin.name}')
print(f'{u32_pin.type}')
print(f'{u32_pin.value}')
u32_pin.set(10)
print(f'{u32_pin.value}')

print(f'bit_pin {bit_pin.value}')
bit_pin.set(True)
print(f'bit_pin {bit_pin.value}')

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


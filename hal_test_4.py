#!/usr/bin/env python3

import hal
h = hal.component("test")
h.newpin("out", hal.HAL_U32, hal.HAL_OUT)
print(f'{h.getitem("out")}')
print(f'{h.getpin}') # this seems to not return anything useful
print(f'{h.getpins()}')
print(f'{h.getprefix()}')
h.setprefix('weird')
print(f'{h.getpins()}')
print(f'{h.getprefix()}')

h.exit()

'''
dir(h)
exit
getitem
getparam
getpin
getpins
getprefix
newparam
newpin
ready
setprefix
unready
'''

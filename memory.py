#!/usr/bin/python3

from psutil import virtual_memory
from psutil._common import bytes2human

memory = virtual_memory()
used = bytes2human(memory.used)
total = bytes2human(memory.total)

print(f"RAM: {used}/{total}")


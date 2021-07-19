#!/usr/bin/python3

from psutil import virtual_memory
from psutil._common import bytes2human
import subprocess

def get_value(value_name):
    value = subprocess.run(['xrescat', f'i3xrocks.{value_name}'], capture_output=True)
    return value.stdout.decode('utf-8')

memory = virtual_memory()
used = bytes2human(memory.used)
total = bytes2human(memory.total)

color = get_value("label.color")
font = get_value("value.font")

print(f"<span color='{color}' font='{font}'>RAM: {used}/{total}</span>")


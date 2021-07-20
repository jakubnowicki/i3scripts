#!/usr/bin/python3

from psutil import cpu_percent
import subprocess
import os

def get_value(value_name):
    value = subprocess.run(['xrescat', f'i3xrocks.{value_name}'], capture_output=True)
    return value.stdout.decode('utf-8')

cpu = cpu_percent(interval=1)

color = get_value("label.color")
font = get_value("value.font")
icon = get_value("label.cpu")

def clicked():
    """Returns True if the button was clicked"""
    button = "BLOCK_BUTTON" in os.environ and os.environ["BLOCK_BUTTON"]
    return bool(button)


if clicked():
    subprocess.run(['/usr/bin/gnome-system-monitor', '--class=floating_window'])

print(f"<span color='{color}' font='{font}'>{icon} </span><span color='{color}' font='{font}'>{cpu}%</span>")


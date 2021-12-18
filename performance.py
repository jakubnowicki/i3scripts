#!/usr/bin/python3

import subprocess
import os

def get_value(value_name):
    value = subprocess.run(['xrescat', f'i3xrocks.{value_name}'], capture_output=True)
    return value.stdout.decode('utf-8')

def clicked():
    """Returns True if the button was clicked"""
    button = "BLOCK_BUTTON" in os.environ and os.environ["BLOCK_BUTTON"]
    return bool(button)

performance_status = subprocess.run(['powerprofilesctl'], capture_output=True)
performance = performance_status.stdout.decode('utf-8').split()
performance_value = performance[performance.index('*') + 1].replace(':', '')

charging_status = subprocess.run(['acpi'], capture_output=True)
charging = charging_status.stdout.decode('utf-8').split()[4]


label_color = color = get_value("label.color")

if performance_value == "performance":
    color = "#ff2200"
elif performance_value == "balanced":
    color = label_color
else:
    color = "#00cc66"

font = get_value("value.font")
small_font = font.replace("13", "10")

possible_values = ["performance", "balanced" ,"power-saver"]

if clicked():
    next_value = possible_values.index(performance_value) + 1
    if next_value > 2:
        next_value = 0
    subprocess.run(['powerprofilesctl', 'set', possible_values[next_value]])

print(f"<span color='{color}' font='{font}'>{performance_value}</span><span color='{label_color}' font='{small_font}'> {charging}</span>")

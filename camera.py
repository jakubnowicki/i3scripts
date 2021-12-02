#!/usr/bin/python3
import subprocess

def get_value(value_name):
    value = subprocess.run(['xrescat', f'i3xrocks.{value_name}'], capture_output=True)
    return value.stdout.decode('utf-8')

camera_status = subprocess.run(['lsof', '/dev/video0'], capture_output=True)
camera_status_value = camera_status.stdout.decode('utf-8')

if camera_status_value:
  status = "on"
  color = "#ff2200"
else:
  status = "off"
  color = "#00cc66"

font = get_value("value.font")
label_color = get_value("label.color")
icon = get_value("label.cpu")

print(f"<span color='{label_color}' font='{font}'>cam: </span><span color='{color}' font='{font}'>{status}</span>")

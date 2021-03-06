#!/usr/bin/python3

from i3ipc import Connection
import subprocess

i3 = Connection()
windows = i3.get_tree().leaves()

windows_list = str()

for i, window in enumerate(windows):
    suffix = "\n"
    if i == len(windows) - 1:
        suffix = ""
    windows_list = windows_list + window.window_title + suffix

command = f'echo "{windows_list}" | dmenu -l 20 -fn \'Fira Code:regular:pixelsize=20\''

process = subprocess.Popen([command],
                     stdout=subprocess.PIPE, 
                     stderr=subprocess.PIPE, shell=True)
stdout, stderr = process.communicate()
selected_window = stdout.decode('utf-8').strip()

focus_command = f'[title="{selected_window}"] focus'
i3.command(focus_command)

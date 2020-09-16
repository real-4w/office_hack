from os import times
import win32gui
import w_vda
import time

current_window_handle = win32gui.GetForegroundWindow()

w_vda.move_window_to_desktop_number(current_window_handle,0)

time.sleep(2)

w_vda.move_window_to_desktop_number(current_window_handle,1)


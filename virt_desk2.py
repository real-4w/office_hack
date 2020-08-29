#https://github.com/mrob95/py-VirtualDesktopAccessor
import pyvda
import win32gui

number_of_active_desktops = pyvda.GetDesktopCount()
current_desktop = pyvda.GetCurrentDesktopNumber()

current_window_handle = win32gui.GetForegroundWindow()
pyvda.MoveWindowToDesktopNumber(current_window_handle, 1)

pyvda.GoToDesktopNumber(2)

window_moved_to = pyvda.GetWindowDesktopNumber(current_window_handle)
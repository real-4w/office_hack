# willems VDA wrapper atound 'VirtualDesktopAccessor.dll' || 64 bits python only
# https://github.com/Ciantic/VirtualDesktopAccessor
import os
import ctypes
from ctypes import cdll
path = os.path.dirname(os.path.realpath(__file__)) 
vda = cdll.LoadLibrary(os.path.join(path,'VirtualDesktopAccessor.dll'))

def move_window_to_desktop_number(hwnd,n):
    vda.MoveWindowToDesktopNumber(hwnd,n) 

def get_current_desktop_number():
    return vda.GetCurrentDesktopNumber() 

def get_desktop_id_by_number(n):
    return vda.GetDesktopIdByNumber(n)

def is_window_on_desktop_number(hwnd,n):
    return vda.IsWindowOnDesktopNumber(hwnd,n)

def is_window_on_current_virtual_desktop(hwnd):
    return vda. IsWindowOnCurrentVirtualDesktop(hwnd)

def get_window_desktop_id(hwnd):
    return vda.GetWindowDesktopId(hwnd)

def get_window_desktop_number_by_id(desktopId):
    return vda. GetDesktopNumberById(desktopId)

def get_window_desktop_number(hwnd):
    return vda.GetWindowDesktopNumber(hwnd)

def get_desktop_count():
    return vda.GetDesktopCount()

def go_to_desktop_number(n=0):
    vda.GoToDesktopNumber(n)

# https://github.com/Ciantic/VirtualDesktopAccessor
# dllmain.h
import os
import ctypes, time
from ctypes import cdll
from time import sleep
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

# def move_current_window_to_desktop(n=0,follow=True):
#    wndh = win32gui.GetForegroundWindow()   
#    vda.MoveWindowToDesktopNumber(wndh,n)
#    if follow:
#        vda.GoToDesktopNumber(n)
if __name__ == "__main__":                                                    #only run when this is called by itself and not imported 
    print(get_desktop_count())
    print(get_current_desktop_number())

   

    go_to_desktop_number(0)
    print ("desktop 0")
    sleep(3)

    go_to_desktop_number(1)
    print ("desktop 1")
    sleep(3)

#pid = wintypes.DWORD()
#user32.GetWindowThreadProcessId(h_wnd, ctypes.byref(pid))
#print(pid.value)

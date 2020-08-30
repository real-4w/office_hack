#use 64 bit python
#uses https://github.com/Ciantic/VirtualDesktopAccessor/blob/master/x64/Release/VirtualDesktopAccessor.dll
#https://stackoverflow.com/questions/60879235/python-windows-10-launching-an-application-on-a-specific-virtual-desktop-envir

import ctypes, time, shlex, subprocess
from pathlib import Path

def launch_apps_to_virtual_desktops(command_lines, desktops=3):
    virtual_desktop_accessor = ctypes.WinDLL(r"C:\Users\vandersw\OneDrive\Documenten\Personal\Python\office_hack\VirtualDesktopAccessor.dll")
    for i in range(desktops):
        virtual_desktop_accessor.GoToDesktopNumber(i)
        time.sleep(0.25) # Wait for the desktop to switch
        for command_line in command_lines:
            if command_line:
                subprocess.Popen(shlex.split(command_line))
        time.sleep(2) # Wait for apps to open their windows
    virtual_desktop_accessor.GoToDesktopNumber(0) # Go back to the 1st desktop

command_lines = """
"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
"C:\Program Files (x86)\Internet Explorer\iexplore.exe"
""".splitlines()



p = Path.home()
print("p = ", p)
print("resolved = ", p.resolve())
print('CWD ', Path.cwd())
print('Parent CWD', Path.cwd().parent)

launch_apps_to_virtual_desktops(command_lines)
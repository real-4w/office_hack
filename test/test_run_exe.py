import ctypes, time, shlex, subprocess

command_lines = [
"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
"C:\Program Files (x86)\Internet Explorer\iexplore.exe"
]

for command_line in command_lines :
    print(command_line)
    command_line = "\"" + command_line + "\""
    print(command_line)
    subprocess.Popen(shlex.split(command_line))

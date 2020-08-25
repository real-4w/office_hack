import webbrowser
import yaml
import ctypes, time, shlex, subprocess
#===========================================================================================================
def ProcessYAML (yaml_file) :
    '''This function opens the yaml file and returns the data object'''
    with open(yaml_file) as f:
        y_data = yaml.load(f, Loader=yaml.FullLoader)
        debug = y_data['debug']
        if debug == True : print("YAML file:\n", y_data)
    return (y_data)  
#===========================================================================================================
yaml_data = ProcessYAML('tools.yaml')                                     #yaml settings are global variables
debug = yaml_data['debug']                                                #debug mode?
#===========================================================================================================
if __name__ == "__main__":                                                    #only run when this is called by itself and not imported 
    desk1 = yaml_data['desk1']
    desk2 = yaml_data['desk2']
    
    
    #needs to go to yaml file
    command_lines = [
    "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    "C:\Program Files (x86)\Microsoft Office\Office16\OUTLOOK.EXE"
    ]

    for command_line in command_lines :
        command_line = "\"" + command_line + "\""
        subprocess.Popen(shlex.split(command_line))
    for website in desk1 :
        webbrowser.open_new(website)

    time.sleep(1)                                              #only 5 calls per min allowed

    #needs to go to yaml file
    command_lines = [
    "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    ]
    for command_line in command_lines :
        command_line = "\"" + command_line + "\""
        subprocess.Popen(shlex.split(command_line))

    for website in desk2 :
        webbrowser.open_new(website)
#WIP Need to workout how to open new virtual desktop
import webbrowser, yaml, time,ctypes, time, shlex, subprocess
import w_vda, win32gui
from cli_badges import badge
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
    desktops = w_vda.get_desktop_count()
    if debug == True : print(f"Number of desktops is: {desktops}.")
    if (desktops ==  1) : 
        print("Script requires at least 2 virtual desktops open.") 
        time.sleep(5)
        exit(1)
    desk1 = yaml_data['desk1']
    desk2 = yaml_data['desk2']
    execs1 = yaml_data['execs1']
    execs2 = yaml_data['execs2']
    if debug == True : print(f"Going to desk 0.")
    w_vda.go_to_desktop_number(0)                                              #now do desk 1 - gives warnings
    for command_line in execs1 : 
        command_line = "\"" + command_line + "\""
        if debug == True : 
            print (command_line)
        else : 
            subprocess.Popen(shlex.split(command_line))
            time.sleep(1)
    for website in desk1 :
        if debug == False : 
            webbrowser.open_new(website)
    time.sleep(1)
    # now prep desk 2
    w_vda.go_to_desktop_number(1)                                               #now do desk 2 - gives warnings
    for command_line in execs2 : 
        command_line = "\"" + command_line + "\""                                   
        if debug == True : 
            print (command_line)
        else : 
            subprocess.Popen(shlex.split(command_line))
            time.sleep(1)
            current_window_handle = win32gui.GetForegroundWindow()
            w_vda.move_window_to_desktop_number(current_window_handle,1)         #open en then move to desk 2
            time.sleep(1)
    time.sleep(1)
    for website in desk2 :
        if debug == False : webbrowser.open_new(website)
    time.sleep(1)
    w_vda.go_to_desktop_number(0)                                                   #now do desk 0 - gives warnings
    time.sleep(1) 
    Desk1Badge = badge("Browser 1 URLs opened",str(len(desk1)), messagebg='green',messagecolor='black')
    Desk2Badge = badge("Browser 2 URLs opened",str(len(desk2)), messagebg='blue')
    print(Desk1Badge, Desk2Badge)
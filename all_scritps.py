import webbrowser
import yaml
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
    for website in desk1 :
        webbrowser.open_new(website)
    for website in desk2 :
        webbrowser.open_new(website)
#WIP Need to workout how to open new virtual desktop
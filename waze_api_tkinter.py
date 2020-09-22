#https://github.com/kovacsbalu/WazeRouteCalculator/tree/master/WazeRouteCalculator
#https://docs.python.org/3/library/logging.html
from tkinter.constants import LEFT
import WazeRouteCalculator
import logging, yaml, datetime
import os
from time import sleep
import tkinter as tk
#============================================================================================================================
def screen_clear() :                                                                    # The screen clear function
   if os.name == 'posix':                                                               # for mac and linux(here, os.name is 'posix')
      _ = os.system('clear')
   else:                                                                                # for windows platfrom
      _ = os.system('cls')
   # print out some text

def ProcessYAML (yaml_file) :
    '''This function opens the yaml file and returns the data object'''
    with open(yaml_file) as f:
        y_data = yaml.load(f, Loader=yaml.FullLoader)
        debug = y_data['debug']
        if debug == True : print("YAML file:\n", y_data)
    return (y_data, debug) 
yaml_data, debug = ProcessYAML('waze_api.yaml')                                         # yaml settings are global variables

def PrintAllRoutes(all_routes, from_address, to_address) :
    print("=" * 90)
    if debug == True : print("R: ", type(all_routes), all_routes)
    print(f"From {from_address} to {to_address} @ at {datetime.datetime.now().strftime('%H:%M:%S on %d-%m-%Y')}")
    for key in all_routes:                                                           # dictionary 
        if debug == True : print(key, type(all_routes[key]), all_routes[key])
        print(f"Route {key}, distance {all_routes[key][1]:.2f} km, duration {all_routes[key][0]:.2f} min.")
    return()
#============================================================================================================================
class UpdateLabel():
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Traffic.")
        self.win.minsize(640, 240)
        self.ctr = 2
        #self.timer_var = tk.StringVar()
        self.route_var = tk.StringVar()
        route_txt = f"Traffic monitor: initialising..\n From xxx to yyy."
        self.route_var.set(route_txt)
        w_lab=tk.Label(self.win, textvariable=self.route_var, justify=tk.LEFT)
        w_lab.place(x=20, y=0)
        #lab=tk.Label(self.win, textvariable=self.timer_var, bg='#40E0D0', fg='#FF0000')
        #lab.place(x=20, y=150)
        self.updater()
        self.win.mainloop()
    def updater(self):
        self.ctr -= 1
        update_label = f"Traffic: Next update in {str(self.ctr)} seconds."
        #self.timer_var.set(update_label)
        self.win.title(update_label)
        if self.ctr > 0:
            self.win.after(1000, self.updater)
        else:
            routes = WazeRouteCalculator.WazeRouteCalculator(from_address, to_address, region, vehicle_type)
            all_routes_in = routes.calc_all_routes_info()
            #PrintAllRoutes(all_routes_in, from_address, to_address)
            route_txt = f"Traffic monitor @ at {datetime.datetime.now().strftime('%H:%M:%S on %d-%m-%Y')}\n\nFrom {from_address}\nTo {to_address}\n"
            for key in all_routes_in:                                                           # dictionary 
                route_txt = route_txt + f"Route {key}, distance {all_routes_in[key][1]:.2f} km, duration {all_routes_in[key][0]:.2f} min.\n"
            route_txt = route_txt + f"""\nFrom {to_address}\nTo {from_address}\n"""
            routes = WazeRouteCalculator.WazeRouteCalculator(to_address, from_address, region, vehicle_type)
            all_routes_out = routes.calc_all_routes_info()
            #PrintAllRoutes(all_routes_out, to_address, from_address)
            for key in all_routes_out:                                                           # dictionary 
                route_txt = route_txt + f"Route {key}, distance {all_routes_out[key][1]:.2f} km, duration {all_routes_out[key][0]:.2f} min.\n"
            self.route_var.set(route_txt)
            self.ctr = 60
            self.win.after(1000, self.updater)
#============================================================================================================================
if __name__ == "__main__":                                                           # only run when this is called by itself and not imported 
    if debug == True :
        logger = logging.getLogger('WazeRouteCalculator.WazeRouteCalculator')
        logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        logger.addHandler(handler)
    
    from_address = yaml_data['from_address']
    to_address = yaml_data['to_address']
    region = yaml_data['region']
    vehicle_type = yaml_data['vehicle_type']

    UL=UpdateLabel()


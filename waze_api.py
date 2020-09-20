#https://github.com/kovacsbalu/WazeRouteCalculator/tree/master/WazeRouteCalculator
#https://docs.python.org/3/library/logging.html
import WazeRouteCalculator
import logging, yaml, datetime

def ProcessYAML (yaml_file) :
    '''This function opens the yaml file and returns the data object'''
    with open(yaml_file) as f:
        y_data = yaml.load(f, Loader=yaml.FullLoader)
        debug = y_data['debug']
        if debug == True : print("YAML file:\n", y_data)
    return (y_data, debug) 
yaml_data, debug = ProcessYAML('waze_api.yaml')                                     #yaml settings are global variables

def PrintAllRoutes(all_routes, from_address, to_address) :
    print("=" * 90)
    if debug == True : print("R: ", type(all_routes), all_routes)
    print(f"From {from_address} to {to_address} @ at {datetime.datetime.now().strftime('%H:%M:%S on %d-%m-%Y')}")
    for key in all_routes:                                                           # dictionary 
        if debug == True : print(key, type(all_routes[key]), all_routes[key])
        print(f"Route {key}, distance {all_routes[key][1]:.2f} km, duration {all_routes[key][0]:.2f} min.")
    return()
if __name__ == "__main__":                                                    #only run when this is called by itself and not imported 
    if debug == True :
        logger = logging.getLogger('WazeRouteCalculator.WazeRouteCalculator')
        logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        logger.addHandler(handler)

    from_address = yaml_data['from_address']
    to_address = yaml_data['to_address']
    region = yaml_data['region']
    vehicle_type = yaml_data['vehicle_type']

    routes = WazeRouteCalculator.WazeRouteCalculator(from_address, to_address, region, vehicle_type)
    all_routes_in = routes.calc_all_routes_info()
    PrintAllRoutes(all_routes_in, from_address, to_address)

    routes = WazeRouteCalculator.WazeRouteCalculator(to_address, from_address, region, vehicle_type)
    all_routes_out = routes.calc_all_routes_info()
    PrintAllRoutes(all_routes_out, to_address, from_address)

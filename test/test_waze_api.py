#https://github.com/kovacsbalu/WazeRouteCalculator/tree/master/WazeRouteCalculator
#https://docs.python.org/3/library/logging.html

import WazeRouteCalculator
import logging

logger = logging.getLogger('WazeRouteCalculator.WazeRouteCalculator')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
logger.addHandler(handler)

from_address = '157b Hobsonville Road, Auckland, New Zealand'
to_address = '10 Kitchener Street , Auckland, New Zealand'
region = 'AU'
vehicle_type = 'PRIVATE'
route = WazeRouteCalculator.WazeRouteCalculator(from_address, to_address, region, vehicle_type)
route.calc_all_routes_info()

route = WazeRouteCalculator.WazeRouteCalculator(to_address, from_address, region, vehicle_type)
route.calc_all_routes_info()


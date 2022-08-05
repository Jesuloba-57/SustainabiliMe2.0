import requests
import json
from geopy.geocoders import Nominatim
import sys

class Transport():
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
        self.base_URL = "https://transit.router.hereapi.com/v8/routes?apiKey="
        self.api_key = "BJedH07Vrx2ay2ya73lzk3pQIZLKfvciXFNjzlrcF7M"
        self.origin = "&origin=" 
        self.destination = "&destination="

    def user_inputs(self):
        user_origin = self.src
        user_destination = self.dest
        return user_origin, user_destination

    def get_coords(self):
        org, dest = self.user_inputs()
        geolocator = Nominatim(user_agent="my-application-default")
        origin_location = geolocator.geocode(org)
        dest_location = geolocator.geocode(dest)
        o = str(origin_location.latitude) + ',' + str(origin_location.longitude)
        d = str(dest_location.latitude) + ',' + str(dest_location.longitude)
        return o, d

    def get_transit(self):
        o_coords, d_coords = self.get_coords()
        find_routes = requests.get(self.base_URL + self.api_key + self.origin + o_coords + self.destination + d_coords).json()
        try:
            routes = find_routes['routes'][0]['sections']
        except:
            return ("No route found.")
            sys.exit()
        transport = []
        destinations = []
        total_times = []
        for i in range(len(routes)):
            try:
                start_time = routes[i]['departure']['time'].split('T')[-1]
                end_time = routes[i]['arrival']['time'].split('T')[-1]

                start_time_hour = start_time[:2] + ":"
                start_time_min = start_time[3:5]

                end_time_hour = end_time[:2] + ":"
                end_time_min = end_time[3:5]

                total_times.append("Route Time: " + start_time_hour + start_time_min + "-" + end_time_hour + end_time_min)

            except:
                #print("Could not find departure time")
                total_times.append(-1)

            try:
                #print("Transportation Method:", routes[i]['type'])
                transport.append("Transit Type: " + routes[i]['type'])
            except:
                transport.append("Transit Type: Could not find departure transportation method")
        
            try:
                #print("Destination:", routes[i]['arrival']['place']['name'])
                destinations.append("Destination: " + routes[i]['arrival']['place']['name'])
            except:
                destinations.append("Destination: Final Destination")


            
        start = routes[0]['departure']['time'].split('T')[-1]
        end = routes[-1]['arrival']['time'].split('T')[-1]

        start_hour = start[:2] + ":"
        end_hour = end[:2] + ":"

        start_min = start[3:5]
        end_min = end[3:5]
        

        final_times = ("Estimated Journey Time: " + start_hour + start_min + "-" + end_hour + end_min)


        return transport, destinations, total_times, final_times



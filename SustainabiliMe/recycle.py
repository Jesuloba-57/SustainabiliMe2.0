import requests
import json
import urllib
import random
from geopy.geocoders import Nominatim

class Recycle:
    def __init__(self, zipcode, item):
        self.api_key = "424b735a5626aa76"
        self.base_url = "http://api.earth911.com/"
        self.zipcode = zipcode
        self.item = item



    # def get_materials(self):
    #     results = requests.get(self.base_url + 'earth911.getMaterials?api_key=' + self.api_key).json()
    #     results =(results['result'])
    #     recyclables = []
        
    #     for item in results:
    #         recyclables.append((item['description'], item['material_id']))
    #     return recyclables


    #Want to figure out some sort of dropdown for this
    def user_search(self):
        new_search = self.item #input("What would you like to search for?: ")
        clean_search = new_search.replace(" ", "_")
        search = requests.get(self.base_url + 'earth911.searchMaterials?api_key=' + self.api_key + '&query=' + clean_search)
        results = search.json()['result']
        selection = []
        for item in results:
            selection.append(item.get('material_id'))        
        
        # #print(results)
        # if len(results) == 1:
        #     selection = results.get('material_id')
        # else:
        #     indicator = 0
        #     while indicator == 0:   
        #         # for i in results:
        #         #     print(i['description'])
        #         new_prompt = input("Which option do you want?: ")
        #         clean_search = new_prompt.replace(" ", "_")
        #         search = requests.get(self.base_url + 'earth911.searchMaterials?api_key=' + self.api_key + '&query=' + clean_search)
        #         results = search.json()['result']
        #         #print(results)
        #         if len(results) == 1:
        #             selection = results.get('material_id')
        #             indicator = 1

        return selection
    

    def get_coords(self):
        loc_input = self.zipcode
        geolocator = Nominatim(user_agent="my-application-default")
        user_loc = geolocator.geocode(loc_input)
        try:
            loc_lat = round(user_loc.latitude, 2)
            loc_long = round(user_loc.longitude, 2)
            return str(loc_lat), str(loc_long)
        except AttributeError:
            return -1, -1

    def get_locations(self):
        latitude, longitude = self.get_coords()
        if latitude == -1 and longitude == -1:
            return -2
        geolocator = Nominatim(user_agent="my-application-default")
        id_list = self.user_search()
        if len(id_list) == 0:
            return -1   #exit clause if item is not found
        mat_id = str(id_list[0])
        search = requests.get(self.base_url + "earth911.searchLocations?api_key=" + self.api_key + "&latitude=" + latitude + 
        "&longitude=" + longitude + "&material_id=" + mat_id + "&max_distance=50")
        results = search.json()['result']
        return results


    """
    new_results = requests.get(base_url + 'earth911.searchMaterials?api_key=' + api_key + '&query=' + 'plastic')
    new_results = new_results.json()['result']
    print(len(new_results))

    #this = requests.get("http://api.earth911.com/earth911.searchMaterials?api_key=" + api_key + "&query=plastic")
    #this = this.json()
    #print(this)
    """

# geolocator = Nominatim(user_agent="my-application-default")

# for i in result[:10]:
#     print(i['description'])
#     print(i['distance'])
#     loc_lat = str(i['latitude'])
#     loc_long = str(i['longitude'])
#     coords = loc_lat + ", " + loc_long
#     location = geolocator.reverse(coords)
#     print(location)

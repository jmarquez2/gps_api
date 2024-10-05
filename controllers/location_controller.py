from flask_restful import Resource
from db.database_functions import get_locations
from datetime import datetime

class LocationController(Resource):
    
    def get(self, id):
        sorted_locations = sorted(get_locations(id), key = lambda x : x['timestamp'], reverse = True)
        locations = [ self.transformLocation(item) for item in  sorted_locations]
        return locations

    def transformLocation(self, item):
        return {
            "id" : item["id"],
            "dateTime" : str(datetime.fromtimestamp(int(item["timestamp"]))),
            "deviceId" : item["deviceId"],
            "latitude" : float(item["latitude"]),
            "longitude" : float(item["longitude"]),

        }
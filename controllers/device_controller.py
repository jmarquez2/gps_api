
from flask_restful import Resource
from db.database_functions import save_device, get_devices
from flask import request

class DeviceController(Resource):
    
    def get(self, id : str):
        return get_devices(id)

    
class AddDeviceController(Resource):
        
        def post(self):
            if "userId" not in request.json:
                return {"message" : "userId not found"}, 400

            return {"Device saved" : save_device(request.json)}
    
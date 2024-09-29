from flask import Flask
from flask_restful import Api

from controllers.gps_controller import GPSController
from controllers.device_controller import DeviceController, AddDeviceController



app = Flask(__name__)
api = Api(app)




api.add_resource(GPSController, '/gps')
api.add_resource(AddDeviceController, '/device')
api.add_resource(DeviceController, '/device/<string:id>')
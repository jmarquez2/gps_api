from flask import Flask
from flask_restful import Api

from gps_controller import GPSController



app = Flask(__name__)
api = Api(app)




api.add_resource(GPSController, '/gps')
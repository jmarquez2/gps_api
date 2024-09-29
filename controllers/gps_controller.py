import datetime
from flask import request
from flask_restful import Resource

from gps.gps_api import save_coordinates
import socketio



sio = socketio.Server(async_mode='threading')


class GPSController(Resource):

    @sio.event
    def connect(sid, environ, auth):
        print('connect ', sid)

    @sio.event
    def add_room_devices(sid):
        sio.enter_room(sid, 'devices')
        print(f'added {sid} to group devices')


    def get(self):
        return {'Hello' : str(datetime.datetime.now())}

    def post(self):
        
        result = save_coordinates(request.json)
        response = {'message' : result[1]}

        if result[0] == -1:
            return response, 400
        else :
            sio.emit(request.json["deviceId"], request.json, room='devices')
            return response


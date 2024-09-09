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
        print('connect ', sid)


    def get(self):
        return {'Hello' : str(datetime.datetime.now())}

    def post(self):
        
        result = save_coordinates(request.json)
        response = {'message' : result[1]}

        if not result[0]:
            return response, 400
        else :
            sio.emit('updated coordinates', request.json, room='devices')
            return response


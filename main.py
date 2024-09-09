from app import app as flaskApp
from gps_controller import sio
import socketio

app = socketio.WSGIApp(sio, flaskApp)



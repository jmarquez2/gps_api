from app import app as flaskApp
from controllers.gps_controller import sio
import socketio

app = socketio.WSGIApp(sio, flaskApp)



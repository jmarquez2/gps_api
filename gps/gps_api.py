from db .database_functions import save_gps_data

def save_coordinates(data) -> tuple:

    if 'latitude' not in data:
        return (-1, 'Latitude not set')
    if  'longitude' not in data:
        return (-1, 'Longitude not set')
    if 'deviceId' not in data:
        return  (-1, 'deviceId not set')
    
    if data.get("save"):
        save_gps_data(data)
        return (1, 'Saved data location')

    return (1, 'Data location recieved')

    

def save_coordinates(data) -> tuple:
    if 'latitude' not in data:
        return (False, 'Latitude not set')
    if  'longitude' not in data:
        return (False, 'Longitude not set')
    #TODO save function here
    
    return (True, 'Location data saved')

    
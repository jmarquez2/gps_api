
import boto3
from uuid import uuid4
from time import time
from decimal import Decimal
from boto3.dynamodb.conditions import Key


def save_gps_data(data):
  
    table = _get_table("location")

    table.put_item(
        Item = {
            'id' : str(uuid4()),
            'timestamp' : int(time()),
            'latitude' : Decimal(str(data["latitude"])),
            'longitude' : Decimal(str(data["longitude"])),
            'deviceId' : data["deviceId"]
        }
    )

def save_device(data):
    table = _get_table("devices")
    uid = str(uuid4())

    table.put_item(Item={
        "id" : uid,
        "userId" : data["userId"],
        "description" : data.get("description")
    })

    return uid

def get_devices(id : str):
    table = _get_table("devices")

    data = table.query(IndexName='userId-index', KeyConditionExpression = Key('userId').eq(id))
    return data.get("Items")

def get_locations(id : str):
    table = _get_table("location")

    data = table.query(IndexName = 'deviceId-index',  KeyConditionExpression = Key('deviceId').eq(id), ScanIndexForward=False, Limit=5)

    return data.get("Items")
    


def _get_table(name : str):
    dynamodb = boto3.resource('dynamodb')
    return dynamodb.Table(name)







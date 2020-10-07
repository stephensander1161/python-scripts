import os 
import sys
import datetime
import time 
import boto3

db = boto3.resource('dynamodb')
table = db.Table("Sensor")

response = table.get_item(
  Key={
    'Sensor_Id':"1"
    }
)
print(response["Item"])

class MyDb(object):

    def __init__(self, Table_Name='Sensor'):
        self.Table_Name = Table_Name
        self.db = boto3.resource('dynamodb')
        self.table = self.db.Table(Table_Name)
        self.client = boto3.client('dynamodb')



    def get(self, Sensor_Id='1'):
        response = self.table.get_item(
            Key={
                'Sensor_Id':Sensor_Id
            }
        )

        return response

    def put(self, Sensor_Id='', Temperature='', Humidity=''):
        self.table.put_item(
            Item={
                'Sensor_Id':Sensor_Id,
                'Temperature': Temperature, 
                'Humidity': Humidity
            }
        )

    def delete(self, Sensor_Id=''):
        self.table.delete_item(
            Key={
                'Sensor_Id': Sensor_Id
            }
        )

    def describe_table(self):
        response = self.client.describe_table(
            TableName='Sensor'
        )
        return response

obj = MyDb()
print(obj.describe_table())

resp = obj.put(Sensor_Id='1', Temperature='32', Humidity='787')

resp = obj.put(Sensor_Id='2', Temperature='32', Humidity='787')

delete = obj.delete(Sensor_Id='2')

    

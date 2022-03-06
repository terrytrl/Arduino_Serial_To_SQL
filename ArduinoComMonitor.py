import serial
from serial import Serial
import csv
from datetime import datetime
from time import sleep
import requests
import json
from io import StringIO
import sqlalchemy
import geocoder

ser = serial.Serial('COM3', 9600)

# mysql_conn = 'mysql+mysqldb://root:799677Ahdg23#@localhost/binance_price_stream'
# engine = sqlalchemy.create_engine(mysql_conn)


# def writeDataSQL(input):
    
#     json_data = pymysql.escape_string(input)
#     sql = "insert into all_tag ( index_name) values ('" + json_data + "') "
#     engine.execute(sql)

while True:

    sleep(2)
    LDRByteValue = ser.read()
    LDRdata = str(int.from_bytes(LDRByteValue, "big"))
    dateTime = str(datetime.today())
    
    sensorType = "LDR"
    # g = geocoder.ip('me')
    # location = str(g.latlng)
    location = "Hawthorn, Victoria"

    package = [dateTime, sensorType, location, LDRdata]
    
    url = 'http://localhost:3344/api/datapost'

    r = requests.post(url, json={ 
            "DateTime" : dateTime,
            "SensorType" : sensorType,
            "Location" : location,
            "LDRData" : LDRdata})
        
    with open('data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        
        writer.writerow(package)
        
        

        
        
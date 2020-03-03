from gpiozero import LED, Button
import serial
import sys
import time
import requests
import json

gps_led = LED(14)
request_led = LED(15)
lock_led = LED(24)
lock_switch = Button(23)

ser = serial.Serial('/dev/ttyUSB0', 9600)
    
def rfidData(id):
    if(ser.in_waiting >0):
        rfid = ser.readline()
        print(rfid)
        url = 'https://parcel-office.herokuapp.com/api/?train_ID={0},rfid={1}'.format(id, rfid)
        r = requests.get(url)
        data = r.json()
        if data['status']:
            print(data)


def sendData(id,lat,long,seal_status,parcel_status, rfid):
    url = 'https://parcel-office.herokuapp.com/api/?train_ID={0},lat={1},long={2},seal_status={3},parcel_status={4}'.format(id, lat, long, seal_status, parcel_status)
    r = requests.get(url)
    data = r.json()
    if data['status']:
        print('Data is successfully sended')
        request_led.on()
        gps_led.off()
        time.sleep(1)
        request_led.off()
        gps_led.on()
        print(data)
        
while True:
    id = 2
    lat = 21.35267
    long = 72.32678
    seal_status = lock_switch.is_active
    parcel_status = True

    if seal_status:
        lock_led.on()
        sendData(id,lat,long,seal_status,parcel_status, rfid)
    else:
        lock_led.off()
        rfid(id)

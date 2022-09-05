
from options import OUTDOOR_SENSOR_COM_NAME
from sensors import Sensor

import serial
import time


class OutdoorSensor(Sensor):
    def __init__(self) -> None:
        self.time_delay = 1 #  second
    
    def listen_sensor(self):
        with serial.Serial(OUTDOOR_SENSOR_COM_NAME) as sensor_com:
            while True:
                line = sensor_com.readline()
                str_line = line.decode('utf-8')

                print('Sensor shows ', str_line)
                
                if self.time_delay > 0:
                    time.sleep(self.time_delay)

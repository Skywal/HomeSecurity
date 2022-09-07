import serial
import time

from options import OUTDOOR_SENSOR_COM_NAME
from sensors import Sensor, SubscribersManager


class OutdoorSensor(Sensor):
    def __init__(self, subscribers_manager:SubscribersManager = None) -> None:
        self.time_delay = 1 #  second
        self.is_listen = True

        self.subscribers_manager = SubscribersManager()
        if subscribers_manager:
            self.subscribers_manager = subscribers_manager
        
        self.sensor_state: bool = False

        
    def listen_sensor(self) -> None:
        """
        Notify all subscribers only when sensor state has changed
        """

        with serial.Serial(OUTDOOR_SENSOR_COM_NAME) as sensor_com:
            old_sensor_state = self.sensor_state

            while self.is_listen:
                
                line = sensor_com.readline()
                str_line = line.decode('utf-8').split()
                
                try:
                    
                    self.sensor_state = self.__convert_com_signal(str_line[-1])

                    if old_sensor_state != self.sensor_state:
                        old_sensor_state = self.sensor_state
                        self.subscribers_manager.notify(self.sensor_state)
                    
                except Exception as e:
                    print(str(e))
                    
                if self.time_delay > 0:
                    time.sleep(self.time_delay)


    def __convert_com_signal(self, raw_signal:str) -> bool:
        if raw_signal:
            if raw_signal == "0":
                return False
            return True
        return False

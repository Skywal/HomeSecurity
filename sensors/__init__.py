import options

from abc import ABC, abstractmethod


#OUTDOOR_SENSOR_COM_NAME = options.OUTDOOR_SENSOR_COM_NAME

class Sensor(ABC):

    @abstractmethod
    def listen_sensor(self):
        pass
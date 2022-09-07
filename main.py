from sensors.door_sensor import OutdoorSensor
from sensors import OutdoorSensorSub

from threading import Thread, Lock
import time

lock = Lock()

outdoor_sensor = OutdoorSensor()
bot_subscriber = OutdoorSensorSub()

outdoor_sensor.subscribers_manager.subscribe(bot_subscriber)


sensor_thread = Thread(target=outdoor_sensor.listen_sensor)
sensor_thread.start()

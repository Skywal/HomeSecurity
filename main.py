from telegram_bot import basic_bot
from sensors.door_sensor import OutdoorSensor
from cctv.camera import Camera
from telegram_bot.basic_bot import CameraBot

from threading import Thread


## Telebot bot test
outdoor_sensor = OutdoorSensor()
cam = Camera()
basic_bot = CameraBot(cam)

outdoor_sensor.subscribers_manager.subscribe(basic_bot)

sensor_thread = Thread(target=outdoor_sensor.listen_sensor)
sensor_thread.start()

basic_bot.pooling()
## -------------------------------------------------------------------------------------
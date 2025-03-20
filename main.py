""" Camera bot entrypoint """

from options import LoggingConfig
LoggingConfig.configure_logging()

from logging import getLogger

from telegram_bot import basic_bot
from sensors.door_sensor import OutdoorSensor
from cctv.camera import Camera
from telegram_bot.basic_bot import CameraBot

from threading import Thread

# from telegram_bot import test

log = getLogger(__name__)

## Telebot bot test
outdoor_sensor = OutdoorSensor()
log.info('Outdoor sensor initialized.')

cam = Camera()
log.info('Camera initialized.')

basic_bot = CameraBot(cam)
log.info('Bot initialized.')

outdoor_sensor.subscribers_manager.subscribe(basic_bot)
sensor_thread = Thread(target=outdoor_sensor.listen_sensor)
sensor_thread.start()
log.info('Outdoor sensor pooling begin...')

log.info('Starting bot...')
basic_bot.pooling()
## -------------------------------------------------------------------------------------
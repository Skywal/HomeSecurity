import time
import telebot
from logging import getLogger

from sensors import Subscriber
from cctv.camera import Camera
from options import BOT_OPTIONS

log = getLogger(__name__)


class CameraBot(Subscriber):
    bot = telebot.TeleBot(BOT_OPTIONS.API_TOKEN)
    camera: Camera

    def __init__(self, camera: Camera) -> None:

        CameraBot.camera = camera
        self.chat_id: int = BOT_OPTIONS.GROUP_CHAT_ID
        self.bot_time_delay: float = 0.4
    
    @bot.message_handler(commands=['p'])
    def send_single_picture(message):
        byte_image = CameraBot.make_photo()
        # print(message.chat.id)
        CameraBot.bot.send_message(message.chat.id, "Photo on demand")
        CameraBot.bot.send_photo(message.chat.id, byte_image)
       
        log.info("The photo has been sent into char {}".format(message.chat.id))

    def update(self, context):
        CameraBot.bot.send_message(self.chat_id, "ALARM! SENSOR TRIGGERRED!")
        log.info("BOT: SENSOR TRIGGERRED!")

        for i in range(5):
            byte_image = CameraBot.make_photo()

        
            CameraBot.bot.send_photo(self.chat_id, byte_image)
            if self.bot_time_delay > 0.0:
                time.sleep(self.bot_time_delay)

        # return super().update(context)
    
    def pooling(self) -> None:
        self.bot.infinity_polling()

    @staticmethod
    def make_photo() -> bytes:
        image = CameraBot.camera.make_single_shot(is_resize=False)
    
        return image

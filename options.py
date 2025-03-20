import logging.config


OUTDOOR_SENSOR_COM_NAME: str = "/dev/ttyACM0"


class BOT_OPTIONS:
    API_TOKEN: str = 'Your telegram bot token'
    GROUP_CHAT_ID: int = 100101


class RTSP:
    USERNAME: str = 'username'
    PASSWORD: str = 'password'
    ADDRESS: str = 'address'


class LoggingConfig:

    LOGING_CONFIG = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': "[ %(asctime)s ] %(levelname)s - %(name)s %(lineno)d - %(process)d %(processName)s - %(thread)d %(threadName)s - %(message)s",
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'verbose',
                'level': 'INFO',
                # 'stream': 'ext: // sys.stdout',
            }
        },
        "root": {
            "handlers": ["console"],
            "level": "INFO",
        },
    }

    @classmethod
    def configure_logging(cls):
        logging.config.dictConfig(cls.LOGING_CONFIG)

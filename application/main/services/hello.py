from application.initializer import logger_instance
from application.main.config import AppConfig

logger = logger_instance.get_logger(__name__)
logs_dir = '{}/'.format(str(AppConfig().LOGS_DIR))


def say_hello(msg):
  return 'Hello ' % msg

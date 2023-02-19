import queue
import warnings
warnings.filterwarnings("ignore", category=UserWarning)


class LoggerInstance(object):
    def __new__(cls):
        from application.main.utility.logger.custom_logging import LogHandler
        return LogHandler()


class IncludeAPIRouter(object):
    def __new__(cls):
        from application.main.routers.api import router as router_face
        from fastapi.routing import APIRouter
        router = APIRouter()
        router.include_router(router_face, prefix='/api', tags=['sample'])
        return router

class Account(object):
    account = queue.Queue()
    
    @classmethod
    def load_account(cls,path):
        with open(path) as f:
            for line in f:
                data = {
                    "email":line.split(" ")[0],
                    "password":line.split(" ")[1].replace("\n","")
                }
                cls.account.put(data)
        return Account.account
# class MinIOInstance(object):
#     def __new__(cls):
#         from application.main.services.minio import MinioService
#         return MinioService()


queue_account = Account.load_account("data/account.txt")

logger_instance = LoggerInstance()


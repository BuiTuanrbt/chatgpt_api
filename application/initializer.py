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


class MinIOInstance(object):
  def __new__(cls):
    from application.main.services.minio import MinioService
    return MinioService()


logger_instance = LoggerInstance()

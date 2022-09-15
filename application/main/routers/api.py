from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

from application.initializer import logger_instance
from application.main.dto import obj_dto
from application.main.services import hello

router = APIRouter(prefix='/v1')
logger = logger_instance.get_logger(__name__)


@router.post("/hello")
async def index_face(obj: obj_dto.HelloDTO):
  try:
    logger.info('Start hello')
    face_vector = hello.face_encoding(obj.bucket_id, obj.obj_id)
    result = hello.index_face(face_vector, obj.cif, obj.cccd_cmnd, obj.phone, obj.image_id, obj.age, obj.last_update,
                              obj.name)
    return JSONResponse(content={
      'status': 'success',
      'message': 'Say hello to {} success!'.format(obj.msg)
    }, status_code=200)
  except Exception as e:
    return JSONResponse(content={
      'status': 'fail',
      'message': str(e)
    }, status_code=400)
    logger.error('Error detail: ', exc_info=True)

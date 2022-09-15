import io

from minio import Minio

from application.initializer import (logger_instance)
from application.main.config import settings


class MinioService(object):
  def __init__(self):
    self.logger = logger_instance.get_logger(__name__)
    self.client = Minio(endpoint=settings.MINIO_HOST,
                        access_key=settings.MINIO_ACCESS_KEY,
                        secret_key=settings.MINIO_SECRET_KEY,
                        secure=settings.MINIO_SECURE
                        )

  def get_list(self, domain):
    try:
      response = self.client.list_objects(str(domain))
      return response
    except Exception as e:
      self.logger.error('Error detail: ', exc_info=True)
      return None

  def get(self, bucket_id, obj_id):
    try:
      response = self.client.get_object(bucket_id, obj_id)
      return io.BytesIO(response.data)
    except Exception as e:
      self.logger.error('Error detail: ', exc_info=True)
      return None
    finally:
      # pass
      response.close()
      response.release_conn()

  def clone(self, bucket_id, obj_id):
    try:
      response = self.client.get_object(bucket_id, obj_id)
      return response.data
    except Exception:
      self.logger.error('Error detail: ', exc_info=True)
      return None
    finally:
      response.close()
      response.release_conn()

  def push(self, bucket_id, obj_id, obj):
    try:
      if not self.client.bucket_exists(bucket_id):
        self.client.make_bucket(bucket_id)
      self.client.fput_object(bucket_id, obj_id, obj)
    except Exception as e:
      self.logger.error('Error detail: ', exc_info=True)

  def make_bucket(self, bucket_id):
    try:
      if self.client.bucket_exists(bucket_id):
        return 0
      self.client.make_bucket(bucket_id)
    except Exception as e:
      self.logger.error('Error detail: ', exc_info=True)

  def remove_bucket(self, bucket_id):
    try:
      list_obj = self.client.list_objects(str(bucket_id))
      for obj in list_obj:
        self.client.remove_object(bucket_id, obj.object_name)
      self.client.remove_bucket(bucket_id)
    except Exception as e:
      self.logger.error('Error detail: ', exc_info=True)

  def remove(self, bucket_id, obj_id):
    try:
      if not self.client.bucket_exists(bucket_id):
        return -1
      self.client.remove_object(bucket_id, obj_id)
      return 0
    except Exception as e:
      self.logger.error('Error detail: ', exc_info=True)
      return -1

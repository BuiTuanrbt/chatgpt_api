from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware

from application.initializer import IncludeAPIRouter
from application.main.config import settings
from application.main.errors.http_error import http_error_handler
from application.main.errors.validation_error import http422_error_handler


def get_application():
  _app = FastAPI(title=settings.API_NAME,
                 description=settings.API_DESCRIPTION,
                 version=settings.API_VERSION)

  _app.add_exception_handler(HTTPException, http_error_handler)
  _app.add_exception_handler(RequestValidationError, http422_error_handler)

  _app.include_router(IncludeAPIRouter())

  _app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_HOSTS or ["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
  )
  return _app


app = get_application()


@app.on_event("shutdown")
async def app_shutdown():
  # on app shutdown do something probably close some connections or trigger some event
  print("On App Shutdown i will be called.")

# uvicorn.run("manage:app", host=settings.HOST, port=settings.PORT, log_level=settings.LOG_LEVEL, use_colors=True,reload=True)

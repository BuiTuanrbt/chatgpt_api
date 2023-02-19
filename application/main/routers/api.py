from fastapi.responses import JSONResponse, Response
import os
from application.main.services.chatbot import Chatbot
from fastapi.routing import APIRouter
import base64
from application.initializer import logger_instance, queue_account
from application.main.dto import obj_dto

router = APIRouter(prefix='/v1')
logger = logger_instance.get_logger(__name__)

@router.post("/hello")
async def hello(obj: obj_dto.HelloDTO):

    logger.info('Start hello')

    return JSONResponse(content={
        'status': 'success',
        'message': 'Hello'
    }, status_code=200)

user_sesstion={}
@router.post("/chat")
def chatting(request: obj_dto.QuestionRequest):
    user_id = request.user_id
    prompt = request.question

    flag = request.flag
    if user_id not in user_sesstion:
        if flag:
            logger.info(f'{user_id}Start browsing')
            try:
                user_sesstion[user_id] = Chatbot(config = queue_account.get())
            
                message = user_sesstion[user_id].ask(
                    prompt,
                    conversation_id=user_sesstion[user_id].config.get("conversation"),
                    parent_id=user_sesstion[user_id].config.get("parent_id"),
                )
                return JSONResponse(content={
                    "user_id": user_id,
                    "answer": message},status_code=200)
            except Exception as exc:
                return JSONResponse(content={exc}, status_code=500)
    else:
        if flag:
            logger.info(f'{user_id}Start chatting')
            try:
                message = user_sesstion[user_id].ask(
                    prompt,
                    conversation_id=user_sesstion[user_id].config.get("conversation"),
                    parent_id=user_sesstion[user_id].config.get("parent_id"),
                )
                return JSONResponse(content={
                    "user_id": user_id,
                    "answer": message},status_code=200)
            except Exception as exc:
                return JSONResponse(content={exc}, status_code=500)
        else:
            logger.info(f'{user_id}Stop chatting')
            del user_sesstion[user_id]
    
   

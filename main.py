import json
from fastapi import FastAPI, Request, requests
import os
from dotenv import load_dotenv
import httpx
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
app = FastAPI()

load_dotenv()

GROUP_ID =  os.getenv('CHAT_ID')
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
PROJECT_NAME = os.getenv('PROJECT_NAME')






async def sendTgMessage(message: str):
    """
    Sends the Message to telegram with the Telegram BOT API
    """
    tg_msg = {"chat_id": GROUP_ID, "text": message, "parse_mode": "Markdown"}
    API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    async with httpx.AsyncClient() as client:
     result = await client.post(API_URL, data = tg_msg)
     return result.json()

@app.post("/hook")
async def recWebHook(req: Request):
    """
    Receive the Webhook and process the Webhook Payload to get relevant data
    Refer https://developer.github.com/webhooks/event-payloads for all GitHub Webhook Events and Payloads
    """
    body = await req.json()
    print(body)
    event = req.headers.get("X-Github-Event")
    if event == "push":  # check if the event is a star
        ref = body["ref"]
        username = body["pusher"]["name"]
        msg = body["commits"][0]["message"]
        message = f"{username} ha pushato un aggiornamento sul progetto! \n *{PROJECT_NAME}*  \n sul branch: {ref} \n con il messaggio: *{msg}* \n"
        await sendTgMessage(message=message)
     
        





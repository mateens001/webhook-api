# main.py
from fastapi import FastAPI, Request
import httpx
import logging

app = FastAPI()

# Logging setup
logging.basicConfig(level=logging.INFO)

# Webhook Receiver
@app.post("/webhook")
async def receive_webhook(request: Request):
    payload = await request.json()
    logging.info(f"Webhook received: {payload}")
    return {"status": "received", "data": payload}

# Webhook Sender
@app.post("/trigger")
async def trigger_webhook():
    target_url = "http://host.docker.internal:8000/webhook"  # For local test
    payload = {"event": "test_event", "message": "Hello Webhook!"}
    
    async with httpx.AsyncClient() as client:
        response = await client.post(target_url, json=payload)

    return {"status": "sent", "response_code": response.status_code}

import asyncio

from pydantic import BaseModel

from browser_manager import BrowserManager
from fastapi import FastAPI, HTTPException
import uvicorn

class DecodePayload(BaseModel):
    contextId: str
    requestId: str
    result: str

class SignPayload(BaseModel):
    contextId: str
    path: str
    body: str

app = FastAPI()
browser_manager = BrowserManager(concurrent_browsers=1, contexts_per_browser=1)

@app.get("/health")
async def health():
    return {"message": "OK"}

@app.get("/fp")
async def get_fp():
    try:
        context = browser_manager.get_random_context()
        fingerprint = await context.get_fingerprint()
        user_agent = await context.get_user_agent()

        return {"status": "success", "result": fingerprint, "userAgent": user_agent, "timezone": context.timezone, "contextId": context.id}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/decode")
async def decode(payload: DecodePayload):
    try:
        context = browser_manager.get_context_by_id(payload.contextId)

        result = await context.decode_result(payload.requestId, payload.result)
        session_key = await context.get_session_key(result["tokenId"])

        return {"status": "success", "result": session_key}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/sign")
async def sign(payload: SignPayload):
    try:
        context = browser_manager.get_context_by_id(payload.contextId)
        session_sign = await context.get_session_sign(payload.path, payload.body)

        return {"status": "success", "result": session_sign}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))

async def run_fastapi():
    config = uvicorn.Config(app=app, host="127.0.0.1", port=8000, loop="asyncio")
    server = uvicorn.Server(config)
    await server.serve()

async def start_browser_manager():
    print("Starting browser manager....")
    await browser_manager.initialize()

async def main():
    await asyncio.gather(start_browser_manager(), run_fastapi())

asyncio.run(main())
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

# 1. Creiamo l'applicazione
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


# 2. Dati ricevuti dalla rotta POST
class Colpo(BaseModel):
    parola: str


# 3. Pagina principale
@app.get("/")
def home():
    return FileResponse("static/index.html")


# 4. Ping
@app.get("/ping")
def ping():
    return {"risposta": "pong"}


# 5. GET
@app.get("/gioca")
def gioca(parola: str):
    if parola == "ping":
        return {"risposta": "pong"}
    return {"risposta": "Non ho capito: scrivi ping"}


# 6. POST
@app.post("/gioca")
def gioca_post(colpo: Colpo):
    if colpo.parola == "ping":
        return {"risposta": "pong"}
    return {"risposta": "Non ho capito: scrivi ping"}
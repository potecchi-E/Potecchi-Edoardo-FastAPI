# main.py - il server del ping-pong, con GET e con POST
from fastapi import FastAPI
from pydantic import BaseModel
# 1. creiamo l'applicazione, cioè il server
app = FastAPI()

# 2. i dati che la rotta POST /gioca riceve: la parola del colpo
class Colpo(BaseModel):
    parola: str

# 3. ping: nessun dato, la risposta è sempre pong
@app.get("/ping")
def ping():
    return {"risposta": "pong"}

# 4. il colpo con GET: la parola arriva nell'indirizzo
@app.get("/gioca")
def gioca(parola: str):
    if parola == "ping":
        return {"risposta": "pong"}
    return {"risposta": "Non ho capito: scrivi ping"}

# 5. il colpo con POST: la parola arriva in JSON, nel corpo della richiesta
@app.post("/gioca")
def gioca_post(colpo: Colpo):
    if colpo.parola == "ping":
        return {"risposta": "pong"}
    return {"risposta": "Non ho capito: scrivi ping"}
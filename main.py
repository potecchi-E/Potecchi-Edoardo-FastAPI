# main.py - il server del ping-pong: ora legge la parola che scrivi
from fastapi import FastAPI
# 1. creiamo l'applicazione, cioè il server
app = FastAPI()

# 2. ping: nessun dato, la risposta è sempre pong
@app.get("/ping")
def ping():
    return {"risposta": "pong"}

# 3. il colpo con GET: la parola arriva nell'indirizzo e il server decide che cosa rispondere
@app.get("/gioca")
def gioca(parola: str):
    if parola == "ping":
        return {"risposta": "pong"}
    return {"risposta": "Non ho capito: scrivi ping"}
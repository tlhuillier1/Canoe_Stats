from fastapi import FastAPI
from app.routes import athletes

app = FastAPI(
    title="API Canoë-Kayak Stats",
    description="Récupère les données des athlètes FFCK",
    version="1.0.0"
)

# Inclusion des routes depuis routes/athletes.py
app.include_router(athletes.router)

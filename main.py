from fastapi import FastAPI
import requests


app = FastAPI()

@app.get("/")
def read_root():
    url = "https://cna-slalom.nicolas-abbal.com/api/ffck/boats/C1H282170"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
    else:
        data = {"message": "Erreur lors de l'appel"}
    
    return data

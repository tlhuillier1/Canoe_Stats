import requests
from fastapi import HTTPException

FFCK_BASE_URL = "https://cna-slalom.nicolas-abbal.com/api/ffck/boats/C1H282170"

def get_athlete_data() -> dict:

    url = f"{FFCK_BASE_URL}"
    response = requests.get(url)

    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="Athlète non trouvé")
    
    print(response.json())

    return response.json()

def compute_athlete_stats(data: dict) -> dict:

    people = data.get("people")
    
    if not people or len(people) == 0:
        raise ValueError("Aucune donnée 'people' trouvée dans la réponse.")

    person = people[0]

    stats = {
        "id": data.get("id"),
        "person": person
    }

    return stats